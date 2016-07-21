class Prime:
	def __init__(self):
		self.primes = [2]
	
	def buildPrimes(self, limit):
		
		for i in range(1, limit + 1, 2):
			if self.isPrime(i): self.primes.append(i)
	
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

# Takes array of numbers, and returns true if all are permutations of each other
def isPermutation(nums):
	
	if len(nums) == 0: return False
	if len(nums) == 1: return True
	
	def getDigitCounts(num):
		digits = {
			0: 0,
			1: 0,
			2: 0,
			3: 0,
			4: 0,
			5: 0,
			6: 0,
			7: 0,
			8: 0,
			9: 0,	
		}
		while num > 0:
			digits[num % 10] += 1
			num = num // 10
			
		return digits
	
	digitCount = getDigitCounts(nums[0])
	
	for num in nums:
		if digitCount != getDigitCounts(num): return False
	
	return True
	

# Where n is the number of digits in each number
def getPrimePermutations(n):
	primes = Prime()
	primes.buildPrimes(10 ** n)
	primeList = [x for x in primes.primes if x >= 10 ** (n - 1)]
	
	permutations = []
	
	limit = len(primeList)
	for i in range(0, limit - 1):
		for j in range(i + 1, limit): 
			change = primeList[j] - primeList[i]
			if (primeList[j] + change) in primeList:
				potentialPermutation = [primeList[i], primeList[j], primeList[j] + change]
				if isPermutation(potentialPermutation): permutations.append(potentialPermutation)
	
	return permutations
	

print(getPrimePermutations(4))