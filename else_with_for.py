for i in range(5):
    print(i, end=' ')
else:
    print("for done successfully\n")
for i in range(5):
    print(i, end=' ')
    if i == 3:
        break
else:
    print("for done successfully\n")
for i in range(5):
    print(i, end=' ')
    if i == 3:
        continue
else:
    print("for done successfully\n")

