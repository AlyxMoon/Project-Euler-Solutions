import math
import fractions

def getGreatestRecurringCycle(limit):
	
	def getRecurringCycle(n):
		exp = 1
		while True:
			if (10 ** exp) % n != 1:
				exp += 1
			else:
				break
		return exp
	
	max = { 
		"denominator" : 0,
		"cycle" : 0
	}
	
	for i in range(2, limit):
		if fractions.gcd(10, i) == 1:
			temp = getRecurringCycle(i)
			if temp > max["cycle"]:
				max["denominator"] = i
				max["cycle"] = temp

	return max
	
answer = getGreatestRecurringCycle(1000)
print("The denominator %s has the greatest cycle length of %i" % (answer["denominator"], answer["cycle"]))
