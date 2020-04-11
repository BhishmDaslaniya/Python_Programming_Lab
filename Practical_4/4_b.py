'''
	Author : Bhishm Daslaniya [17CE023] 
    "Make it work, make it right, make it fast." 
                                                – Kent Beck  
'''
def is_prime(n):
	if num > 1:
		if len(a) == 0:
			print('prime')
		else:
			print('NOT prime')
	else:
		print('NOT prime')

if __name__=='__main__':
	num = int(input('Input a number: '))
	a = [x for x in range(2, num) if num % x == 0]
	is_prime(num)