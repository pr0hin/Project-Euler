#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

def primenumber(n):
    lopn = []
    for each in range(1,n):
        if ( n%each == 0 ):
            lopn.append(each)

    print ( lopn )

primenumber ( 600851475143 )
