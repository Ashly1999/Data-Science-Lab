#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
get_ipython().run_line_magic('matplotlib', 'inline')
points, cluster_indexes = make_blobs(n_samples=300, centers=4, cluster_std=0.8, random_state=0)
x = points[:, 0]
y = points[:, 1]
plt.scatter(x, y, s=50, alpha=0.7)


# In[3]:


kmeans = KMeans(n_clusters=4, random_state=0)
kmeans.fit(points)
predicted_cluster_indexes = kmeans.predict(points)
plt.scatter(x, y, c=predicted_cluster_indexes, s=50, alpha=0.7, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=100)


# In[4]:


import pandas as pd
customers = pd.read_csv('customer_data.csv')
customers.head()


# In[5]:


kmeans = KMeans(n_clusters=5, random_state=0)
kmeans.fit(points)
predicted_cluster_indexes = kmeans.predict(points)
plt.scatter(x, y, c=predicted_cluster_indexes, s=50, alpha=0.7, cmap='viridis')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=100)


# In[8]:


inertias = []

for i in range(1, 10):
    kmeans = KMeans(n_clusters=i, random_state=0)
    kmeans.fit(points)
    inertias.append(kmeans.inertia_)
plt.plot(range(1, 10), inertias)

plt.xlabel('Number of clusters')
plt.ylabel('Inertia')


# In[10]:


import pandas as pd
customers = pd.read_csv('customer_data.csv')
customers.head()


# In[11]:


points = customers.iloc[:, 3:5].values

x = points[:, 0]

y = points[:, 1]

plt.scatter(x, y, s=50, alpha=0.7)

plt.xlabel('Annual Income (k$)')

plt.ylabel('Spending Score')


# In[12]:


kmeans = KMeans(n_clusters=5, random_state=0)

kmeans.fit(points)

predicted_cluster_indexes = kmeans.predict(points)

plt.scatter(x, y, c=predicted_cluster_indexes, s=50, alpha=0.7, cmap='viridis')

plt.xlabel('Annual Income (k$)')

plt.ylabel('Spending Score')

centers = kmeans.cluster_centers_

plt.scatter(centers[:, 0], centers[:, 1], c='red', s=100)


# In[13]:



cluster = kmeans.predict(np.array([[120, 20]]))[0]

clustered_df = df[df['Cluster'] == cluster]

clustered_df['CustomerID'].values


# In[14]:


from sklearn.preprocessing import LabelEncoder

df = customers.copy()

encoder = LabelEncoder()

df['Gender'] = encoder.fit_transform(df['Gender'])

df.head()


# In[16]:


points = df.iloc[:, 1:5].values

inertias = []

for i in range(1, 10):
    kmeans = KMeans(n_clusters=i, random_state=0)
    kmeans.fit(points)
    inertias.append(kmeans.inertia_)

plt.plot(range(1, 10), inertias)

plt.xlabel('Number of Clusters')

plt.ylabel('Inertia')


# In[17]:


kmeans = KMeans(n_clusters=5, random_state=0)

kmeans.fit(points)

df['Cluster'] = kmeans.predict(points)

df.head()


# In[19]:


results = pd.DataFrame(columns = ['Cluster', 'Average Age', 'Average Income', 'Average Spending Index', 'Number of Females', 'Number of Males'])

for i in range(len(kmeans.cluster_centers_)):
    age = df[df['Cluster'] == i]['Age'].mean()

    income = df[df['Cluster'] == i]['Annual Income (k$)'].mean()

    spend = df[df['Cluster'] == i]['Spending Score (1-100)'].mean()

    gdf = df[df['Cluster'] == i]

    females = gdf[gdf['Gender'] == 0].shape[0]

    males = gdf[gdf['Gender'] == 1].shape[0]

    results.loc[i] = ([i, age, income, spend, females, males])

results.head()


# In[ ]:




