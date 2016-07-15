def get_sum_string_code(string):
	sum = 0

	for char in string:
		sum += ord(char) - 64

	return sum

def get_names_score(filename):
	file = open(filename)

	names = sorted(file.read().split(","))
	sum = 0
	count = 0
	
	for name in names:
		count += 1
		sum += get_sum_string_code(name[1:-1]) * count
		
	file.close()
	return sum


print(get_names_score("Problem22_names.txt"))