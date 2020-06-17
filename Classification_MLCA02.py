#!/usr/bin/env python
# coding: utf-8

# In[3]:


#importing pandas to read the data
import numpy as np
import pandas as pd
#importing the train_test_split to split the data into train set and test set
from sklearn.model_selection import train_test_split
#importing the decision tree classifier model 
from sklearn.tree import DecisionTreeClassifier
# importing the metrics function
from sklearn import metrics
# importing the accuracy_score library to check the accuracy of the model
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn import tree
# importing the preprocessing library 
from sklearn import preprocessing


# In[4]:


#reading the csv file using the read function
injury_data=pd.read_csv('C:/Users/himaj/Desktop/ML_CA02/datasets/test2.csv')
list(injury_data.columns)


# In[6]:


#printing the first 10 rows of the dataset.
injury_data.head(6)


# In[7]:


# removing few unwanted or unnecessary coloumns
injury_data=injury_data.drop(['Longitude','Latitude'],axis=1)


# In[9]:


#checking the number of null values in each coloumn
print(injury_data.isnull().sum())


# In[11]:


#getting the list of all column names
injury_data.columns


# In[13]:


# renaming the column names
injury_data.columns=(['Master_Record_Number', 'Year', 'Month', 'Day', 'Weekend', 'Hour',
       'Collision_Type', 'Injury_Type', 'Primary_Factor', 'Reported_Location'])
injury_data.columns


# In[14]:


#injury_data_new = injury_data_new.dropna()
# importing the SimpleImputer to impute the null values
from sklearn.impute import SimpleImputer
impute_data= SimpleImputer(strategy="constant")
#print(imp.fit_transform(injury_data_new))
injury_data['Collision_Type']=impute_data.fit_transform(injury_data.Collision_Type.values.reshape(-1,1))
injury_data['Primary_Factor']=impute_data.fit_transform(injury_data.Primary_Factor.values.reshape(-1,1))
injury_data['Weekend']=impute_data.fit_transform(injury_data.Weekend.values.reshape(-1,1))


# In[15]:


# checking for any null values left
print(injury_data.isnull().sum())


# In[17]:


from sklearn import preprocessing
#calling the function labelencoder()
number = preprocessing.LabelEncoder()
injury_data['Collision_Type'] = number.fit_transform(injury_data.Collision_Type)
injury_data['Weekend'] = number.fit_transform(injury_data.Weekend)
injury_data['Primary_Factor'] = number.fit_transform(injury_data.Primary_Factor)
injury_data['Injury_Type'] = number.fit_transform(injury_data.Injury_Type)
#injury_data_new['Reported_Location'] = number.fit_transform(injury_data_new.Reported_Location)


# In[18]:


### Feature selection for columns 
feature = [ 'Weekend', 
       'Collision_Type','Primary_Factor']
# target column
target = ['Injury_Type']


# In[20]:


X = injury_data[feature] # Features
y = injury_data[target] # Target variable


# In[21]:


# spliting the dataset into the train set and the test set in the ratio of 70 and 30
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=1)


# In[22]:


# Creating an object for the decision tree 
model = DecisionTreeClassifier()


# In[23]:


# Training the model
model = model.fit(x_train,y_train)


# In[24]:


#Predicting the outcome of the testset
y_pred = model.predict(x_test)


# In[25]:


# checking the accuracy of the predicted model
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


# In[ ]:




