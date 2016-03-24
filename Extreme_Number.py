#-*-coding:utf-8-*-
import random
guess=0
y=int(random.random()*99)

print u"終極密碼 GO~"

x=-1
while x<0 or x>99:
	x=input("Enter the number you guess(0~99):")
	int(x)		
guess+=1

little=0
big=99
while x!=y:
	if x>y:
		# print y
		big=x
		print "Now range is %d to %d" %(little,big)
		x=input("Enter the number you guess(0~99):")
		while x>big or x<little:
			print "Out of range!!!"
			x=input("Enter the number you guess(0~99):")
		int(x)
		guess+=1
	elif x<y:
		# print y
		little=x
		print "Now range is %d to %d" %(little,big)
		x=input("Enter the number you guess(0~99):")
		while x>big or x<little:
			print "Out of range!!!"
			x=input("Enter the number you guess(0~99):")
		int(x)
		guess+=1
print "Congratuation!!! The answer is %d, you guess %d times" %(y,guess)