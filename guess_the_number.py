# The number of guesses should be limited, i.e (5 or 9).
# Print the number of guesses left.
# Print the number of guesses he took to win the game.
# “Game Over” message should display if the number of guesses becomes equal to 0.
guesses = 5
prize = 12
while guesses > 0:
    num = int(input("enter a number between 1 and 100 : "))
    if num == prize:
        guesses -= 1
        print("Congrats, you guessed right in ", str(5-guesses), "guesses")
        break
    elif num >=50 and num <= 100:
        guesses -= 1
        print("please guess lesser than this. Guesses left: ", str(guesses))
        continue
    elif num >= 15 and num < 50:
        guesses -= 1
        print("please guess lesser than this. You are closer. Guesses left: ", str(guesses))
        continue
    elif num <=10 and num > 0:
        guesses -= 1
        print("please guess greater than this. Guesses left: ", str(guesses))
        continue
    elif num > 10 and num < 15 and num != 12:
        guesses -= 1
        print("you are close.  Guesses left: ", str(guesses))
        continue
print("Game Over")
