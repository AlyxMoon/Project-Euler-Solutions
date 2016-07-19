def sumSelfPowers(n):
	
	sum = 0
	for i in range(1, n + 1):
		sum += i ** i
	return sum
	
result = sumSelfPowers(1000)
print("Result: %i" % result)