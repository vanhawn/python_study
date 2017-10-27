#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#算术运算符
a = 'a'
b = 'b' 
c = 1
d = 2
x = a + b             #输出 ab
x = C + d             #输出 3
x = d - c             #输出 1
x = a * d             #输出 aa
x = c * d             #输出 2
x = d ** c            #输出 d的c次幂 这里输出2有1次方
x = d / c             #输出 2.0 带除，带小数
x = 9 // 2            #输出 4 只取商的整数部分 9.0//2.0 返回4.0
x = 21 % 4            #输出 1 返回除法的余数 取余或叫取模

#比较运算符
a == b                #比较对象是否相等
a != b                #比较对象是否不相等
a > b                 #比较a是否大于b
a < b                 #比较a是否小于b
a <= b                #比较a是否小于等于b
a >= b                #比较a是否大于等于b

#赋值运算符
=                     #简单的赋值运算符
+=                    #例如 i+=b 等价于 i=i+b
-=                    #与上类似
*=  /=   %=   **=   //=   #都与加法一样，无非是把+就成了别的算术运算

#逻辑运算符
and                   #布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值
or                    #布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值
not                   #布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。

#成员运算符
in                    #如果在指定的序列中找到值返回 True，否则返回 False。
not in                #如果在指定的序列中没有找到值返回 True，否则返回 False。

#身份运算符
is                    #判断两个标识符是不是引用自一个对象,例如：x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
is not                #判断两个标识符是不是引用自不同对象

#位运算符 (二进制，基本不用)
&                     #按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
|                     #按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
^                     #按位异或运算符：当两对应的二进位相异时，结果为1
~                     #按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1
<<                    #左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。
>>                    #右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数

#运算符优先级(括号()能改变优先级)
**                    #指数 (最高优先级)
~ + -                 #按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //              #乘，除，取模和取整除
+ -                   #加法减法
>> <<                 #右移，左移运算符
&                     #位 'AND'
^ |                   #位运算符
<= < > >=             #比较运算符
>< == !=              #等于运算符
= %= /= //= -= += *= **=    #赋值运算符
is is not             #身份运算符
in not in             #成员运算符
not or and            #逻辑运算符