l = 10
# global variable


def func1():
    """comment line l = 5 and global l alternatively and run program to see different results"""
    # l = 5
    # local variable
    global l
    # accessing global l in function and changing it
    l += 10
    print(l)


print(func1.__doc__)
func1()
print(l)
