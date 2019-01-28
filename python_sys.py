import sys
import os
import string
import re

#argv[1]数据类型是字符串。是文件列表，运行的时候输入为 "A文件名 B文件名 C文件名"  这些文件名如果不在一个文件夹，那么必须是绝对地址
#argv[1]如果是相对地址，那么这些文件名必须全部在同一个文件夹内，并且这个文件也要在那个文件夹内
#argv[2]是想要被替换的字符串
#argv[3]是想要替换的字符串
#argv[4]数据类型是字符串。是新的目录的路径，需要包含最后的/，同时也不需要文件名，直接取原来的文件名进行

file_array = sys.argv[1].split(" ")
for one_file in file_array:
	file_name = os.path.basename(one_file)     #从绝对路径中得到文件名
	file_new = sys.argv[4]+file_name           #得到新的目录的绝对路径
	#regrex_one = re.compile("\W"+sys.argv[2])
	#regrex_two = re.compile(sys.argv[2]+"\W")
	try:                                             #尝试打开旧文件
		fi = open(one_file,"r",encoding="UTF-8")
	except IOError:
		print("can't open "+one_file)
		continue 
	try:                                             #尝试打开新文件
		fn = open(file_new,"a+")
	except IOError:
		print("can't open "+file_new)
		fi.close()
		continue
	for s in fi.readlines():                          #读取一行
		'''s_array = s.split(" ")
		for word in s_array:                          #得到每一个单词
			if word==sys.argv[2]:                     #相符的情况分为在行尾和不在行尾
				word=sys.argv[3]
			elif word==sys.argv[2]+"\n":
				word=sys.argv[3]+"\n"
				fn.write(word)
				continue
			elif word.find("\n")!=-1:                #不相符的情况在行尾也需要进行处理
				fn.write(word)
				continue
			fn.write(word+" ")'''
		s_array = re.split("\W",s)
		for word in s_array:                          #得到每一个单词
			if word==sys.argv[2]:                     #相符的情况分为在行尾和不在行尾
				word=sys.argv[3]
			elif word==sys.argv[2]+"\n":
				word=sys.argv[3]+"\n"
				fn.write(word)
				continue
			fn.write(word+" ")
		fn.write("\n")

	fi.close()
	fn.close()





