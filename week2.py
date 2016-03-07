#-*-coding:utf-8-*-
money=5000
f=open("ATM.txt","w")

while money>0:
	print u"請輸入提款金額"
	f.write("請輸入提款金額\n")
	withdraw=raw_input()
	if withdraw.isdigit():
		money=money-int(withdraw)
		if money<0:
			str="您的存款不足"
			print str.decode("utf-8")
			f.write("%s\n" %str)
		elif money>0:
			str="您的存款還剩%d元" %money
			print str.decode("utf-8")
			f.write("%s\n" %str)
		else:
			str="您的存款無剩餘存款"
			print str.decode("utf-8")
			f.write("%s\n" %str)
		print money
		
f.close()

g=open("ATM.txt")
line=g.readlines()
line=''.join(line)
print "\n\n"
print line.decode("utf-8")
g.close
		