from math import sqrt

def getDivisorCount(num):
	if num in (0,1): count = 1
	elif num in (2,3): count = 2
	else:
		count, i = 2, 2
		bound = sqrt(num)
		if sqrt(num).is_integer(): count += 1
		while i <  bound:
			if num % i == 0: count += 2
			i += 1
	return count

num, i = 0, 0
goal = int(raw_input("How many divisors will you count to?\n> "))
while True:
	i += 1
	num += i
	count = getDivisorCount(num)
	if count > goal:
		print "First number with at least %i divisors: %i" % (goal, num)
		break