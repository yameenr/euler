'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def main():
	''' Iterates downward from largest 3 digit number products until first palindrome is hit'''
	large = 0
	beg = 100
	end = 999 

	while large == 0:
		for i in range( end,beg, -1 ):
			for j in range( end,beg, -1):
				prod = i * j
				if is_palindrome(prod):
					if prod > large:
						large = prod
					break

	print('largest palindrome product is:{:d}'.format(large) )


def is_palindrome(num):
	''' returns True if palindrome '''
	num_str = str(num)
	length = len(num_str) 
	iterations = length / 2 if length % 2 == 0 else length / 2 + 1

	for i in range(int(iterations)):
		c1 = num_str[ i: i+1 ] 
		c2 = num_str[ length-i -1 : length-i ]

		#debug( length, i, c1, c2) 
		if c1 != c2:
			return False
	
	return True

def debug(length, i, c1, c2):
	print('Length is {:d}, i is now: {:d}, {:s} compared to {:s}'.format(length, i, c1,c2))

if __name__ == '__main__':
	main()
