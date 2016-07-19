class Prime:
	def __init__(self):
		self.primes = [2,3,5,7]
	
	def isPrime(self, n):
		if n in [0,1]: return False
		if n == 2: return True
	
		# Immediately leave if already in the prime list
		if n in self.primes: return True
	
		# Negative numbers are hard, make them not negative
		if n < 0: 
			isNegative = True
			n = -n
		else: isNegative = False
		
		# The core of it, check if it's divisible by primes already found
		for i in self.primes:
			if n % i == 0: return False
			
		# Adds to the prime list as necessary to fully check given number
		j = self.primes[-1] + 2
		while j <= (n ** 0.5):
			if self.isPrime(j):
				self.primes.append(j)
				
			if n % j == 0: return False
			j += 2
		
		return True

def digitCount(num):

	count = 0
	while num > 0:
		count += 1
		num = num // 10
	return count
		
def getTruncatablePrimes():

	primes = Prime()
	truncatablePrimes = []
	
	# Apparently there are 11 truncatable primes, let's go with it
	goal = 11
	
	i = 11
	while len(truncatablePrimes) < goal:
		
		if primes.isPrime(i):
			truncatable = True
			digits = digitCount(i)
			
			num = i
			# right to left truncation
			for d in range(1, digits):
				num = num // 10
				if not primes.isPrime(num):
					truncatable = False
					break
			
			# left to right truncation
			if truncatable:
				num = i
				for d in range(1, digits):
					num = num % (10 ** (digitCount(num) - 1))
					
					if not primes.isPrime(num):
						truncatable = False
						break
			
			if truncatable:
				truncatablePrimes.append(i)
		
		i += 2
	
	return truncatablePrimes

result = getTruncatablePrimes()
print("Truncatable Primes: %s" % result)
print("Sum: %i" % sum(result))