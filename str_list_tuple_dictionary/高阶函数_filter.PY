#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#filter()函数用于过滤序列
	#filter()也接收一个函数和一个序列
	#filter()把传入的函数依次作用于每个元素
	#然后根据返回值是True还是False决定保留还是丢弃该元素
	#filter()函数返回的是一个迭代器，需要用for或list()等计算出来
def fn(x):
    return x % 2 == 1
l1 = [1,2,3,4,5,6,7,8,9]
l2 = filter(fn, l1) 	#只取奇数

def not_empty(x):
    return x and x.strip()
l3 = list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])) #去掉为空的元素

#用filter()求素数
	#先构造一个从3开始的奇数序列
def f1():
    n = 1
    while True:
        n += 2
        yield n

	#再定义一个筛选函数
def not_divisible(n):
    return lambda x: x % n > 0
 
 	#最后定义一个生成器，不断返回下一个素数
def prime():
    yield 2
    it = f1()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n),it)
 	#列出1000以内的素数
for i in prime():
    if i < 1000:
        print(i)
    else:
        break
		