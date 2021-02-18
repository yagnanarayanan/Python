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


yagna = Employee('Yagna Narayanan', 100, 'Learner')
rohan = Employee('Rohan Sharma', 200, 'Instructor')
print(rohan.print_details())
print(yagna.print_details())
Employee.change_leaves(50)
print(yagna.print_details())
