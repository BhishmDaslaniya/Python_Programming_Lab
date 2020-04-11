'''
	Author : Bhishm Daslaniya [17CE023] 
    "Make it work, make it right, make it fast." 
                                                – Kent Beck  
'''
number = int(input("Enter number:"))
if number%2==0:
	print("Even")
	if number%4 == 0:
		print("Number is multiple of 4")
else:
	print("Odd")