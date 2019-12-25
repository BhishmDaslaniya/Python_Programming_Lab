def CheckEvenOdd(number):
	if number%2==0:
		print(str(number) + " : Even")
	else:
		print(str(number) + ": Odd")

def findFactors(n):
	print("Factors of "+ str(n) + " is : ")
	for i in range(1,n):
		if n%i==0:
			print(i)

n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))

CheckEvenOdd(n1)
CheckEvenOdd(n2)

if n1%n2==0:
	print(str(n1)  + " is divisible by "+ str(n2))
if n2%n1==0:
	print(str(n2)  + " is divisible by "+str(n1))

findFactors(n1)
findFactors(n2)