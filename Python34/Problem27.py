# Keeps an internal array of prime numbers, generated as necessary
class Prime:
	def __init__(self):
		self.primes = [2,3]
	
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

primes = Prime()
maxCoefficient = {
	"a" : 0,
	"b" : 0,
	"count" : 0,
}

for b in range(-999, 1000, 2):
	
	# b must be prime for when n = 0
	if primes.isPrime(b):
		
		# a must be odd, for when n = 1
		for a in range(-999, 1000, 2):
			
			n = 0
			while True:
				
				result = (n ** 2) + (a * n) + b
				if primes.isPrime(result):
					n += 1
				else: break
			
			if n > maxCoefficient["count"]:
				maxCoefficient["count"] = n
				maxCoefficient["a"] = a
				maxCoefficient["b"] = b
				
print(maxCoefficient)
print("Product of coefficients: %i" % (maxCoefficient["a"] * maxCoefficient["b"]))