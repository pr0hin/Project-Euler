


def largestpalindrome(): 
	lomn = range(100,999)
	lonn = []
	for number in lomn[:]: 
		for each in lomn: 
			palindrome = number*each 
			lon = list(str(palindrome))
			loncopy = list(str(palindrome))	
			while (checkifnumberispalindrome(lon, loncopy)):	
				del lon[0]
				if len(lon) > 1:
					del lon[-1]
				if len(lon) == 0:
					lonn.append(palindrome)	
	print (max(lonn))
				


def checkifnumberispalindrome(lon, loncopy):
		for digit in lon:
			if digit == lon[0] and digit == lon[len(lon)-1]:
				return True		
			else:	
				return False	


	

largestpalindrome()
			
