# number guesser
import random
top_of_range = input("Enter top of range number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please enter a number greater than 0 next time")
        quit()
else:
    print("Please enter a number next time")
    quit()
a = random.randint(1, top_of_range)
no_of_guesses = 0
while True:
    guess = input(f"Guess a number between 1 and {top_of_range -1}: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please enter a number")
        continue
    if a == guess:
        print("You guessed correct!")
        no_of_guesses += 1
        print(f"Total number of valid guesses made: {no_of_guesses}")
        break
    elif a < guess:
        print("Guess a smaller number.")
        no_of_guesses += 1
    else:
        print("Guess a larger number")
        no_of_guesses += 1
print(f"Yes the number to be guessed was {a}")
