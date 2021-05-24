import random

user = input("Do you want to roll the dice ")

while user == "y":

    k = random.randint(1,6)
    
    if k == 1:
        print(" --------- ")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print(" --------- ")
    
    if k == 2:
        print(" --------- ")
        print("|       0 |")
        print("|         |")
        print("| 0       |")
        print(" --------- ")

    if k == 3:
        print(" --------- ")
        print("|       0 |")
        print("|    0    |")
        print("| 0       |")
        print(" --------- ")

    if k == 4:
        print(" --------- ")
        print("| 0     0 |")
        print("|         |")
        print("| 0     0 |")
        print(" --------- ")

    if k == 5:
        print(" --------- ")
        print("| 0     0 |")
        print("|    0    |")
        print("| 0     0 |")
        print(" --------- ")

    if k == 6:
        print(" ---------- ")
        print("| 0      0 |")
        print("| 0      0 |")
        print("| 0      0 |")
        print(" ---------- ")

    user = input("Do you want to roll again the dice ")
