# class variable is searched in instance of B, then searched in instance of A and then in class B and then in class A
# uncomment the lines one by one to see the output change as per comment search
class A:
    class_variable = 'I am class variable in class A'

    # def __init__(self):
    #     self.class_variable = 'I am an instance variable in class A'


class B(A):
    pass
    #class_variable = 'I am class variable in class B'

    # def __init__(self):
    #     self.class_variable = 'I am an instance variable in class B'


a = A()
b = B()
print(b.class_variable)
# search: instance in B --> instance in A --> class var in B --> class var in A
