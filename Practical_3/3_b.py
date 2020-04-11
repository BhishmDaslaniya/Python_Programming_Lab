'''
	Author : Bhishm Daslaniya [17CE023] 
    "Make it work, make it right, make it fast." 
                                                – Kent Beck  
'''
def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

if __name__=='__main__':
	user1 = input("What's your name?")
	user2 = input("And your name?")
	user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
	user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)
	print(compare(user1_answer, user2_answer))