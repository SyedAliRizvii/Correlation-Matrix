#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import Libariries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # Import Required Packages

# In[3]:


# to handle datasets
import pandas as pd
import numpy as np

# to visualise al the columns in the dataframe
pd.pandas.set_option('display.max_columns', None)
# suppress some warning
pd.options.mode.chained_assignment = None  # default='warn'


# # Load the data and Plot a Histogram of the SalePrice column

# In[4]:


# load dataset
data = pd.read_csv('house-price-data.csv')

data.hist(column='SalePrice',  bins = 250)


# In[5]:


data 


# In[11]:


df= pd.read_csv ('pima-indians-diabetes.csv')


# In[12]:


df


# In[13]:


Plasma = df.corr()
print(Plasma)


# In[17]:


matrix = df.corr().round(2)
sns.heatmap(matrix, annot=True, vmin=-1, vmax=1, center=0, cmap ='vlag')
plt.show()


# In[19]:


plt.savefig ('heatmap.png')


# In[ ]:




