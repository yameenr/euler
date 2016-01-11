'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''

large = 0
orig_num = 600851475143


def main():
	num = orig_num
	factorize(num)

def factorize(num):
	i = 2
	global large
	while (num > 1 and i < num / 2):
		#debug(int(num), int(i), int(large))
		if( num % i == 0):
			num /= i
			if( is_prime( i ) ):
				if( i > large ):
					large = i
			if ( num == 1 ):
				break	
			i = 2
		i += 1
	large = int(num)
	print("Largest prime factor of {:d} is {:d}".format(orig_num, large))

def debug(num, i, large):
	print("Number is now: {:d}, i is now: {:d}, large is now {:d}".format(num, i, large))

def is_prime(x):
	''' Returns if number is a prime '''
	if x == 2 or x == 3:		
		return True
	if (x % 2 == 0) or ( x % 3 == 0):
		return True
	for i in range(5,x):
		if( x % i == 0 and x != i):
			return False 
	return True 


if __name__ == '__main__':
	main()
