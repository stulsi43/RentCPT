# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 22:03:41 2020

@author: Sohail Tulsi
"""
import pandas as pd
import numpy as np
import datetime
now = datetime.datetime.now()

df = pd.read_csv('prop24_unclean.csv')

# drop blank from adverts
df['Raw_Data'].replace('', np.nan, inplace=True)
df.dropna(subset=['Raw_Data'], inplace=True)

#reduced price 
df['reduced_yn'] = df['Raw_Data'].apply(lambda x: 1 if 'reduced' in x.lower() else 0)

#price
df['price'] = df['Raw_Data'].apply(lambda x: x.partition("R ")[2].partition("\n")[0])

# drop blank no price
df['price'].replace('', np.nan, inplace=True)
df.dropna(subset=['price'], inplace=True)

#house or apartment
df['apartment_house'] = df['Raw_Data'].apply(lambda x: x.partition("Bedroom")[2].partition("\n")[0])

# no of bedrooms
df['bedrooms'] = df['Raw_Data'].apply(lambda x: x.partition("\n")[2].partition("\n")[2].partition("\n")[0])

#area
df['area'] = df['Raw_Data'].apply(lambda x: x.partition("\n")[2].partition("\n")[2].partition("\n")[2].partition("\n")[0])

#meterage
meter = df['Raw_Data'].apply(lambda x: x.partition(" ")[2].partition(" m²")[0])
#for j in range(len(lines)):
#    for i in range(len(lines[j])):
        #(df['price'] = df['Raw_Data'].apply(lambda x: x.split('\n')[i])) if 'R ' in df['Raw_Data'][j].apply(lambda x: x.split('\n')[i]) else None
#price = lines.partition("R ")[2].partition(",")[0]

#return print(df)      
#house or apartment
#row_1 = df['Raw_Data'].apply(lambda x: x.split('\n')[0])
#row_2 = df['Raw_Data'].apply(lambda x: x.split('\n')[1])
#row_3 = df['Raw_Data'].apply(lambda x: x.split('\n')[2])
#row_4 = df['Raw_Data'].apply(lambda x: x.split('\n')[3])
#row_5 = df['Raw_Data'].apply(lambda x: x.split('\n')[4])
#row_6 = df['Raw_Data'].apply(lambda x: x.split('\n')[5])
#row_7 = df['Raw_Data'].apply(lambda x: x.split('\n')[6])

#lines = df['Raw_Data'].apply(lambda x: x.split('\n'))
#rawdata_length = len(lines)