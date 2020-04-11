'''
	Author : Bhishm Daslaniya [17CE023] 
    "Make it work, make it right, make it fast." 
                                                – Kent Beck
    !!!! Graph implemetation in python tedius task!!!! Not possible for me!!
    Problem solution status : Not completd!!!!  
'''


import math

mod = 1000000007
v = []
for i in range(100005):
	v.append([])

par = [-1] * 100005
dis = [0] *100005
low = [None] *100005
num = 0
total = 0
ev =0
global n 
si = [None] * 100005
vi = [False] * 100005
tit = 0
def numberofnodes(s,e):
	si[s] = 1
	vi[s] = True
	for u in v[s]:
		if(vi[u]):
			continue
		numberofnodes(u,s)
		si[s] = si[s] + si[u]


def dfs(so):
	global tit,num
	vi[so] = True
	dis[so] = low[so] = tit + 1
# 	dis[so] = tit
# 	low[so] = tit
# 	tit +=1
	num +=1
	for u in v[so]:
		if(not vi[u]):
			par[u] = so
			dfs(u)
			low[so] = min(low[so],low[u])
			if(low[u] > dis[so]):
				bi = so
				bo = u
				if(si[u] != 0 and (n-si[u])!=0 ):
					total+=1
				if(si[u]%2 == 0  and (n-si[u])%2==0):
					ev+=1
		elif(u != par[so]):
		  #  print(low[so],dis[u])
			low[so] = min(low[so],dis[u])

def modInverse(a, m):
	m0 = m
	y = 0 
	x = 1 
	if (m == 1):
		return 0
	while (a > 1): 
		q = a / m
		t = m 
		m = a % m
		a = t 
		t = y 
		y = x - q * y 
		x = t
	if (x < 0): 
		x += m0 
	return x 

if __name__ == '__main__':
    n,m = map(int,input().split())
    for i in range(m):
    	a,b =  map(int,input().split())
    	v[a].append(b)
    	v[b].append(a)

    numberofnodes(1,0)
    dfs(1)
    q = modInverse(total,mod)
    p1 = (ev%mod * q)%mod
    p2 = (1 - p1 + mod)%mod
    if total==0:
    	print(0,0)
    else:
    	print(p1,p2)