#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math


# In[6]:


import numpy as np
import matplotlib.pyplot as plt


# In[7]:


a=np.arange(-100,100,0.01)
b=[np.sinc(x) for x in a]

plt.plot(a,b)


# In[11]:


def sinc(x,n):
    f=0
    for i in range(n):
        f += (-1)**i*x**(2*i)/math.factorial(2*i+1)
        return f
    
for j in range(100):
    print(sinc(x,j))


# In[ ]:




