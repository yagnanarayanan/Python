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


class Programmer(Employee):

    def __init__(self, name, salary, role, languages):
        self.name = name
        self.salary = salary
        self.role = role
        self.languages = languages

    def print_prg(self):
        return f"Programmer\'s Name: {self.name}, Salary: {self.salary}, Role: {self.role}, Leaves: {self.no_of_leaves}" \
               f", Languages: {self.languages}"


yagna = Employee('Yagna Narayanan', 100, 'Learner')
rohan = Employee('Rohan Sharma', 200, 'Instructor')
subham = Programmer('Subham Patil', 500, 'Programmer', ['Java', 'C++'])
print(subham.print_prg())
print(subham.print_details())
