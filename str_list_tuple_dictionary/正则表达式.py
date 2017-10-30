#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re 		#导入正则模块
num = '0755-12345'
#match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
test_m = re.match(r'^\d{4}-\d{1,8}$', num)  #匹配num,强烈建议写r，这样表达式中的转义可以不写\

#常见的判断方法、
test_n = input('请输入你的邮箱:')
mail_m = r'^[\w\d]+[\d\w_.]+@([\d\w]+).([\d\w]+)(?:.[\d\w]+)?$'
if re.match(mail_m, test_n):
    print('OK')
else:
    print('failed')

#切分字符串
l = 'a b     c'
l2 = l.split(' ')  #结果是['a', 'b', '', '', '', '', 'c']
l3 = re.split(r'\s+',l) #结果是['a', 'b', 'c']
l = 'a,b   c'
l2 = re.split(r'[\s\,]+', l) #结果是['a', 'b', 'c']

#分组
    #除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组
mat1 = r'^(\d{4})-(\d{1,8})$' #分别定义了两个组
m = re.match(mat1, num)
m.group(0)       #输出 0755-12345
m.group(1)       #输出 0755
m.group(2)       #输出 12345

#贪婪匹配
    #正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
re.match(r'^(\d+)(0*)$', '102300').groups() #输出('102300', '')
#由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了

re.match(r'^(\d+?)(0*)$', '102300').groups() #输出('1023', '00')
#必须让\d+采用非贪婪匹配，才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配

#编译
    #如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，
    #接下来重复使用时就不需要编译这个步骤了，直接匹配
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
re_telephone.match('010-12345').groups() #输出('010', '12345')
re_telephone.match('010-8086').groups()  #输出('010', '8086')


#模块方法

#re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败
re.match(pattern, string)

#re.search匹配整个字符串，直到找到一个匹配
re.search(pattern, string)

#通过正则表达式将字符串分离。如果用括号将正则表达式括起来
#匹配的字符串也会被列入到list中返回。maxsplit是分离的次数，
#maxsplit=1分离一次，默认为0，不限制次数
#re.split('\W+', 'Words, words, words.')和re.split('(\W+)', 'Words, words, words.')输出不一样
re.split(pattern, string, maxsplit=0) 

#正则表达式
re.compile(pattern)

#找到匹配的所有子串，并把它们作为一个列表返回。从左到右有序地返回。无匹配，返回空列表
re.findall(pattern, string)

#找到匹配的所有子串，并把它们作为一个迭代器返回。从左到右有序地返回。无匹配，返回空列表
re.finditer(pattern, string)

#找到匹配的所有子串，并将其用一个不同的字符串替换。
#可选参数 count 是模式匹配後替换的最大次数；count 必须是非负整数。
#缺省值是 0 表示替换所有的匹配。如果无匹配，字符串将会无改变地返回。
re.sub(pattern, repl, string, count=0, flags=0)
#例子
text = "JGood is a handsome boy, he is cool, clever, and so on..."
print(re.sub(r'\s+', '-', text))   #空格替换成 - 

#与re.sub方法作用一样，但返回的是包含新字符串和替换执行次数的两元组
re.subn(pattern, repl, string)
#例子
num = re.subn(r'\d{1}','-','123abc')  #返回('---abc', 3)

#对字符串中的非字母数字进行转义
re.escape(pattern)
#例子
num = re.escape(r'\d{1}') #返回 \\d\{1\}

#清空缓存中的正则表达式
re.purge()
