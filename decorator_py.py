def deco(func):
    def a():
        print("**********Decorator Starts*************")
        func()
        print("**********Decorator Ends***************")
    return a


@deco
def print_something():
    print("Hi there")


print_something()
