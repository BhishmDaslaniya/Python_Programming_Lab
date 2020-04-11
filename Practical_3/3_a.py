'''
	Author : Bhishm Daslaniya [17CE023] 
    "Make it work, make it right, make it fast." 
                                                – Kent Beck  
'''
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("List a:" + str(a))
even = [_ for _ in a if _%2==0]
print("List of even numbers:" + str(even)) 
