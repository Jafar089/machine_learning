import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

f=pd.read_csv('student.csv')
# print(f.head())
plt.scatter(x=f.student_study_hours, y=f.student_marks_percentage)
plt.title("Student marks prediction by ML")
plt.xlabel('student_study_hours')
plt.ylabel('student_marks_percentage')
# plt.show()

# for Data cleaning in csv file
print(f.isnull().sum(),end="\n\n")
print(f.mean(),end="\n\n")
N=f.fillna(f.mean())
print(N.isnull().sum(),end="\n\n")
print(N.head())
x=f.drop("student_marks_percentage",axis='columns')
y=f.drop("student_study_hours",axis='columns')
print("Shape of x is",x.shape)
print("Shape of y is",y.shape)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=51)
print("Shape of x_train is",x_train.shape)
print("Shape of y_train is",y_train.shape)
print("Shape of x_test is",x_test.shape)
print("Shape of y_test is",y_test.shape)

from sklearn.linear_model import LinearRegression

