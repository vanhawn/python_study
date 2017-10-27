#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#数字类型
int 		#整数  如1 100 56369  -256  -0x260 0x69
float 		#浮点娄 如 1.2 4.3 -6.5	-32.54e100 	32.3+e18
complex 	#复数 如 3.14j 	9.322e-36j -.6545+0J

#数字类型转换
int(x)			#将x转换为一个整数
float(x)		#将x转换到一个浮点数
complex(x)		#将x转换到一个复数，实数部分为 x，虚数部分为 0
complex(x, y)	#将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式

#数学函数  (有些需要导入 math 模块)
abs(x)			#返回数字的绝对值，如abs(-10) 返回 10
ceil(x)			#返回数字的上入整数，如math.ceil(4.1) 返回 5
max()			#返回给定参数的最大值，参数可以为序列。
fabs(x)			#返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)		#返回数字的下舍整数，如math.floor(4.9)返回 4
min()			#返回给定参数的最小值，参数可以为序列。
sqrt(x)			#返回x的平方根

#随机数函数 
import random
random.choice()	#返回一个列表，元组或字符串的随机项
random.randrange()  #返回一个随机数，random.randrange(1, 100, 2)) 产生一个100以内的奇数
random.random()		#返回随机生成的一个浮点数数，它在[0,1)范围内
random.shuffle(x)   #随机将序列如列表 排序
random.uniform(x, y)#将随机生成下一个浮点数，它在[x,y]范围内
