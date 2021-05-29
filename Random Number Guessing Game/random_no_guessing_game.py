import random

num = random.randint(1, 100)

user_input = 0

count = 0

while user_input != num:
    user_input = int(input("Enter your guess "))

    if user_input < num:
        print("Your number is less")
        print("Try Again")

    elif user_input > num:
        print("Your number is much")
        print("Try Again")
    
    else:
        print("Congratulations you guessed the right number")

    count += 1

print("Kudos to you!!")
print("You took", str(count), "trials for guessing the correct number")