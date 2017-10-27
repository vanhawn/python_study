#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#列表生成式
i = [x * x for x in range(1,100)]
j = [x * x for x in range(1,100) if x % 2 == 0]
k = [x + y for x in 'xyz' for y in 'abc']

import os
l = [d for d in os.listdir('.')]        # os.listdir可以列出文件和目录

d = {'x': 'A', 'y': 'B', 'z': 'C'}
jk = [k + '=' + v for k, v in d.items()]

l1 = ['Hello', 'World', 'IBM', 'Apple']
l2 = [s.lower() for s in l1]            #lower把大写变小写,参考字符串处理方法


#生成器
g = (x * x for x in range(10))    #创建一个生成器有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()
#生成器保存的是算法 每次调用next(g)就计算出g的下一个元素的值,算出最后一个元素后再用next()抛出StopIteration的错误
#不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象


#第二种创建方法，写函数,如果一个定义中包含yield关键字那么这个函数就是个生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


#最难理解的就是生成器和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成生成器的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
#举个简单的例子，定义一个生成器，依次返回数字1，3，5
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)


#用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，
#必须捕获StopIteration错误，返回值包含在StopIteration的value中
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


print('\a')