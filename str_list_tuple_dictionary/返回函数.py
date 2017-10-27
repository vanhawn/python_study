#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
    #通常情况下，求和的函数是这样定义的:
def f(*args):
    x = 0
    for i in args:
        x += i
    return x

#如果不需要立刻求和，而是在后面的代码中，根据需要再计算,那就返回求和的函数
def my_sum(*args):
    def sum():
        x = 0
        for i in args:
            x += i
        return x
    return sum
#当我们调用my_sum()时，返回的并不是求和结果，而是求和函数
f = my_sum(1,2,3,6,5,8,7,4)
print(f())

#请再注意一点，当我们调用my_sum()时，每次调用都会返回一个新的函数
f1 = my_sum(2,4,6,8)
f2 = my_sum(1,3,5,7)
print('我是f1,%s\n我是f2,%s'%(f1(),f2()))

#在函数my_sum中又定义了函数sum，并且内部函数sum可以引用外部函数my_sum的参数和局部变量，
#当my_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

#闭包
    #闭包用起来简单，实现起来可不容易
    #需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f1()才执行。来看一个例子
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
#你可能认为调用f1()，f2()和f3()结果应该是1，4，9 其实他的输出全是9
#原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，
#它们所引用的变量i已经变成了3，因此最终结果为9

#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
#如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
#无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()  #这次结果就分别是1、4、9
