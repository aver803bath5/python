# -*- coding: utf-8 -*-
import re
code=""
bingo="E-056790"
while not re.findall(r"^[A-Z]-\d{6}",code):
	code=raw_input("Please enter your code(^[A-Z]-\d{6}):")

if bingo in code:
	print u"恭喜您中了10萬元"
# print re.findall(r"[A-Z]-.56790",code)
elif code in re.findall(r"[A-Z]-.56790",code):
	print u"恭喜您中了2萬元"

elif code in re.findall(r".-...790",code):
	print u"恭喜您中了100元購物禮券"
else:
	print u"銘謝惠顧"