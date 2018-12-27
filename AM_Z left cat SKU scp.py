#!/usr/bin/env python3
# -*- coding: utf-8 -*-

This code is basically when you have got the links for left cat nav using previous code and now you only want sku count of those links.


from lxml import html
import requests
import pandas as pd
import numpy as np 
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from contextlib import suppress
from time import sleep
from random import randint
from time import time
xlsx1 = pd.ExcelFile("/Users/sidharthjain/Downloads/pandas_simple2.xlsx")
xlsx1
df = xlsx1.parse("Sheet1")
links=df["Link to page"]
links1=links[0:10000]
links1

links_main=[]
count=[]
for index, i in enumerate(links1):
    with suppress(Exception):
        
    #page=Request(i, headers={'User-Agent': 'Mozilla/5.0'})
    #page1=urlopen(page).read()
        #print(i)
        #agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36)'}
        page = requests.get(i,headers=headers)
        print(index)
        sleep(randint(10,15))
        
        #requests+=1
        #elapsed_time=time()-start_time
        #print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
        #clear_output(wait = True)
        
        contents = page.content 
        #print(contents)
        soup = BeautifulSoup(contents, "lxml")
        soup.prettify()
        a=soup.find('span',attrs={'id':'s-result-count'})
        product_name=a.text
        print(product_name)
        links_main.append(i)
        count.append(product_name)
        
df1 = pd.DataFrame({'cat/subcat link': links_main, 'sku count': count})
df1
writer = pd.ExcelWriter('pandas_simple3.xlsx', engine='xlsxwriter',options={'strings_to_urls': False})
df1.to_excel(writer, sheet_name='Sheet1')

writer.save()
        
product_name
