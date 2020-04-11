'''
	Author : Bhishm Daslaniya [17CE023] 
    "Make it work, make it right, make it fast." 
                                                – Kent Beck  
'''
a = [0,0,1,1,1,2,3,5,6,7,13,15,24,43,57,65,87]

n = int(input("Enter number:"))
ans = [_ for _ in a if _ < n]
print(ans)