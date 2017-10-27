#!/usr/bin/env python3
# -*- coding: utf-8 -*-
with open('list.py','r') as f:
	f.flush()	#直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入
	f.fileno()	#返回一个整型的文件描述符(file descriptor FD 整型)，可用于底层操作系统的 I/O 操作
	f.isatty()	#文件如果是一个终端设备返回 True，否则返回 False
	f.next()	#返回文件下一行
	f.read()	#读取整个文件
	f.read(size)	#读取指定字节数
	f.readline(size)	#读取事先，包括\n
	f.readlines(sizeint)#读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 
	#实际读取值可能比 sizeint 较大, 因为需要填充缓冲区
	
	f.seek()	#设置文件当前位置
	f.tell()	#返回文件指针当前位置
	f.truncate() #从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；
	#截断之后后面的所有字符被删除，其中 Widnows 系统下的换行代表2个字符大小。

	f.write()	#写入文件
	f.writelines()#向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符
	f.close()	#关闭文件  用with方法可以省略