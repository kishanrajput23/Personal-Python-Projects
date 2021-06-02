import random

choices = ["Rock", "Paper", "Scissor"]

player = False
cpu_score = 0
player_score = 0

while True:
    player = input("Enter your choice ").capitalize()

    computer = random.choice(choices)

    if computer == player:
        print("Its tie now...")

    elif player == "Rock":
        if computer == "Paper":
            print("You lose...", computer, "covers", player)
            cpu_score += 1

        else:
            print("You won...", player, "smashes", computer)
            player_score += 1

    elif player == "Paper":
        if computer == "Rock":
            print("You won...", player, "covers", computer)
            player_score += 1
        
        else:
            print("You lose...", computer, "cut", player)
            cpu_score += 1

    elif player == "Scissor":
        if computer == "Paper":
            print("You won...", player, "cut", computer)
            player_score += 1

        else:
            print("You lose...", computer, "smashes", player)
            cpu_score += 1

    elif player == "End":
        print("The final scores are ")
        print(f"CPU Score {cpu_score}")
        print(f"Player Score {player_score}")
        break