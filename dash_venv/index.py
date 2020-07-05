"""
Filename: index.py
Initial practice with Dash
"""

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import sqlite3

import plotly.graph_objs as go

conn = sqlite3.connect(r"C:\Users\MTGro\Desktop\coding\wineApp\db\wine_data.sqlite")
c = conn.cursor()
df = pd.read_sql("select * from wine_data", conn)
df = df[['country', 'description', 'rating', 'price','province','title','variety','winery','color']]
df.head(1)