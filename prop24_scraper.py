# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 22:23:31 2020

@author: Sohail Tulsi
"""

from selenium import webdriver
import time
import pandas as pd


def get_prop24(url,DRIVER_PATH,slp_time):
    
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.set_window_size(1120, 1000)
    driver.get(url)

    max_tabs = int(driver.find_element_by_xpath('/html/body/div[1]/div[9]/div/div/div[1]/div[4]/div/ul/li[8]/a').text)
    listing_numbers = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21']
    data = []


    for j in range(max_tabs):
        try:
            try:
                try:
                    for i in listing_numbers:
                        try:
                            listing_info = driver.find_element_by_xpath('/html/body/div[1]/div[9]/div/div/div[1]/div[3]/div['+ i +']').text
                            data.append(listing_info)
                        except:
                            pass
                            
                except:
                    pass
                driver.find_element_by_xpath('/html/body/div[1]/div[9]/div/div/div[1]/div[4]/a[2]').click()
                time.sleep(slp_time) #Change to let the page load.
            except:
                pass
            driver.find_element_by_xpath('/html/body/div[1]/div[9]/div/div/div[1]/div[5]/a[2]').click()
            time.sleep(slp_time) #Change to let the page load.
        except:
            pass
    
   
    return pd.DataFrame(data, columns = ['Raw_Data'])


