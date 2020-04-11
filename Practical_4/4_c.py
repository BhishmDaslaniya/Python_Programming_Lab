'''
	Author : Bhishm Daslaniya [17CE023] 
    "Make it work, make it right, make it fast." 
                                                – Kent Beck  
'''
import random
def list_ends(a_list):
    return [a_list[0], a_list[len(a_list)-1]]

if __name__=='__main__':
	a = [random.randint(1, 50) for iter in range(10)]
	print("list a:"+str(a))
	b = list_ends(a)
	print("new list : "+str(b))