'''
      Author : Bhishm Daslaniya [17CE023] 
    "Make it work, make it right, make it fast." 
                                                – Kent Beck  
'''
import string
import random 

def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
      return ''.join(random.choice(chars) for _ in range(size))

if __name__=='__main__':
      print(pw_gen(int(input('How many characters in your password?: '))))
