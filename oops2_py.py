class Employee:
    leaves = 10


yagna = Employee()
yagna.name = "Yagna Narayanan"
yagna.location = "India"
print(f"{yagna.name} from {yagna.location} has {yagna.leaves} leaves")
# yagna.leaves = 9
print(f"{yagna.name} from {yagna.location} has {yagna.leaves} leaves")
Employee.leaves = 8
print(f"{yagna.name} from {yagna.location} has {yagna.leaves} leaves")
print(yagna.__dict__)
print(Employee.__dict__)
