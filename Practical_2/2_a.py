	'''
	Author : Bhishm Daslaniya [17CE023] 
    "Make it work, make it right, make it fast." 
                                                – Kent Beck  
'''
n = int(input("Enter number: "))

print("Factors of "+ str(n) )
for _ in range(1,n):
	if(n % _ == 0):
		print( _ ,end=" ")