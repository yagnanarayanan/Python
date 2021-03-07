# Multiple Inheritance
class Employee:
    no_of_leaves = 20

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        return f"Name: {self.name}, Salary: {self.salary}, Role: {self.role}, Leaves: {self.no_of_leaves}"

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod
    def from_inst(cls, string):
        # params = string.split("-")
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))

    @staticmethod
    def print_good():
        print("Simple Function.")


class Player:
    no_of_games = 3

    def __init__(self, name, games):
        self.name = name
        self.games = games


class CoolProg(Employee, Player):
    language = 'C++'

    def print_lang(self):
        return f"{self.name}\'s language is {self.language}"


yagna = Employee('Yagna Narayanan', 100, 'Learner')
rohan = Employee('Rohan Sharma', 200, 'Instructor')
abishek = CoolProg("Abishek Tripati", 300, 'Cool Programmer')
print(abishek.print_details())
print(abishek.print_lang())
