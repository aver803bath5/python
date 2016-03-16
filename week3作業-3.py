#-*-coding:utf-8-*-
fo=open("input.txt","r")
print "Name of the file: ", fo.name
line=fo.readlines()
fo.close()

line_num=len(line)
space_num=0
e_num=0
word_num=0


for x in range(0,line_num):
	e_num=line[x].count("e")+e_num
	space_num=line[x].count(" ")+space_num
	word_num=len(line[x])+word_num

print u"此英文文檔有 %d 個空白" %space_num
print u"此英文文檔有 %d 個 e 字母" %e_num
print u"此英文文檔有 %d 個 字元" %word_num

space_num=float(space_num)
e_num=float(e_num)
word_num=float(word_num)


space_portion=space_num/word_num*100

print u"此英文文檔的空白個數佔此文檔 %4.2f %%" %(space_num/word_num*100)
print u"此英文文檔的字母 \"e\" 個數佔此文檔 %4.2f %%" %(e_num/word_num*100)
