import numpy as np
a = [1, 2, 3]
one_d_array = np.array(a)
print(one_d_array)
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
two_d_array = np.array(b)
print(two_d_array)
# 2 is step size below
print(np.arange(1, 10, 2))
print(np.zeros(5))
print(np.zeros((2, 3)))
print(np.ones(2))
print(np.ones((3, 2)))
# 10 evenly spaced numbers between 0 and 5
print(np.linspace(0, 5, 10))
# diagonal of matrix is 1 rest 0
print(np.eye(3))
# uniform distribution
d = np.random.rand(6)
print(d)
print(np.random.rand(5, 5))
# normal distribution
print(np.random.randn(5))
# 5 random numbers between 1 and 100 (not inclusive of 100)
print(np.random.randint(1, 100, 5))
# reshape a 1d array into a 2d array
d1 = d.reshape(3, 2)
print(d1)
# max value in array
print(d1.max())
# max value position
print(d1.argmax())
print(d1.shape)
print(d1.dtype)
print(a[1:])
one_d_array[1:] = 100
print(one_d_array)
# if the copy function is not used, the sliced array will just be a view of the original
# and changes made to the view will affect the original
one_d_copy = one_d_array.copy()
# one_d_copy = one_d_array
one_d_copy[:] = 99
print(one_d_copy)
print(one_d_array)
print(two_d_array)
print(two_d_array[:2, 1:])
arr = np.arange(1, 11)
print(arr)
print(arr[arr > 5])
arr1 = np.arange(50).reshape(5, 10)
print(arr1)
print(arr1[:2, :2])
print(arr1[arr1 < 16])
c = np.arange(5, 16, 3)
print(c)
print(c + 1)
print(c * 3)
print(np.exp(c))
print(np.max(c))
print(np.sin(c))
print(np.log(c))
# Numpy Exercises below
custom = np.arange(0, 9, 1)
custom_1 = custom.reshape(3, 3)
print(custom_1)
c2 = np.random.randn(25)
print(c2)
c3 = np.arange(0.01, 1.01, 0.01).reshape(10, 10)
print(c3)
c4 = np.linspace(0, 1, 20)
print(c4)
mat = np.arange(1, 26).reshape(5, 5)
print(mat.sum())
mat_copy = mat.copy()
no_of_col = mat_copy.shape[1]
print(mat)
print('column sum: ')
l1 = []
for j in range(0, no_of_col):
    s = 0
    for i in list(mat_copy[:, j]):
        s += i
    l1.append(s)
print(np.array(l1))
print(l1)
# or use below
mat.sum(axis=0)
