# two players take turns to roll a die. Each player can roll the die any number of times till they wish or roll a 1
# If a player rolls a 1, then the particular players score becomes 0 for that turn
# Game is played till either player gets a score of 20
import random
# print(rand_dice_num)
player_1_score = 0
player_2_score = 0


def dice_gen():
    rand_dice_num = random.randint(1, 6)
    return rand_dice_num


# keep playing till either player gets to total score of 20
while player_1_score < 20 or player_2_score < 20:
    temp1_score = 0
    while True:
        choice = input("Player 1's turn. Do you want to roll the dice? (y/n) :")
        if choice.lower() == 'y':
            dice1_number = dice_gen()
            if dice1_number == 1:
                print("Player 1 got a 1. Your score for this round is 0. It' player 2's turn now.")
                temp1_score = 0
                break
            else:
                print(f"Player 1 got a {dice1_number}")
                temp1_score += dice1_number
                print(f"Your temp score for this round is {temp1_score}")
                continue
        elif choice.lower() == 'n':
            break
    player_1_score += temp1_score
    if player_1_score >= 20 or player_2_score >= 20:
        break
    temp2_score = 0
    while True:
        choice = input("Player 2's turn. Do you want to roll the dice? (y/n) :")
        if choice.lower() == 'y':
            dice2_number = dice_gen()
            if dice2_number == 1:
                print("Player 2 got a 1. Your score for this round is 0. It' player 1's turn now.")
                temp2_score = 0
                break
            else:
                print(f"Player 2 got a {dice2_number}")
                temp2_score += dice2_number
                print(f"Your temp score for this round is {temp2_score}")
                continue
        elif choice.lower() == 'n':
            break
    player_2_score += temp2_score
    if player_1_score >= 20 or player_2_score >= 20:
        break

print(f"Player 1 score: {player_1_score}, Player 2 score: {player_2_score}")
