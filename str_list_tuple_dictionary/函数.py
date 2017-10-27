#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#定义函数的语法
def function():	    #def是defind的简写，后面跟的是函数名，()里是参数
	pass            #函数体

def area(w,h):      #计算面积的函数，有两个形参，w和h
    return w*h      #对参数进行处理

area(2, 3)          #调用函数，传实参2和3 (分别对应w,h,按顺序)

def printstr(my_str): 
    '''打印传进来的字符串'''     #函数说明
    print(my_str)      
    return          # return 后面为空或者不写return默认返回None

#位置参数
def power(x,y):  #这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和y
    return x*y

#默认参数
def power1(x,y=2):  #y=2叫默认参数，有默认参数，可只传实参给x.如果需要算2的5次方可传入2,5
    return x*y

#可变参数
def power(*nubmers): #形参为可变参数,调用该函数时，可以传入任意个参数，包括0个参数
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#扩展一下，*nums表示把nums这个list的所有元素作为可变参数传进去
num = [1,2,3,4,5,6,6]
power(*num)

#关键字参数
def person(name, age, **kw):    #关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个字典
    print('name:', name, 'age:', age, 'other:', kw)

person('huang', 22, city='shenzhen')  #输出结果 name: huang age: 22 other: {'city': 'shenzhen'}
person('weeds', 18, gender='M', job='Engineer') #输出结果 name: weeds age: 18 other: {'gender': 'M', 'job': 'Engineer'}

extra = {'city': 'shenzhen', 'job': 'Engineer'}
person('lee', 18,**extra)   #输出结果 name: lee age: 18 other: {'city': 'shenzhen', 'job': 'Engineer'}


#命名关键字参数  (命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错)
        #要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数
def person(name, age, *, city, job):    #命名关键字参数需要一个分隔符*，*后面的参数被视为命名关键字参数
    print(name, age, city, job) 

person('weeds', 24, city='shenzhen', job='Engineer')

        #如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *args, city, job):
    print(name, age, args, city, job)

        #命名关键字参数可以有缺省值，从而简化调用
def person(name, age, *, city='shenzhen', job):
    print(name, age, city, job)

person('lee', 24, job='Engineer') #调用时，可不传入city参数

#参数组合
        #在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
        #这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
        #在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
        #通过一个tuple和dict，你也可以调用上述函数
arg = (1, 2, 3, 4)
kww = {'d': 99, 'x': '#'}
f1(*arg, **kww)