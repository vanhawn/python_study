#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#sorted()	函数就可以对list进行排序
l = sorted([1,5,8,77,-11,-78])

#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
l1 = sorted([1,5,8,77,-11,-78],key=abs)  #abs是绝对值

#再看一个字符串排序的例子
l2 = sorted(['aVB','ve','VE','zg'],key=str.lower) #str.lower是大写转小写

#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
l3 = sorted(['aVB','ve','VE','zg'], key=str.lower, reverse = True)

#lambda (匿名函数)
    #关键字lambda表示匿名函数，冒号前面的x表示函数参数
    #匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
l4 = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

#匿名函数lambda x: x * x 实际上就是：
def f(x):
    return x * x

#也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y

l = build(22,44)
print(l())
