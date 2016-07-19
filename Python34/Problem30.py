def isSumOfDigitPower(num, pow):
	
	sum = 0
	n = num
	while n > 0:
		sum += (n % 10) ** pow
		n = n // 10
	
	return sum == num 

def digitCount(num):

	count = 0
	while num > 0:
		count += 1
		num = num // 10
	return count
	
# Return a list containing all narcissistic numbers where the power is n
def getNarcissisticNums(n):
	
	nums = []
	upperBound = digitCount(9 ** n) * (9 ** n)
	
	for i in range(2, upperBound):
		if isSumOfDigitPower(i, n): nums.append(i)
		
	return nums
	
	
result = getNarcissisticNums(5)
print(result)
print(sum(result))