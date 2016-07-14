def getDayOfWeek(day, month, year):
	# Use Gauss' method to determine day of week
	'''
	month is shifted by 2 (January is 11, December is 10, ect)
	if month is January or February, year is shifted 1
	'''
	month = (month - 3) % 12 + 1
	if month > 10: year -= 1
	
	weekday = day % 7
	weekday += (2.6 * month - 0.2) % 7
	weekday += 5 * ((year % 100) % 4) % 7
	weekday += 4 * (year % 100) % 7
	weekday += 6 * (year % 400) % 7
	weekday += 3 * ((year % 100) % 7)
	weekday += 5 * (int(year / 100) % 4) % 7
	
	return int(weekday % 7)
	
# How many Sundays fell on first of the month
def getFirstSundaysInYearRange(yearStart, yearEnd):
	total = 0
	
	for year in range(yearStart, yearEnd + 1):
		for month in range(1, 13):
			if getDayOfWeek(1, month, year) == 0: total += 1
			
	return total
	
print(getFirstSundaysInYearRange(1901, 2000))
