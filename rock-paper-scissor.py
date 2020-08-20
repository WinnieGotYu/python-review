from random import randint

print("...ROCK...")
print("...PAPER...")
print("...SCISSORS...")

player = input("Type 'rock', 'paper' or 'scissors': ").lower()
choices = ["rock", "paper", "scissors"]
computer = choices[randint(0, 2)]

print(f"Computer plays: {computer}")

if player == computer:
    print("It's a tie")
elif player == 'rock':
    if computer == 'scissors':
        print("Player wins!")
    else:
        print("Computer wins!")
elif player == 'paper':
    if computer == 'scissors':
        print("Computer wins!")
    else:
        print("Player wins!")
elif player == 'scissors':
    if computer == 'paper': 
        print("Player wins!")
    else:
        print("Computer wins!")
else:
    print("Something went wrong")
