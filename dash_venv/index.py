"""
Filename: index.py
Initial practice with Dash
"""

# Import dependencies
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as tfhub
import sqlite3
from sqlite3 import Error
import io

# Create a connection to the sqlite database
conn = sqlite3.connect('db\wine_data.sqlite', detect_types = sqlite3.PARSE_DECELTYPES)
c = conn.cursor()

# Read the table in the database
wine_df = pd.read_sql('Select * from wine_data', conn)

# Drop the duplicate descriptions
wine_df = wine_df.drop_duplicates('description')

# Drop null prices
wine_df = wine_df.dropna(subset=['price'])

# Filter the dataframe to include only varieties with more than 200 reviews
wine_df = wine_df.groupby('variety').filter(lambda x: len(x) > 200)

# Create a column named color
wine_df["color"] = ""

# Used to update the database with the wine color. Manually updated each wine variety
c.execute("update wine_data set color = 'red' where variety = 'Aglianico'  ")

# Commit the update to the database so it saves
conn.commit()

# Remove all the records without a color
wine_df = pd.read_sql("select country, description,rating,price,province,title,variety, winery, color  from wine_data where color in ('red', 'white', 'other')", conn)
wine_df.to_sql('wine_data', conn, if_exists = "replace")

print(wine_df.head())