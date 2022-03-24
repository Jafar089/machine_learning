import numpy as np

# #printing sum indexing wise

# l2=np.array([1,2,3,4,5])
# l3=np.array([1,2,3,4,5])
# l4=l2+l3
# print(l4)

# #multiply by scaler
# n1=np.array([[1,2,3],[2,4,6]])
# n2=2*n1
# print(n2)

# # printing an identity matrix

# i=np.eye(4)
# print(i)

# # printing 1 d array to 3d array

# def p(x):
#     for i in range(x):
#         l2.append(i)
# l2=[]       
# n=p(27)
# a = np.array(l2)
# o = a.reshape((3,3,3))
# print(o)

# #convert float numpy to int numpy array

# a = np.array([[2.5, 3.8, 1.5],
#               [4.7, 2.9, 1.56]])
# o = a.astype('int')
# print(o)

# n=np.arange(0,101,2)
# print(n)

# # printing same index elements 

# a = np.array([1,2,3,4,5])
# b = np.array([1,3,2,4,5])
# print(np.where(a == b))


# # Output a sequence of equally gapped 5 numbers in the range 0 to 100 (both inclusive)

# o = np.linspace(0, 100, 4)
# print(o)

# # n=np.full((2,3),5)
# # print(n)

# #print 2d array ten times

# a = np.array([[1,2,3],
#               [4,5,6]])
# o = np.tile(a, 10)
# print(o)

# n=np.random.randint(0,10,25)
# n.shape = (5,5)
# print(n)

# # Multiply 2 arrays of numpy using this method

# a = np.array([[1,2,3],
#               [4,5,6],
#               [7,8,9]])
# b = np.array([[2,3,4],
#               [5,6,7],
#               [8,9,10]])
# o = a@b
# print(o)


# #printing transpose of matrix in numpy
# a = np.array([[1,2,3],
#               [4,5,6],
#               [7,8,9]])
# a_transpose = a.T
# print(a_transpose)


# #printing sin value in numpy array
# angles = np.array([45, 90, 180])
# sine_of_angles = np.sin(angles)
# print('Sine of the given array of angles = ', sine_of_angles)