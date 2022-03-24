import numpy as np
# creating simple array
l1=[1,2,3,4]
n1=np.array(l1)
print(n1,end="\n\n")

# # creating multi dimension array
# l2=[[1,2,3,4],[4,3,2,1]]
# n2=np.array(l2)
# print(n2,end="\n")

# # creating zeroes in array
# n3=np.zeros((2,3))
# print(n3,end="\n")

# # creating 10 2/2 times in array
# n4=np.full((2,2), 10)
# print(n4,end="\n")

# # creating number in sequence wise in array from 10 to 52 with the difference of 5
# n5=np.arange(10,52,5)
# print(n5)

# # creating random number in array between 1 to 100 diff. of 5
# n6=np.random.randint(1,100,5)
# print(n6)

# # checking and giving shape of a multi dimension array
# l7=[[1,2,5],[3,4,7]]
# n7=np.array(l7)
# print(n7)
# n7.shape = (3,2)
# print(n7)

# # verticle attach 2nd array in first
# n8=np.array([1,2,3,4])
# n9=np.array([5,6,7,8])
# n10=np.vstack((n8,n9))
# print(n10)

# # horizontle attach 2nd array in first
# n11=np.array([1,2,3,4])
# n12=np.array([5,6,7,8])
# n13=np.hstack((n11,n12))
# print(n13)

# # colunm wise attach 2nd array in first
# n14=np.array([1,2,3,4])
# n15=np.array([5,6,7,8])
# n16=np.column_stack((n14,n15))
# print(n16)

# # printing n18 - n17 in array
# n17=np.array([1,2,3,4])
# n18=np.array([4,6,2,8])
# n19=np.setdiff1d(n18,n17)
# print(n19)

# # printing common elements in array
# n20=np.array([1,2,3,4])
# n21=np.array([4,6,2,8])
# n22=np.intersect1d(n20,n21)
# print(n22)

# # printing sum of two arrays
# n23=np.array([1,2,3,4])
# n24=np.array([4,6,2,8])
# n25=np.sum([n23,n24])
# print(n25)

# # printing sum colunm wise of two arrays
# n26=np.array([1,2,3,4])
# n27=np.array([4,6,2,8])
# n28=np.sum([n26,n27],axis=0)
# print(n28)

# # printing sum row wise of two arrays
# n29=np.array([1,2,3,4])
# n30=np.array([4,6,2,8])
# n31=np.sum([n29,n30],axis=1)
# print(n31)

# # Arithmetic operators in an array
# n32=np.array([10,20,30])
# n32+=1
# print(n32)
# n32-=1
# print(n32)
# n32*=2
# print(n32)
# n32=n32/5
# print(n32)

# # mean median and standerd deviation in array using functions
# l0=[1,2,3,4,5,6,7,8,9]
# print(np.mean(l1))
# print(np.median(l1))
# print(np.std(l1))

# # save and load the numpy array in python
# l20=[2,3,4,5,6,7,8]
# m1=np.save('jafar_numpy', l20)
# m2=np.load('jafar_numpy.npy')
# print(m2)