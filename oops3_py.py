class Employee:
    no_of_leaves = 20

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        return f"Name: {self.name}, Salary: {self.salary}, Role: {self.role}, Leaves: {self.no_of_leaves}"


yagna = Employee('Yagna Narayanan', 100, 'Learner')
rohan = Employee('Rohan Sharma', 200, 'Instructor')
# yagna.name = 'Yagna Narayanan'
# yagna.salary = 100
# yagna.role = 'Learner'
# rohan.name = 'Rohan Sharma'
# rohan.salary = 200
# rohan.role = 'Pro'
# print(yagna.salary)
# print(rohan.no_of_leaves)
print(rohan.print_details())
print(yagna.print_details())
