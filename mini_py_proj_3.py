# rock paper scissors game
# scissors beats paper,
# paper beats rock and
# rock beats scissors
# scores will display after pressing q
import random
options = ['rock', 'paper', 'scissors']
user_wins = 0
comp_wins = 0
while True:
    user_choice = input("Please choose rock or paper or scissors")
    if user_choice.lower() == 'q':
        print(f"User wins: {user_wins} Computer wins: {comp_wins}")
        quit()
    elif user_choice not in options:
        print("Please try again. Only choose rock or paper or scissors: ")
        continue
    r = random.randint(0, 2)
    comp_choice = options[r]
    print(f"Computer chose {comp_choice}")
    if comp_choice == 'scissors' and user_choice == 'paper':
        comp_wins += 1
        print("Computer wins")
    elif user_choice == 'scissors' and comp_choice == 'paper':
        user_wins += 1
        print("User wins")
    elif comp_choice == 'paper' and user_choice == 'rock':
        comp_wins += 1
        print("Computer wins")
    elif user_choice == 'paper' and comp_choice == 'rock':
        user_wins += 1
        print("User wins")
    elif comp_choice == 'rock' and user_choice == 'scissors':
        comp_wins += 1
        print("Computer wins")
    elif user_choice == 'rock' and comp_choice == 'scissors':
        user_wins += 1
        print("User wins")
    else:
        print("Draw. Both get a point each.")
        comp_wins += 1
        user_wins += 1
        continue
