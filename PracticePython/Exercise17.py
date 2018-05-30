# -*- coding: utf-8 -*-
"""
Use the BeautifulSoup and requests Python packages 
to print out a list of all the article titles on the New York Times homepage.
"""
import requests
from bs4 import BeautifulSoup

url="https://www.nytimes.com/"
req=requests.get(url)
req_html=req.text

soup=BeautifulSoup(req_html)
title=soup.find('span','article').string
print(title)