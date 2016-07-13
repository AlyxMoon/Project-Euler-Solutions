pow = int(raw_input("Enter the power you'd like to go to: "))
num = 2 ** pow
print "Number:\n%i\n" % num

sum = 0
while num > 0:
	sum += num % 10
	num /= 10

print "Sum of digits: %i" % sum