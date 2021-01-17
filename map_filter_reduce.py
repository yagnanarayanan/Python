from functools import reduce
from math import sqrt
# -----------MAP------------------
l = ['3', '5', '8', '6']
print(f"Elements in list : {l}")
# increment the value in index 1 by 6
# for i in range(len(l)):
#     l[i]= int(l[i])
# l[1] = int(l[1]) + 6
# l[1] = str(l[1])
l = list(map(int, l))
l[1] += 6
# l = list(map(str,l))
print(f"Elements in list after incrementing 1st index element by 6 using map : {l}")
# list to have square of the elements


def square(a):
    return a*a


def sq_root(a):
    return sqrt(a)


func = [square, sq_root]
l1 = list(map(square, l))
print(f"Elements in new list with squares using map : {l1}")

l2 = list(map(lambda x: x*x*x, l))
print(f"Elements in new list with cubes using map : {l2}")

for i in range(3):
    val = list(map(lambda x: x(i), func))
    print(val)
# ------------FILTER--------------
# display numbers greater than 5 fom the list


def gt_5(a):
    if a > 5:
        return a


print(f"Elements in list : {l}")
l3 = list(filter(gt_5, l))
print(f"Elements in list greater than 5 from list using filter : {l3}")
# -------------REDUCE------------
# print the product of the numbers in the list
prod = reduce(lambda x, y: x*y, l)
print(f"Elements in list : {l}")
print(f"Product of elements in list using reduce : {prod}")
