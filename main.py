import random

computer_win = 0
user_win = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Invalid input. Please type Rock, Paper, or Scissors.")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == computer_pick:
        print("It's a tie!")

    elif (
           (user_input == "rock" and computer_pick == "scissors")
        or (user_input == "paper" and computer_pick == "rock")
        or (user_input == "scissors" and computer_pick == "paper")
    ):
        print("You won!")
        user_win += 1

    else:
        computer_win += 1
        print("Computer won!")

print("You won", user_win, "times.")
print("The computer won", computer_win, "times.")
print("Goodbye!")