
'''
Gauss' Method
R(1+5R(A-1,4)+4R(A-1,100)+6R(A-1,400),7)

Let A − 1 = year = Y, m = month − 2 mod 12 (March = 1,..., January = −1 mod 12 = 11 and February = 12) and d = days of the month, this formula becomes
{\displaystyle w=d+\lfloor 2.6m-0.2\rfloor +5R(Y,4)+4R(Y,100)+6R(Y,400){\bmod {7}}.} w=d+\lfloor 2.6m-0.2\rfloor +5R(Y,4)+4R(Y,100)+6R(Y,400){\bmod {7}}.

Let A − 1 = year = y + 100c, this formula becomes
{\displaystyle w=d+\lfloor 2.6m-0.2\rfloor +5R(y,4)+3R(y,7)+5R(c,4){\bmod {7}}.} w=d+\lfloor 2.6m-0.2\rfloor +5R(y,4)+3R(y,7)+5R(c,4){\bmod {7}}.

d = 1
[2.6 × 11 − 0.2] = 28 mod 7 = 0
5R(99,4) = 5 × 3 = 15 mod 7 = 1
4R(1999,100) = 4 × 99 mod 7 = 4 × 1 = 4
6R(1999,400) = 6 × 399 mod 7 = 6 × 0 = 0
3R(99,7) = 3 × 1 = 3
5R(19,4) = 5 × 3 mod 7 = 1
w = 1 + 0 + 1 + 4 + 0 = 1 + 0 + 1 + 3 + 1 = 6 = Saturday.

'''

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
#print(getDayOfWeek(31,12,2000))
