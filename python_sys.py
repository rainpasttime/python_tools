import sys
import os
import string

#argv[1]数据类型是字符串。是文件列表，运行的时候输入为 "A文件名 B文件名 C文件名"  这些文件名如果不在一个文件夹，那么必须是绝对地址
#argv[1]如果是相对地址，那么这些文件名必须全部在同一个文件夹内，并且这个文件也要在那个文件夹内
#argv[2]是想要被替换的字符串
#argv[3]是想要替换的字符串
#argv[4]数据类型是字符串。是新的目录的路径，需要包含最后的/，同时也不需要文件名，直接取原来的文件名进行

file_array = sys.argv[1].split(" ")
for one_file in file_array:
	file_name = os.path.basename(one_file)     #从绝对路径中得到文件名
	file_new = sys.argv[4]+file_name           #得到新的目录的绝对路径

	#search_for_one = " "+sys.argv[2]+"\\n"      #考虑换行的前一个字的全词匹配
	#replace_with_one = " "+sys.argv[3]+"\\n"         
	#search_for_two = sys.argv[2]+" "           #考虑每一行前面的第一个字的全词匹配
	#replace_with_two = sys.argv[3]+" "
	#search_for_three = " "+sys.argv[2]+" "     #考虑每一行中间的单词的全词匹配
	#replace_with_three = " "+sys.argv[3]+" "
	#print(search_for)
	#print(file_new)

	try:                                             #尝试打开旧文件
		fi = open(one_file,"r",encoding="UTF-8")
	except IOError:
		print("can't open "+one_file)
		continue 
	try:                                             #尝试打开新文件
		fn = open(file_new,"w")
	except IOError:
		print("can't open "+file_new)
		fi.close()
		continue
	for s in fi.readlines():
		s_new = s.replace(sys.argv[2],sys.argv[3])
		
		

		'''s_new = s.replace(search_for_one,replace_with_one)  
		s_new = s.replace(search_for_two,replace_with_two) 
		s_new = s.replace(search_for_three,replace_with_three)'''
		fn.write(s_new)
	fi.close()
	fn.close()





