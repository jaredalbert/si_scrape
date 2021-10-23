import os
import glob
import pandas as pd
os.chdir(r'C:\Users\Windows10\Desktop'      \
         r'\from old dell\Python_files\SI_scraper')
files = [i for i in glob.glob('*.csv')]
combined_files = pd.concat([pd.read_csv(i) for i in files])
combined_files.to_csv('combined.csv', index = False, encoding = 'utf-8-sig')
print('done')