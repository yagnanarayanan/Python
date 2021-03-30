# take size of list input from user
# tell user to input the items of the list
# ask user to choose to print a list or set or dictionary comprehension
l = []
size = int(input("Enter list size: "))
for i in range(size):
    item = input("Enter item name: ")
    l.append(item)
choice = int(input("1.list comprehension 2.set comprehension 3.dictionary comprehension :"))
l1 = [item for item in l]
s1 = {item for item in l}
d1 = {i: f"{l[i]}" for i in range(size)}
if choice == 1:
    print(f"list comprehension: {l1}")
elif choice == 2:
    print(f"set comprehension: {s1}")
elif choice == 3:
    print(f"dictionary comprehension: {d1}")
else:
    print("Invalid choice")