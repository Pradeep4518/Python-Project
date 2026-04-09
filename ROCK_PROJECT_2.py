import random
choices = ["rock","paper","scissor"]
print("--------- Rock --- Paper --- Scissor --- Game ---------")
while True:
    user = input("Enter Rock or Paper or Scissor :").lower()
    computer = random.choice(choices)
    print("Computer chose:",computer)
    if user == computer:
        print("It is a tie!")
    elif (user == "rock" and computer == "scissor") or (user == "scissor" and computer == "paper") or (user == "paper" and computer == "rock"):
        print("YOU WIN!")
    elif user in choices:
        print("YOU LOSE!")
    else:
        print("Invalid input!")
    play = input("Play again? (yes/no) :").lower()
    if play != "yes":
        print("Thanks for Playing!")
        break
