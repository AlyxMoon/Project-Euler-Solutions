def getDigitCount(num):

	count = 0
	if num == 0: count += 1
	
	while num > 0:
		num = num // 10
		count += 1
	
	return count

def findFib(n):

	count, currNum, prevNum = 1, 1, 1
	while(getDigitCount(currNum) < n):
		count += 1


		currNum += prevNum;
		prevNum = currNum - prevNum;

	count += 1
	
	return count
	
print(findFib(1000))