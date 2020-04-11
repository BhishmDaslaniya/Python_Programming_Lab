'''
	Author : Bhishm Daslaniya [17CE023] 
    "Make it work, make it right, make it fast." 
                                                – Kent Beck  
'''
number,check = map(int,input("Enter two numbers:").split())
if number%check==0:
	print(str(number) + " is divided by "+ str(check))
else:
	print(str(number) + " is not divided by "+ str(check))