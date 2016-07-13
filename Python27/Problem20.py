from math import factorial
from math import floor

n = int(raw_input("Enter the factorial number to calculate: "))
num = factorial(n)

sum = 0
while num > 0:
	sum = sum + (num % 10)
	num = num // 10
	
print "Sum of digits: %i" % sum 
