# generate 10 random arithmetic questions and evaluate them as user provides the answer for each question
# Don't proceed to the next question till user provides correct answer for each question
import random

for i in range(1, 11, 1):
    min_operand = 1
    max_operand = 10
    operators = ['+', '-', '*']
    operator_choice = random.choice(operators)
    operand_1 = random.randint(min_operand, max_operand)
    operand_2 = random.randint(min_operand, max_operand)
    while True:
        value = input(f"{operand_1} {operator_choice} {operand_2} = ")
        if str(value) == str(eval(str(operand_1)+str(operator_choice)+str(operand_2))):
            print(f"{eval(str(operand_1)+str(operator_choice)+str(operand_2))}")
            i += 1
            break
        else:
            print("Try again")
            continue
