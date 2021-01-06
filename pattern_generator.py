# Pattern Printing
# Input = Integer n
# Boolean = True or False
#
# True n=5
# *
# **
# ***
# ****
#
# False n=5
# ****
# ***
# **
# *
def pattern_gen(row, cond):
    if cond:
        for i in range(0,row + 1):
            for j in range(0,i):
                print('*', end='')
            print('')
    else:
        for i in range(row,0,-1):
            for j in range(i,0,-1):
                print('*', end='')
            print('')

a = input("Enter number of rows: ")
b = input("Enter condition True (1) or False (0): ")
c = True
if b == '1':
    c = True
else:
    c = False
pattern_gen(int(a   ), c)
