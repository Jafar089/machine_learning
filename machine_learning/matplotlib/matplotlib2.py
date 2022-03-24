import numpy as np
from matplotlib import pyplot as p

a=np.array([1,2,3,4,5,6,7,8,9,10])
y=3*a
y2=2*a
# p.plot(a,y,color='red',linestyle='--',linewidth=2)
# p.plot(a,y2,color='orange',linestyle=':',linewidth=2)
# p.title('Graph')
# p.xlabel('x-axis')
# p.ylabel('y-axis')
# p.grid(True)
# p.show()


#printing 2 graphs according to your chopice using subplot method

# p.subplot(1,2,1)
# p.plot(a,y,color='red',linestyle='--',linewidth=2)
# p.title('Graph')
# p.xlabel('x-axis')
# p.ylabel('y-axis')
# p.grid(True)
# p.subplot(1,2,2)
# p.plot(a,y2,color='orange',linestyle=':',linewidth=2)
# p.title('Graph')
# p.xlabel('x-axis')
# p.ylabel('y-axis')
# p.grid(True)
# p.show()



#Bar plot graph in series shape

# dict={'zain':89,'Jafar':77,'Ammad':100,'anne':41}
# names=list(dict.keys())
# values=list(dict.values())
# p.bar(names, values,color='red')
# p.title('Bar plot')
# p.xlabel('Names')
# p.ylabel('Marks')
# p.grid(True)
# p.show()



#Bar plot graph in horizontle shape

dict={'zain':89,'Jafar':77,'Ammad':100,'anne':41}
names=list(dict.keys())
vlues=list(dict.values())
p.barh(names, vlues,color='red')
p.title('Bar plot')
p.xlabel('Marks')
p.ylabel('Names')
p.grid(True)
p.show()

# printing scatter plot graph using this method

# x=[10,20,30,40,50,60,70,80,90]
# y=[5,7,2,4,3,9,5,1,6]
# z=[2,4,6,8,3,5,2,7,1]
# p.scatter(x, y,color='limegreen',marker='*',s=180)
# p.scatter(x, z,color='cyan',marker='.',s=80)
# p.title('Scatter Graph')
# p.xlabel('x-axis')
# p.ylabel('y-axis')
# p.show()

# printing scatter subplot graph using this method


# x=[10,20,30,40,50,60,70,80,90]
# y=[5,7,2,4,3,9,5,1,6]
# z=[2,4,6,8,3,5,2,7,1]
# p.subplot(2,1,1)
# p.scatter(x, y,color='limegreen',marker='*',s=180)
# p.title('Scatter Graph')
# p.subplot(2,1,2)
# p.scatter(x, z,color='cyan',marker='.',s=80)

# p.xlabel('x-axis')
# p.ylabel('y-axis')
# p.show()

#printing histogram graph using this method

# data=np.random.randint(1,100,12)
# print(data)
# p.hist(data,color='red',bins=4)
# p.show()

#printing csv file graph using this method

# import pandas as pd

# iris=pd.read_csv('jafar1.csv')
# p.hist(iris['ali'],color='orange')
# p.show()

#printing boxplot using this method

# median formula is apply 

# one=[1,2,3,4,5,6,7,8,9]
# two=[4,5,6,7,8,9]
# three=[2,1,7,4,5,7,1,5]
# final=list([one,two,three])
# p.boxplot(final)
# p.show()

#printing violonplot using this method
# one=[1,2,3,4,5,6,7,8,9]
# two=[4,5,6,7,8,9]
# three=[2,1,7,4,5,7,1,5]
# final=list([one,two,three])
# p.violinplot(final,showmedians=True)
# p.show()

#printing pie chart 

# fruits=['Apple','mango','orange','gauva']
# quantity=[50,60,80,15]
# p.pie(quantity,labels=fruits,autopct='%0.1f%%',colors=['yellow','green','orange','gray'],shadow=True)
# p.show()

# doughnut chart print using this method

# fruits=['Apple','mango','orange','gauva']
# quantity=[50,60,80,15]
# p.pie(quantity,labels=fruits,radius=1.5)
# p.pie([100],colors=['white'],radius=1)
# p.show()


