import random
# 1, 5, 10 and 25 is valid user input for change values to match the sum of change to the random value generated
# if user does not input any of the valid inputs, tell user to try again
# accept valid user input till user inputs '', then sum up the inputs to see if it matches to the random value
a = random.randint(1, 99)
print(f"Please give change for {a}")
change_sum = 0
valid = 1
while valid:
    change = int(input('Enter the first coin: '))
    if change in [1, 5, 10, 25]:
        valid = 0
        break
    else:
        print('Enter 1, 5, 10 or 25')
change_sum = change
flag = 1
while flag:
    change = input('Enter the next coin: ')
    if change == '':
        flag = 0
        break
    change = int(change)
    if change not in [1, 5, 10, 25]:
        print('Enter 1, 5, 10 or 25')
        continue
    change_sum += int(change)
if change_sum == a:
    print(f"That's the correct change for {a} !")
else:
    print('Better luck next time')
