# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 18:26:50 2021

@author: Heejun Lee
"""

# import libraries
from bs4 import BeautifulSoup
import numpy as np
from time import sleep
from random import randint
from selenium import webdriver
import pandas as pd
 
# creating empty data list
price_dt = []
mpg_dt = []
seat_dt = []
 
# reading the list of urls
 
df = pd.read_csv("linklist_11.csv")
mylist = df['link1'].tolist()
 
# Creating substring
 
for i in range(16):
    url = mylist[i]
    driver2 = webdriver.Chrome()
    driver2.get(url)
    sleep(randint(10, 20))
    soup = BeautifulSoup(driver2.page_source, 'html.parser')
 
    # First checking whether the link is valid
 
    fnd = '0'
 
    found = soup.find(class_="p-1 p-md-3 text-center display-1")
    if found is None:
        dummy = 1
    else:
        fnd = found.text
 
    nt = 'page not found'
    if nt in fnd:
        final = 0
        mpg = 0
        seat = 0
        price_dt.append(final)
        mpg_dt.append(mpg)
        seat_dt.append(mpg)
        fnd = '0'
 
    else: # price scraping
        try:
            price = soup.find(class_='heading-3').text
            final_price = price.replace("$", "")
            final_price = final_price.replace(",", "")
        except:
            final_price = 0
 
        if final_price.isnumeric():
            final = int(final_price)
        else:
            final = 0
        price_dt.append(final)
 
        # mpg scraping
        mpg_raw = soup.find_all(class_='px-1 px-lg-0_75 px-xl-1 py-0_5')[+4].text
        mpg_dt.append(mpg_raw)
 
        # seat cap scraping
        seat_raw = soup.find_all(class_='px-1 px-lg-0_75 px-xl-1 py-0_5')[+5].text
        seat_dt.append(seat_raw)
 
df = pd.DataFrame()
# forming the dataframe
 
df['price']=price_dt
df['mpg']=mpg_dt
df['seat']=seat_dt
 
print(df)