#!/usr/bin/python3

# 打开一个文件
import os

f = open("foo.txt", "r", encoding='utf-8')

# num = f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
# print(num)
print(f.read())
# 关闭打开的文件
f.close()
