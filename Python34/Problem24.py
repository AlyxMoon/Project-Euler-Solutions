def get_nth_lexic_permutation(digits, goal):
	
	count = 1
	while(count < goal):
		end = len(digits)
		
		i = end - 1
		while(digits[i - 1] >= digits[i]): i -= 1
		
		j = end
		while(digits[j - 1] <= digits[i - 1]): j -= 1
		
		digits[i - 1], digits[j - 1] = digits[j - 1], digits[i - 1]
		
		i += 1
		j = end
		while(i < j):
			digits[i - 1], digits[j - 1] = digits[j - 1], digits[i - 1]
			i += 1
			j -= 1
			
		count += 1
		
	return int(''.join([ "%d" % x for x in digits]))
	
print(get_nth_lexic_permutation([0,1,2,3,4,5,6,7,8,9], 1000000))

# Finding the pattern...
# 0123456789	beginning
# 0123456798	SWAP last two
# 0123456879	SWAP last with third, SWAP last two
# 0123456897	SWAP last two
# 0123457689	SWAP last with fourth, SWAP last two, SWAP second to last two