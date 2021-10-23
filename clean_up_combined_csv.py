import pandas as pd
from rich import print as rprint
path = r'C:\Users\Windows10\Desktop\from old dell\Python_files\SI_scraper\combined.csv'
df = pd.read_csv(path)
#rprint(df.poster.value_counts())
df['Date'] = pd.to_datetime(df['Date'])
df= df.sort_values(by = 'Date')
df.drop('Unnamed: 0', axis =1, inplace = True)
df = df.drop_duplicates(keep='first', inplace=False, ignore_index=True)
df.to_csv('cleaned_combined.csv', index = False, encoding = 'utf-8-sig')