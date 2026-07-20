import random 
user = input("Select Snake, Water or Gun: ")
choices = ["Snake", "Water", "Gun"]

computer = random.choice(choices)

print("User chose:", user)
print("Computer chose:", computer)

if user == computer:
    print("It is a draw")

elif(user == "Snake" and computer == "Water") or\
    (user == "Water" and computer == "Gun") or\
    (user == "Gun" and computer == "Snake"):
    print("You win")

else:
    print("You lose:")

