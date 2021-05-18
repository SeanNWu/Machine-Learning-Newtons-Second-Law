import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle


data = pd.read_csv("data.csv", sep=",") #the seperation would be ;
data = data[["mass","acceleration","force"]]
print(data.head())
predict = "force"

X = np.array(data.drop([predict],1))#taking in an array of eveything but force
Y = np.array(data[predict]) #force
X_TRAIN,X_TEST,Y_TRAIN,Y_TEST = sklearn.model_selection.train_test_split(X,Y,test_size = 0.1) #splitting ten percent of the data up
linear = linear_model.LinearRegression()
linear.fit(X_TRAIN,Y_TRAIN)
acc =linear.score(X_TEST,Y_TEST)
print("ACCURACY: ",acc)
mass = input("ENTER YOUR MASS (1-10)")
acce = input("ENTER ACCELERATION(1-10)")

newTest = [[mass,acce]]
print(linear.predict(newTest)," Newtons")


'''
prediction = linear.predict(X_TEST)
for x in range(len(prediction)):
    print(prediction[x],X_TEST[x],Y_TEST[x])
'''
