s = input("input string : ")
rev_s = "".join(reversed(s))
if s==rev_s:
	print("Palindrome")
else:
	print("Not Palindrome")