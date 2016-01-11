'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''


def main():
	orig_num = 13195 
	num = orig_num
	i = 2
	large = 0 
	while (num > 1 and i < num/2):
		debug(num, i, large)
		if( num % i == 0):
			num /= i
			if( is_prime( i ) ):
				if( i > large ):
					large = i
			if ( num == 1 ):
				break	
			i = 2
		i += 1
    
	j = orig_num / large
	print("j is now: {:f}".format(j))
	
	if( is_prime( int(j) ) and j > large):
		large = j

	print("Largest factor is {:d}".format(large))


def debug(num, i, large):
	print("Number is now: {:f}, i is now: {:f}, large is now {:f}".format(num, i, large))

def is_prime(x):
	''' Returns if number is a prime '''
	if x == 2 or x == 3:		
		print("{:d} is prime".format(x))
		return True
	if (x % 2 == 0) or ( x % 3 == 0):
		print("{:d} is prime".format(x))
		return True
	for i in range(5,x):
		if( x % i == 0 and x != i):
			print("{:d} is not prime".format(x))
			return False 
	print("{:d} is prime".format(x))
	return True 


if __name__ == '__main__':
	main()
