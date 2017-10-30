#!/usr/bin/env python3
# -*- coding: utf-8 -*-
list_1=[1,4,5,7,3,6,7,9]
list_1=set(list_1)
list_2=set([2,6,0,66,22,8,4])
list_3=set([1,3,7])
list_4=set([5,6,8])
print(list_1.intersection(list_2))          #取交集
print(list_1 & list_2)

print(list_1.union(list_2))                 #取并集
print(list_1 | list_2)

print(list_1.symmetric_difference(list_2))  #把交集去掉，把互相都没有的取出来，对称差集
print(list_1 ^ list_2)

print(list_1.difference(list_2))            #取差集  只保留1里有，2里没有的
print(list_1 - list_2)
print(list_2.difference(list_1))
print(list_2 - list_1)

print(list_1.issubset(list_2))              #判断list_1是不是list_2的子集
print(list_3.issubset(list_1))              #判断list_3是不是list_1的子集
print(list_1.issuperset(list_2))            #判断list_2是不是list_1的父集
print(list_3.isdisjoint(list_4))            #判断是否无交集

list_1.add(777)                             #增加一项
list_1.update(999,888)                      #添加多项
list_1.remove(999)                          #删除
list_1.discard('dddd')                      #不存在数值执行删除不报错
999 in  list_1                              #判断999在不在list_1里
999 not in list_1

list_1.pop()                                #删除任意一个，并返回
