# Rock Paper Scissor Game🔥

- In the rock, paper and scissors game our goal is to create a command-line game where a user has the option to choose between rock, paper and scissors and if the user wins the score is added, and at the end when the user finishes the game, the score is shown to the user.

## 📌Rock, Paper and Scissors Game with Python

- To create the Rock, Paper and Scissors game with Python, we need to take the user’s choice and then we need to compare it with the computer choice which is taken using the random module in Python from a list of choices, and if the user wins then the score will increase by 1:

### Code:

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
            
            
### Output:

    Enter your choice rock
    Its tie now...
    Enter your choice paper
    You won... Paper covers Rock
    Enter your choice scissors
    You lose... Rock smashes Scissors
    Enter your choice end
    The final scores are 
    CPU Score 1
    Player Score 1

## 📌Summary

- Creating these types of games will help a beginner to think logically. You can even use this idea to make your own game. In the end, creating these types of programs will help you create your algorithms, which is a very important skill for coding interviews and competitive programming.
