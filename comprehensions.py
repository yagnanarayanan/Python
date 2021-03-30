# list comprehension
list_comp = [i for i in range(1, 6) if i % 2 == 0]
print(list_comp)
# dictionary comprehension
dict_comp = {i: f"item{i}" for i in range(1, 6) if i % 2 == 0}
print(dict_comp)
# print(dict_comp.items())
# key value pairs interchanged in dictionary using dictionary comprehension
dict_comp = {value: key for key, value in dict_comp.items()}
print(dict_comp)
# set comprehension
dresses = {dress for dress in ['dress1', 'dress1', 'dress2']}
# set stores unique values
print(dresses)
# generator comprehension
odds = (i for i in range(1, 100) if i % 2 != 0)
print(odds)
print(odds.__next__())
print(odds.__next__())
