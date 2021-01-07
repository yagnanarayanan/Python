'''
r : r mode opens a file for read-only. We do not have permission to update or change any data in this mode.
w : w mode does not concern itself with what is present in the file. It just opens a file for writing and
    if there is already some data present in the file, it overwrites it.
x : x is used to create a new file. It does not work for an already existing file, as in such cases the operation fails.
a : a stands for append, which means to add something to the end of the file. It does exactly the same. It just adds the
    data we like in write(w) mode but instead of overwriting it just adds it to the end of the file. It also does not
    have the permission of reading the file.
t : t mode is used to open our file in text mode and only proper text files can be opened by it. It deals with the file
data as a string.
b : b stands for binary and this mode can only open the binary files, that are read in bytes. The binary files include
images, documents, or all other files that require specific software to be read.
+ : In plus mode, we can read and write a file simultaneously. The mode is mostly used in cases where we want to update
our file.
'''
fp1 = open('yagna.txt', 'rt')
# rt is default mode
content = fp1.read()
print(content)
count1 = 0
count2 = 0
for char in content:
    count1 = count1 +1
    if char == '\n':
        count2 += 1
print("Number of characters in the file : ", str(count1))
print("Number of lines in the file : ", str(count2))
fp1.close()

fp2 = open('yagna.txt', 'rt')
content = fp2.read(4)
# reads first four characters
print(content)
fp2.close()

fp3 = open('yagna.txt', 'rt')
content = fp3.read()
count3 = 0
for char in content:
    count3 = count3 +1
    if char == 'o':
        break
print("First occurrence of '0' in file at position : ", str(count3))
fp3.close()

fp4 = open('yagna.txt', 'rt')
content = fp4.read()
count4 = 0
for char in content:
    if char == 'o':
        count4 += 1
print("Total number of occurrence of '0' in file : ", str(count4))
fp4.close()

fp5 = open('yagna.txt', 'rt')
print(fp5.readline())
# prints one line
print(fp5.readlines())
# use read lines to print all lines it prints as a list
fp5.close()

fp6 = open('yagna.txt','a+')
a = fp6.write('He is learning Python.\n')
print("Number of characters written : ", str(a))
fp6.close()

fp7 = open('yagna.txt', 'rt')
print(fp7.tell())
# tells position of file pointer
print(fp7.readline())
print(fp7.tell())
fp7.seek(0)
# moves file pointer to desired location
print(fp7.tell())
print(fp7.readline())
print(fp7.tell())
fp7.close()
# to avoid closing fp everytime use with block
with open('yagna.txt', 'rt') as fp8:
    a = fp8.read()
    print(a)

fp8 = open('yagna.txt', 'rt')
print("fp8 : ", str(fp8.tell()))
b = fp8.read()
print(b)
print("fp8 : ", str(fp8.tell()))
fp8.close()
