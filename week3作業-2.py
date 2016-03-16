#-*-coding:utf-8-*-
x=raw_input("Please Enter a number: ")
x=int(x)
if x==2:
	print u" \"%d\" 是質數！" %x
elif x==1:
	print u" \"%d\" 不～是質數！" %x
for y in range(2,x):
	if x%y==0:
		print u" \"%d\" 不～是質數！" %x
		break
	elif y==x-1:
		print u" \"%d\" 是質數！" %x

