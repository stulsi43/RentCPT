# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 01:00:18 2020

@author: Sohail Tulsi
"""
import prop24_scraper as ps
import pandas as pd

DRIVER_PATH = 'C:/Users/stuls/Documents/ct_rent_proj/chromedriver'
url = 'https://www.property24.com/to-rent/western-cape/9?sp=rr%3dMonth&PropertyCategory=House%2cApartmentOrFlat'
slp_time = 1

df = ps.get_prop24(url,DRIVER_PATH,slp_time)

df.to_csv('prop24_unclean.csv', index= False)


