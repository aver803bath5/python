# -*- coding: utf-8 -*-
class Hanwei:
	# -*- coding: utf-8 -*-
	quote= u"我一點都不會介意"
	number1=""
	number2=""
	def expert1(self):
		print u"C語言",
	def expert2(self):
		print u"電腦網路"
class Chinerei(Hanwei):
	interest="python"
	h=Hanwei
a=Hanwei()
b=Chinerei()
print u"教授的專長是",
a.expert1()
print ""
print u"教授的專長是",
a.expert2()
print u"學生的專長為",;b.expert1();b.expert2()
print u"學生的興趣為"+b.interest
print a.quote
print b.quote


