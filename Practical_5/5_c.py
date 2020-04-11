'''
	Author : Bhishm Daslaniya [17CE023] 
    "Make it work, make it right, make it fast." 
                                                – Kent Beck  
'''
def reverseWord(w):
	return ' '.join(w.split()[::-1])

if __name__=='__main__':
	s = input("Enter sentence:")
	print(reverseWord(s))