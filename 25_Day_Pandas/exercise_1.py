'''
  Read the hacker_news.csv file from data directory
  Get the first five rows
  Get the last five rows
  Get the title column as pandas series
  Count the number of rows and columns
  Filter the titles which contain python
  Filter the titles which contain JavaScript
  Explore the data and make sense of it
'''

import pandas as pd
import numpy as np

df = pd.read_csv('../data/hacker_news.csv')
print(df.head(5))  # Get the first five rows
print(df.tail(5))  # Get the last five rows
