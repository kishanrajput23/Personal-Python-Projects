import random

randNo = random.randint(1,3)
if randNo == 1:
    computer_choose = "r"   # if randNo is equal to 1 then it will store 'r' as computer choice
if randNo == 2:
    computer_choose = "p"   # if randNo is equal to 2 then it will store 'p' as computer choice
if randNo == 3:
    computer_choose = "s"   # if randNo is equal to 3 then it will store 's' as computer choice

# Defining gameWin function for performing major task for this game.

def gameWin(computer_choose, user_input):
    if computer_choose == user_input:
        return None
    elif computer_choose == "r":
        if user_input == "p":
            return True
        elif user_input == "s":
            return False
    
    elif computer_choose == "p":
        if user_input == "r":
            return False
        elif user_input == "s":
            return True
    
    elif computer_choose == "s":
        if user_input == "r":
            return True
        elif user_input == "p":
            return False

print("Computer Choosed already from Rock('r') or Paper('p') or Scissor('s')")

print("Now your turn to choose")

user_input = input("Choose from Rock('r') or Paper('p') or Scissor('s') ")  #taking input from the user

# It shows the user what computer choose from rock, paper or scissor.
print("Computer choosed " + computer_choose)    

# It shows the user what he/she choose from rock, paper or scissor.
print("You Choosed " + user_input)  


# This block of if-else statement will find out conditon of gameWin function

if gameWin(computer_choose, user_input) == None: 
    print("It tie now")

elif gameWin(computer_choose, user_input):
    print("Congratulations You Won!!!") 

else:
    print("You Lose!")
  