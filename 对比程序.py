#!/bin/env python3
# -*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup


target_url = 'http://www.biqukan.com/1_1094/'
head = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'connect':'keep-alive',
        #'referer':'http://www.kuaidaili.com/'
        }
target_req = requests.get(target_url,headers = head)
soup = BeautifulSoup(target_req.text,'lxml')#下方3个参数打算通过对外接口输入内容来解决
para1 = 'div'       #顶层标签
para2 = 'listmain' #顶层类别
para_bot = 'a'     #最终层标签
layer_number = 2
#while
soup_ml= soup.find(para1,{class_=para2}).find_all(para_bot)





for list_ml in soup_ml:
    chapter_url = target_url + list_ml.get('href')
    chapter_name = list_ml.get_text()
    print(chapter_url,chapter_name)
