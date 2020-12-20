# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result
a = float(input("enter 1st number: "))
b = float(input("enter 2nd number: "))
c = input("enter operator (+,-,*,/,**): ")
if (a == 45 and b == 3 and c == "*") or (a == 3 and b == 45 and c == "*"):
    print(555)
elif (a == 56 and b == 9 and c == "+") or (a == 9 and b == 56 and c == "+"):
    print(77)
elif a == 56 and b == 6 and c == "/":
    print(4)
else:
    if c == "+":
        print(a+b)
    elif c == "-":
        print(a-b)
    elif c == "*":
        print(a*b)
    elif c == "/":
        if b != 0:
            print(a/b)
        else:
            print("div by 0 error")
    elif c == "**":
        print(a**b)
    else:
        print("invalid operation")
