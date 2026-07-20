import random
user = input("Select Rock, Paper or Scissors: ")

choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)

print("User chose: ", user)
print("Computer chose: ", computer)

if user == computer:
    print("It is a draw")

elif (user == "Rock" and computer == "Scissors") or\
    (user == "Paper" and computer == "Rock") or\
    (user == "Scissors" and computer == "Paper"):
    print("You win")
else:
    print("You lose")