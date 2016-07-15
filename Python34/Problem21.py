def get_sum_divisors(num):
	
	def get_divisors(num):
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
				yield int(num / i)
				
	return sum(get_divisors(num))

	
def get_amicable_nums(limit):
	nums = {}
	for i in range(2, limit):
		nums[i] = get_sum_divisors(i)
		
	for key in list(nums.keys()):
		value = nums[key]
		# Delete immediately if a perfect number
		if key == value: del nums[key]
		
		# Check for pair
		# Only delete current item if not a pair, will check other item later
		elif not value in nums: del nums[key]
		elif key != nums[value]: del nums[key]
		
	return nums.keys()

	
print(sum(get_amicable_nums(10000)))