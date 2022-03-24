import pandas as pd
b=pd.read_csv('Boston.csv')
print(b.head())
y=b[['medv']]
x=b[['crim']]
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
l=LinearRegression()
print(l.fit(x_train,y_train))
y_pred=l.predict(x_test)
print(y_test.head())
print('\n\n\n')
print(y_pred[0:5])
from sklearn.metrics import mean_squared_error
print(mean_squared_error(y_test,y_pred))