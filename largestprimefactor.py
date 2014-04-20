#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

import math

def primefactors():
	lon = [2,3]
	for each in range(5,int(math.sqrt(600851475143)), 2):
		if each % 2 == 0 or each % 3 == 0:
			continue
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
	lof = []
	for num in lon:
		if 600851475143 % num == 0:
			lof.append(num)
	print (max(lof))





primefactors()
