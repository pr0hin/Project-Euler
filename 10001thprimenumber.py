import math 

def primenumber():
	lon = [2,3]
	for each in range(5,10000000000, 2):
		if each % 2 == 0 or each % 3 == 0:
			continue
		if len(lon) ==  10001:
			break
		maxdiv = int(math.sqrt(each))
		k = 1
		acc = 0
		while (6*k + 1 <= maxdiv or 6*k -1 <= maxdiv):
			div = 6*k + 1
			div2 = 6*k -1
			if each % div == 0 or each% div2 == 0 or each % maxdiv == 0:
				acc = acc + 1
				break
			k = k + 1
		if acc ==  0:
			lon.append(each)
	print (lon[len(lon)-1])
	print (len(lon))
primenumber()
