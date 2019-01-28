# function find a string and replace woth another string
import os
import string

file_old = "C:/Users/Administrator/Desktop/apple.txt"
file_new = "C:/Users/Administrator/Desktop/new.txt"

search_for = "apple"

replace_with = "orange"

try:
	fo = open(file_old,"a+")
except IOError:
	print("can't open old file")

try:
	fn = open(file_new,"a+")
except IOError:
	print("can't open new file")

#用a+的方式打开文件，文件指针默认在文件尾部，所以必须用seek函数，把指针指定在自己想要指定的地方
fo.seek(0,0)      #指定在起点，偏移量是0


#这里有一个注意点，readline()函数和readlines()函数是不一样的,readline()函数得到的是一个字符串
#readlines()得到的是一个字符串列表，里面每一个元素是一行
for s in fo.readlines():
	s_new = s.replace(search_for,replace_with)
	fn.write(s_new)

fo.close()
fn.close()




