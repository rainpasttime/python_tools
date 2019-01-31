#-*-coding:utf-8-*-
import argparse
import sys
import os
import string


parser = argparse.ArgumentParser()
parser.add_argument("file",help="用双引号把文件名包含起来，每个文件名之间用空格进行区分")
parser.add_argument("search",help="想要被替换的字符串")
parser.add_argument("replace",help="想要替换的字符串")
parser.add_argument("newdir",help="新的目录路径，注意路径要以/结尾")
parser.add_argument("-s","--separate",default=" ",help="后面接分隔符，默认使用空格进行分隔")
args = parser.parse_args()

print(args.separate)

file_array = args.file.split(" ")
print(file_array)


for one_file in file_array:
	file_name = os.path.basename(one_file)     #从绝对路径中得到文件名
	file_new = args.newdir+file_name           #得到新的目录的绝对路径
	try:                                             #尝试打开旧文件
		fi = open(one_file,"r",encoding="UTF-8")
	except IOError:
		print("can't open "+one_file)
		continue 
	try:                                             #尝试打开新文件
		fn = open(file_new,"w",encoding="utf-8")
	except IOError:
		print("can't open "+file_new)
		fi.close()
		continue
	for s in fi.readlines():                          #读取一行
		print("s"+s)
		s_array = s.split(args.separate)           #以命令很中输入的分隔符进行分隔
		print(s_array)
		for word in s_array:                          #得到每一个单词
			if word==args.search:                     #相符的情况分为在行尾和不在行尾
				word=args.replace
				fn.write(word+args.separate)
			elif word==args.search+"\n":
				word=args.replace
				fn.write(word)
				fn.write("\n")
				break
			elif word.endswith("\n"):
				fn.write(word)
				break
			else:
				fn.write(word)
	fi.close()
	fn.close()
	
