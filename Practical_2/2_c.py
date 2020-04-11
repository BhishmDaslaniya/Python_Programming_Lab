'''
	Author : Bhishm Daslaniya [17CE023] 
    "Make it work, make it right, make it fast." 
                                                – Kent Beck  
'''
s = input("input string : ")
rev_s = "".join(reversed(s))
if s==rev_s:
	print("Palindrome")
else:
	print("Not Palindrome")