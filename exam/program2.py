#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn


# In[2]:


student=pd.read_csv('student_scores.csv')
print(student)


# In[3]:


student.head()


# In[5]:


student.describe()


# In[6]:


customer=pd.read_csv('customer_data.csv')
print(customer)


# In[7]:


customer.head()


# In[8]:


customer.describe()


# In[12]:


from sklearn.metrices import(accuracy_score)
print("accuracy",accuracy_score(y_test,y_predict))
df=pd.DataFrame({'actual_vale':y_test,'predicted value':y_predict})


# In[13]:


from sklearn.model_selection import train_test_scale
X_train,X_test,Y_train,y_test=train_test_scale(X,y,test_score=0.20)
print(X_train)


# In[14]:





# In[16]:


df=pd.read_csv('student_scores.csv')
df


# In[17]:


dataset=df.values;
dataset


# In[20]:


col=['Hours','Scores']
student=pd.read_csv('student_scores.csv',names=col)


# In[21]:





# In[ ]:




