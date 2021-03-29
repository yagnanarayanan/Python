"""
Iterable : __iter__() or __getitem__()  --> is the object iterable or not
Iterator : __next__()   --> if iterable, the iterator is called
Iteration
"""
# generate fibonacci and factorial generators


def gen(n):
    for i in range(1, n, 2):
        yield i
        # generate values on the fly to save RAM size


def gen_fac(a):
    c = 1
    if a == 0 or a == 1:
        yield 1
    else:
        for i in range(1, a+1):
            c = c*i
        yield c


def gen_fibo(nthterm):
    count = 0
    n1 = 0
    n2 = 1
    if nthterm == 1 or nthterm == 2:
        yield n2
    else:
        while count < nthterm:
            yield n1
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            count += 1

# g = gen(4)
# # only 1,3 will be produced
# # generator can be iterated only once
# print(g)
# print(g.__next__())
# print(g.__next__())
# # print(g.__next__())
# # line 19 produces error as generator run 3 times only
# my_name = 'Yagna'
# my_number = [123]
# print(my_number.__iter__())
# print(my_name.__iter__())
# ier = iter(my_name)
# print(ier.__next__())


# f = gen_fac(5)
# print(f)
# print(f.__next__())
fib = gen_fibo(6)
print(fib)
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
print(fib.__next__())
