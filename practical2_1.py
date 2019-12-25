n = int(input("Enter number: "))

print("Factors of "+ str(n) )
for _ in range(1,n):
	if(n % _ == 0):
		print( _ ,end=" ")