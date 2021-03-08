# Diamond Shape Problem In Multiple Inheritance
# Level 0: class A
# Level 1: class B, class C
# Level 2: class D
class A:
    def val(self):
        print('Func A')


class B(A):
    pass
    # def val(self):
    #     print('Func B')


class C(A):
    pass

    # def val(self):
    #     print('Func C')


class D(B, C):
    # interchange to C, B to search in C first
    pass
    # def val(self):
    #     print('Func D')


a = A()
b = B()
c = C()
d = D()
d.val()
# search in D --> then search in B --> then search in C --> then search in A
