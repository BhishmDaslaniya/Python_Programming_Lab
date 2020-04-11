'''
	Author : Bhishm Daslaniya [17CE023] 
    "Make it work, make it right, make it fast." 
                                                – Kent Beck  
'''
import random
n = random.randint(1, 9)
number=0
guess = input("Enter an integer from 1 to 9 or exit: ")
while n != "guess":
    if guess == "exit":
        print("count:"+str(number))
        break
    elif int(guess) < n:
        number += 1
        print ("guess is low")
        guess = input("Enter an integer from 1 to 9 or exit: ")
    elif int(guess) > n:
        number += 1
        print ("guess is high")
        guess = input("Enter an integer from 1 to 9 or exit: ")
    else:
        number += 1
        print ("Congrats you guess it in " + str(number) + " Steps.")
        break
