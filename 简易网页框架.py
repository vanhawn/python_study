#!/bin/env python3
# -*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup

class caiji(object):

    def first_step(self,target_url):#这里我设想出现了第一个接口 目标页
        #请求头可以从网上找一些其他的头添加进去，用来适应各种环境
        heads = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Connection' : 'keep - alive'
                }
        result = requests.get(target_url,headers = heads)
        return result

    def analyse(self,target_url):
        result = self.first_step(target_url)

        soup = BeautifulSoup(result.text,'lxml').find('div',class_='listmain').find_all('a')#这里我设想出现了第二个接口，网页标签参数，第三个接口，层数
        for ll in soup:
            l1 = target_url + ll.get('href')
            l2 = ll.string
            print(l1,l2)

    def file_save(self,result):
        with open('一念永恒.txt','r',encoding = 'utf-8') as f:
            f.write(内容)


caiji = caiji()
caiji.analyse('http://www.biqukan.com/1_1094/')
