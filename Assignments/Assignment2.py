import math

x,y,p,q = map(int, input().split())

b1 = y*p
b2 = q*x
b3 = x*y

common_factor = math.gcd(b1,math.gcd(b2,b3))

print(int(b1/common_factor),int(b2/common_factor),int(b3/common_factor))