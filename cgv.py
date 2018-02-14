# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:26:51 2018

@author: 장지석
"""

import requests
from bs4 import BeautifulSoup
#from openpyxl import Workbook

url = "http://www.cgv.co.kr/movies/"
source = requests.get(url)
text_file = source.content

soup = BeautifulSoup(text_file, "html.parser")

ol = soup.find("ol")
li = ol.find_all("li")

for l in li:
    rank = l.find("div", {"class": "box-image"})
    strong1 = rank.find("strong").text
    print(strong1)
    reservation = l.find("div", {"class" : "score"})
    strong2 = reservation.find("strong").text
    print(strong2)    
    title = l.find("div", {"class": "box-contents"})
    strong3 = title.find("strong").text
    print(strong3)
    
    
"""
wb = Workbook()
ws = wb.active
wb.remove_sheet(ws)
list = wb.create_sheet("Titles")

wb.save('C:\\Users\\장지석\\Desktop\\titles.xlsx')
"""