
def sum_of_multiples(num):
	num3 = 0
	num5 = 0

	multiple_3 = range(0, num, 3)
	multiple_5 = range(0, num, 5)
	for i in multiple_5:
		num5 = num5 + i
		if i in multiple_3:
			multiple_3.remove(i)
		

	for each in multiple_3:
		num3 = num3 + each

	total = num5 + num3	
	print ( multiple_3)
	print ( multiple_5 ) 
	print ( num3 ) 
	print ( num5 )
	print ( total )
	return

sum_of_multiples(1000)
