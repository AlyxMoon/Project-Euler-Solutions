def is_abundant_num(num):
	def get_divisors():
		yield 1
		
		# Makes sure we only add square root once
		limit = int(num ** 0.5)
		if limit * limit == num:
			yield limit
		else:
			limit += 1
		
		for i in range(2, limit):
			if num % i == 0:
				yield i
				yield num / i

	return sum(get_divisors()) > num

	
# To note, this name sounds silly to me
def get_sum_of_non_abundant_sums(limit):
	abundantList = list(i for i in range(12, limit) if is_abundant_num(i))
	countList = list(range(limit))
	
	for x in abundantList:
		for y in abundantList:
			
			if x + y >= limit:
				break
			countList[x + y] = 0
	return sum(countList)
	
	
print(get_sum_of_non_abundant_sums(28123))