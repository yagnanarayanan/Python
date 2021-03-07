# Multilevel Inheritance
class Dad:
    games = 'Tennis'
    native = 'Mumbai'

    def __init__(self, name):
        self.name = name

    def print_native(self):
        return f"{self.name}\'s native is {self.native}"

    def print_game(self):
        return self.games


class Son(Dad):
    games = 'Basketball'

    def __init__(self, name):
        self.name = name

    def print_game(self):
        return self.games


class Grandson(Son):
    games = 'Cricket'

    def __init__(self, name):
        self.name = name

    def print_game(self):
        return self.games


p1 = Dad('p1')
p2 = Son('p2')
p3 = Grandson('p3')
print(p3.print_game())
print(p3.print_native())
print(p2.print_native())
print(p1.print_native())
