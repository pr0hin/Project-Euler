


def smallestmultiple():
	lon = []
	for each in range(20, 1000000000, 20):
		for num in range(1, 21):
			if each%num > 0:
				print(each)
				break
			if each%num == 0 and num == 20:
				lon.append(each)
				break
		if len(lon) > 0:
			break
	print(lon[0])

smallestmultiple()
					
