"""
Name: roshambo.py
Author: Ansonia McIntire
Created: 2/13/2024
Purpose: Rock Paper Scissors
"""
running_total = 0
still_running = "y"
computer_win = 0
player_win = 0

DASH = 124 * "-"
DASHE = 80 * "_"
DASHES = 16 * "-"

print(DASH) 

print("Hello and Welcome to an Elite Version of Rock, Paper, Scissors!!!")
print()

print("If you were wondring,'how do I play this?' I've got you covered.")
print()

print("Here are some things to know first before entering...")
print()

print("1. RULES and REGULATIONS: (That might be useful to know :)")
print()

print("\t - Remember to enjoy the game!!")
print()

print("2. There are instructions, so please read them.")
print()

print("\t - Enter a number 1, 2, or 3 into the prompt.")
print()

print("\t - Play the game ")

print(DASHE)



# Prompt user

try:

    while still_running == "y":
        
        from random import randint

        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        player = int(input("Enter Choice: "))
        computer = randint(1 , 3)
        
        print(DASHES)
        
        score = 0 
        running_total += score
    

        if player == 1: 
            player_choice = "rock"
            if computer == 1:
                computer_choice = "rock"
                print("Tie! Welp, try again")
                player_win += 1
                computer_win += 1
            
            elif computer == 2:
                computer_choice = "paper"
                print("Computer is the Winnner!!")
                computer_win += 1
                
            elif computer == 3:
                computer_choice = "Scissors"
                print("You have won!.X")
                player_win += 1

                

        elif player == 2:
            player_choice = "paper"
            if computer == 1:
                computer_choice = "rock"
                print("YOU WINNNNNN!!!")
                player_win += 1

            elif computer == 2:
                computer_choice = "paper"
                print("Sorry to inform you but there is a tie")
                player_win += 1
                computer_win += 1

            elif computer == 3:
                computer_choice = "Scissors"
                print("Paper was not a good choice")
                computer_win += 1

        elif player == 3:
            player_choice = "Scissors"
            if computer == 1:
                computer_choice = "rock"
                print("How unfortunate, You lost.")
                computer_win += 1

            elif computer == 2:
                computer_choice = "paper"
                print("Congratulations! You won!")
                player_win += 1

            elif computer == 3:
                computer_choice = "Scissors"
                print("hmm...it seems like there was a tie.")
                player_win += 1
                computer_win += 1
        
    
        print(f"Your choice: {player_choice} ... Computer Choice: {computer_choice}")
        
        print(f"Player: {player_win}\t Computer: {computer_win}")

        still_running = input("Enter 'y' to continue or 'any key to exit'")
    print("Done!")

    
    

    

except: 
    print("Oh no...please put a number 1-3.")


    # Player
    # Rock Rock 
    # Paper
    # Scissors
    # Tie
    # Computer wins because paper covers rock
    # Player wins because rock breaks scissors
    # Paper Rock
    # Paper
    # Scissors
    # Player wins because paper covers rock
    # Tie
    # Computer wins because scissors cut paper
    # Scissors Rock
    # Paper
    # Scissors
    # Computer wins because rock breaks scissors
    # Player wins because scissors cut paper
    # Tie
    # Import random module
    # Get how many rounds to play from human
    # Get 1, 2 or 3 from human (Rock, Paper, Scissors)
    # Generate random 1, 2 or 3 for computer turn (Rock, Paper, Scissors)
    # Use the decision matrix to develop the decision structure
