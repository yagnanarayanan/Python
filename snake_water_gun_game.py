"""
Snake water gun game
Snake vs. Water: Snake drinks the water hence wins.
Water vs. Gun: The gun will drown in water, hence a point for water
Gun vs. Snake: Gun will kill the snake and win.
In situations where both players choose the same object, the result will be a draw.

You have to use a random choice function to select between, snake, water, and gun.
You do not have to use a print statement in case of the above function.
Then you have to give input from your side.
After getting ten consecutive inputs, the computer will show the result based on each iteration.
"""
import random
comp_score = 0
user_score = 0
game_list = ["snake", "water", "gun"]
for i in range(1, 11, 1):
    comp_choice = random.choice(game_list)
    user_choice = input("Please enter snake, water or gun as your choice")
    if user_choice == comp_choice:
        print(f"Computer choice: {comp_choice}")
        comp_score += 1
        user_score += 1
    elif user_choice == "snake" and comp_choice == "water":
        print(f"Computer choice: {comp_choice}")
        user_score += 1
    elif user_choice == "water" and comp_choice == "snake":
        print(f"Computer choice: {comp_choice}")
        comp_score += 1
    elif user_choice == "water" and comp_choice == "gun":
        print(f"Computer choice: {comp_choice}")
        user_score += 1
    elif user_choice == "gun" and comp_choice == "water":
        print(f"Computer choice: {comp_choice}")
        comp_score += 1
    elif user_choice == "gun" and comp_choice == "snake":
        print(f"Computer choice: {comp_choice}")
        user_score += 1
    elif user_choice == "snake" and comp_choice == "gun":
        print(f"Computer choice: {comp_choice}")
        comp_score += 1
    print(f"User score : {user_score} and computer score : {comp_score}")

if user_score > comp_score:
    print("User Wins!")
elif user_score < comp_score:
    print("Computer Wins!")
else:
    print("Both user and computer score is equal. Its a draw.")
print("Game Over!. Have a nice day!")
