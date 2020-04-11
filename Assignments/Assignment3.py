'''
	Author : Bhishm Daslaniya [17CE023] 
    "Make it work, make it right, make it fast." 
                                                – Kent Beck  
'''

t = int(input())

for _ in range(t):
	n = int(input())
	a = list(map(int,input().split()))
	a.sort()
	ans = int(1e9)
	for i in range(1,n):
		ans = min(ans,(a[i-1]^a[i]))
	print(ans)
