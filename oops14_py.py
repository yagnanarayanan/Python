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

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return self.print_details()

    def __str__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"


yagna = Employee('Yagna Narayanan', 100, 'Learner')
rohan = Employee('Rohan Sharma', 100, ' Learner')
print(yagna + rohan)
print(yagna / rohan)
# calls dunder method __add__ and __truediv__
print(yagna)
# calls dunder method __str__ by overriding __repr__
print(repr(yagna))
