


def sumofsquares():
	los = []	
	lon = range (1, 101)
	for each in lon:
		los.append(each*each)
	sumofsquares = sum(los)

	total =	sum(lon)	
	squareofsum = total*total

	difference = squareofsum - sumofsquares
	print (difference)


sumofsquares()

		
