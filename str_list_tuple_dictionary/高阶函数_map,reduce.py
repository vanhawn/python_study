#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def f(x):
	return x * x
#map 
        #把后面传的可迭代对象依次传给在第一个传进去的函数
        #map()函数接收两个参数，一个是函数，一个是可迭代对象
l1 = [1,2,3,4,5,6,7]
l2 = map(f,l1)      #算出列表中每个数的平方
print(list(l2))     #l2是个迭代器，我们需要用list把每个元素计算出来
l3 = map(str,l1)    #把列表中的每个元素转成字符
print(list(l3))

#reduce
from functools import reduce
        #必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
    #第一个例子，求所有数的和
def f1(x,y):
    return x+y

l4 = reduce(f1,l1)
print(l4)
    
    #第二个例子，把l1里的元素合成一个整数 1234567
def f2(x,y):
    return x * 10 + y
l5 = reduce(f2,l1)
print(l5)

#整合例子
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
print(str2int('123312'))