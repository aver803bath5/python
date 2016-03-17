def isPrime(x):
	if x==2:
		return 1
	elif x==1:
		return 0
	for y in range(2,x):
		if(x%y==0):
			return 0
	return 1

x=input('Enter a number: ')
print "check:%d" %isPrime(x)

i=0
for z in range(2,1001):
	if isPrime(z)==1:
		i=i+z
		print z
print i
