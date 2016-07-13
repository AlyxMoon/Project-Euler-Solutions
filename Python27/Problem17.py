import re

def num_to_english(num):
	
	stringOptions = {
		1: "one",
		2: "two",
		3: "three",
		4: "four",
		5: "five",
		6: "six",
		7: "seven",
		8: "eight",
		9: "nine",
		10: "ten",
		11: "eleven",
		12: "twelve",
		13: "thirteen",
		14: "fourteen",
		15: "fifteen",
		16: "sixteen",
		17: "seventeen",
		18: "eighteen",
		19: "nineteen",
		20: "twenty",
		30: "thirty",
		40: "forty",
		50: "fifty",
		60: "sixty",
		70: "seventy",
		80: "eighty",
		90: "ninety"
	}
	
	string = ""
	
	# Deal with the one and tens place
	tempNum = num % 100
	if tempNum > 0 and tempNum < 20:
		string += stringOptions[tempNum]
		
	elif tempNum >= 20 and tempNum < 100:
		if tempNum % 10 != 0:
			string += stringOptions[tempNum % 10]
		string = stringOptions[tempNum - (tempNum % 10)] + "-" + string
	
	# Deal with hundreds
	tempNum = num / 100 % 10
	if tempNum > 0:
		if num % 100 > 0:
			string = stringOptions[tempNum] + " hundred and " + string
		else:
			string = stringOptions[tempNum] + " hundred"
	
	# Deal with thousands
	tempNum = num / 1000 % 10
	if tempNum > 0:
		string = stringOptions[tempNum] + " thousand " + string
	
	return string
	
sum = 0
for i in range(1,1001):
	string = num_to_english(i)
	sum += len(re.findall(r'[a-zA-Z]',string))
	
print sum