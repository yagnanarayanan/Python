import os
print(dir(os))
print(os.getcwd())
# os.chdir("C://")
# uncommenting line 4 will give error as the directory will change so the file will not be available
# print(os.getcwd())
fp = open('physical.txt')
fp.close()
print(os.listdir())
print(os.environ.get('Path'))
print(os.path.exists("C://"))
print(os.path.isfile("C://"))
print(os.path.isdir("C://"))
