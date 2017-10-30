#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os  
print(os.getcwd())   #获取当前的操作目录，即当前Python脚本工作的目录路径  
#os.chdir("/PythonCode/test")   #改变当前脚本工作目录，相当于shell下的cd  
os.chdir(r"/pythoncode/test/test")     #与上面一句等价（推荐使用）  
print(os.getcwd())  
print(os.curdir)  #返回当前目录 '.'  
print(os.pardir)  #获取当前目录的父目录字符串名 '..'  
  
os.makedirs(r"/pythoncode/a/b/c")   #生成多层递归目录  
#若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推  
os.removedirs(r"/pythoncode/a/b/c")    #清理空文件夹  
  
os.mkdir(r"/pythoncode/test/t")   #生成单级目录，相当于shell中mkdir filename  
os.rmdir(r"/pythoncode/test/t")   #删除单级空目录，若目录不为空，无法删除或报错；相当于shell中rmdir filename  
  
print(os.listdir(r"/pythoncode/test/test"))   #列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印  
  
os.remove(r"/pythoncode/test/test/1.py")   #删除一个文件  
os.rename(r"/pythoncode/test/test/1.py",r"/pythoncode/test/test/2.py")   #重命名文件/目录  
print(os.stat(r"/pythoncode/test/test"))     #获取文件/目录信息  
  
print(os.sep)      #输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"  
print(os.linesep)  #输出当前平台使用的行终止符，win下为"\r\n",Linux下为"\n"  
print(os.pathsep)  #输出用于分割文件路径的字符串,win下为";",Linux下为":"  
print(os.environ)  #查看系统的环境变量  
print(os.name)     #输出字符串指示当前使用平台。win->'nt'; Linux->'posix'  
print(os.system("dir"))  #运行shell命令，直接显示  
print(os.path.abspath(r"/pythoncode/test"))   #返回path规范化的绝对路径  
print(os.path.split(r"/pythoncode/test/test/1.py"))  #将path分割成目录和文件名二元组返回  
print(os.path.dirname(r"/pythoncode/test"))    #返回path的目录。其实就是os.path.split(path)的第一个元素  
print(os.path.basename(r"/pythoncode/test"))   #返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。  
print(os.path.exists(r"/pythoncode/test"))   #如果path存在，返回True；如果path不存在，返回False  
print(os.path.isabs(r"/pythoncode/test"))    #如果path是绝对路径，返回True  
print(os.path.isfile(r"/pythoncode/test/p_test.py"))   #如果path是一个存在的文件，返回True,否则返回False  
print(os.path.isdir(r"/pythoncode/test"))    #如果path是一个存在的目录，则返回True。否则返回False  
print(os.path.join(r"/PythonCode",r"/test",r"/day"))   #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略  
print(os.path.getatime(r"/pythoncode/test"))    #返回path所指向的文件或者目录的最后存取时间  
print(os.path.getmtime(r"/pythoncode/test"))    #返回path所指向的文件或者目录的最后修改时间  