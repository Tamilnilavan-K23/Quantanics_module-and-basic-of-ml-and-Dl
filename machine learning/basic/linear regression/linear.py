import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge,Lasso

cd=pd.read_csv(r'F:\quantanics\computer Vision\machine learning\dataset\stock_data.csv',parse_dates=['Date'])
cd.set_index('Date',inplace=True)
print(cd)

x=cd[['AMZN','DPZ','BTC']]
y=cd[['NFLX']]

#change 1
"""
scalar=StandardScaler()
scalar_x=scalar.fit_transform(x)
"""

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,shuffle=False)

model=LinearRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

r2=r2_score(y_pred,y_test)

print("normal linear model:",r2)

rigd=Ridge(alpha=0.1)
rigd.fit(x_train,y_train)
y_pred_ridg=rigd.predict(x_test)

las=Lasso(alpha=0.1)
las.fit(x_train,y_train)
y_pred_las=las.predict(x_test)

print("ridge value:",r2_score(y_pred_ridg,y_test))
print("lasso value:",r2_score(y_pred_las,y_test))



"""
plt.figure(figsize=(10, 5))
plt.plot(y_test.index, y_test.values, label='Actual', color='blue')
plt.plot(y_test.index, y_pred, label='Predicted', color='red')
plt.title('Actual vs Predicted - AMZN')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
"""