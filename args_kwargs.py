def people(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    for key, value in kwargs.items():
        print(f"{key} is a {value}")


a = ["Harry", "Yagna", "Rohan"]
b = {"Harry": "Teacher", "Rohan": "Monitor", "Yagna": "Cook"}
people("People:", *a, **b)
