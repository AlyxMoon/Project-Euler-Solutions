def getDistinctTerms(a, b):
	terms = set()

	for i in range(2, a + 1):
		for j in range(2, b + 1):
			terms.add(i ** j)
			
	return terms

print(len(getDistinctTerms(100, 100)))