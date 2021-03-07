# private: starts with double under score __variable, to access directly use _classname__variablename
# protected: accessed in child classes, starts with under score _variable, to access directly
# use _classname_variablename
# public: variable
class Employee:
    __no_of_leaves = 20
    # private
    _flexi_leave = 2
    # protected

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


yagna = Employee('Yagna Narayanan', 100, 'Learner')
print(yagna._flexi_leave)
print(yagna._Employee__no_of_leaves)
