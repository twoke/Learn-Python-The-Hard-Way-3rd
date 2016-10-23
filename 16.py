
# -*- coding: utf-8 -*-

# ex16: Reading and Writing Files

from sys import argv
script, filename = argv

print "we're going to  erase %r." % filename
print "If you don't want that , hit CTRL-C(^c)."
print "If you want that, hit RETURN."

raw_input ("?")

print "Opening the file..."
target = open(filename,'w')

# target.truncate 对文件进行截断。
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

# target.write 写入文件
print "I'm going to write these to to file."
# target.write("%s\n%s\n%s\n" % (line1, line2, line3))
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
