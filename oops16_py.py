# Setters & Property Decorators
class Person:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name
        self.email = f"{self.first_name}.{self.last_name}@gmail.comm"
        # above line over ridden by email setter

    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@gmail.com"

    @email.setter
    def email(self, string):
        print("Setting Now...")
        names = string.split('@')[0]
        # print(names)
        name = names.split(".")
        # print(name)
        self.first_name = name[0]
        self.last_name = name[1]

    @email.deleter
    def email(self):
        self.first_name = None
        self.last_name = None


p = Person('Narayanan', 'Yagna')
# email property set based on the first_name and last_name
# print(p.email)
p.first_name = 'Ravi'
# changing the first_name changes the email too
print(p.email)
# set the first_name and last_name based on email property
p.email = 'w.k@gmail.com'
print(p.first_name)
print(p.last_name)
del p.email
# deleting email of p will change the first_name and last_name to None by deleter
print(p.email)
