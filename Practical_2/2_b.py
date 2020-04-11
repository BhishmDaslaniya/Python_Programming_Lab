'''
	Author : Bhishm Daslaniya [17CE023] 
    "Make it work, make it right, make it fast." 
                                                – Kent Beck  
'''
import random
a = [random.randint(1, 50) for iter in range(10)]
b = [random.randint(1, 50) for iter in range(15)]
print("list a :" + str(a))
print("list b :" + str(b))
c = [common_value for common_value in set(a) if common_value in set(b)]
print("Common values :" + str(c))