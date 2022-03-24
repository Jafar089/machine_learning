import pandas as pd
# printing data in series of array in pandas having index type is abcde
s1=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s1)
print(type(s1))

# # printing data in series of dictionary in pandas
# s2=pd.Series({'zain':10,'Ammad':20,'Jafar':30},index=['Ammad','zain','Jafar','bilal'])
# print(s2)


# # # Extracting element single or many in array
# n3=pd.Series([2,3,4,5])
# print(n3[2])
# print(n3[:4])
# print(n3[-2:])

# # # add value in series in array or both array add in series
# # # You can also divide multiply and minus using this method 
# n4=pd.Series([2,3,4,5,6,7])
# print(n4+5)
# n5=pd.Series([2,3,4,5,6,7])
# print(n4+n5)



# # # printing both colunm and row using DataFrame in pandas

# j1=pd.DataFrame({"Name":['Muhammad','Ali','Jafar'],"Marks":[80,85,75]},index=['x','y','z'])
# print(j1)

# # # read csv file using these functions head=first five row, tail= last five, shape=how many row&col
# iris=pd.read_csv('jafar1.csv')
# print(iris.head())
# print(iris.tail())
# print(iris.shape)
# print(iris.describe())

# # # iris.iloc method used for extracting the indexes in file and iris.loc method is for given name of index

# print(iris.iloc[0:9,0:3])

# # # iris.drop method for drpping row or colunm in list

# print(iris.drop('study',axis=1))
# print(iris.drop([1,2,3],axis=0))

# # printing values using loc method you can give colunm names
# print(iris.loc[0:9,('study','Quran')])

# # finding minimum and maximum mean and median values in csv file 

# print(iris.min())
# print(iris.max())
# print(iris.mean())
# print(iris.median())

# # using apply method to multiply or any other function you can apply
# def half(s):
#     return s*0.5
# print(iris[['ali','zain']].apply(half))

# # use to count value of the given colunm
# print(iris['ali'].value_counts())

# # use to sort any colounm values
# print(iris.sort_values(by='zain'))
