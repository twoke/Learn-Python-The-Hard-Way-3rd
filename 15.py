
# -*- coding: utf-8 -*-

# ex15: Reading Files

# import argv 变量。 从 sys 模块
from sys  import argv

# 得到 argv的变量
script, filename = argv

# 打开一个文件
txt = open(filename)

# 打印变量的名字
# 读取文件的名字
print "Here's your file %r:" % filename
print txt.read()

# 关闭文件
txt.close()

# 再一次打印文件名
# 输入新的文件名
print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()

txt_again.close()
