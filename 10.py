# -*- coding: utf-8 -*-

# ex10: What Was That?

print "I am 6'2\" tall."  # 将字符串中的双引号转义
print 'I am 6\'2" tall.'  # 将字符串中的单引号转义

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* cat food\n\t* Fishies\n\t* catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Assign string value for each variable
intro = "I'll print a week"
mon = "Mon"
tue = "Tue"
wed = "Wed"
thu = "Thu"
fri = "Fri"

print "%s\n%s\n%s\n%s\n%s\n" % (mon, tue, wed, thu, fri)
print "%r" % intro
print "%r" % "She said \"I'll print a week\""

print "%s" % intro
print "%s" % "She said \"I'll print a week\""
