#!/usr/bin/env python
# coding: utf-8

# In[57]:


import numpy as np
import matplotlib.pyplot as plt


# In[58]:


def logistic(r,n):
    f=0.5
    for i in range(n):
        f=r*f*(1-f)
    return f

for j in range(1,100):
    print(logistic(0.5,j))


# In[85]:


plt.figure(figsize=(17,8))

y=[logistic(0.5,i) for i in range(1,100)]
plt.plot(list(range(1,100)),y, color='red',label='r=0.5')
plt.xlabel('n')
plt.ylabel('f(n)')

y=[logistic(0.95,i) for i in range(1,100)]
plt.plot(list(range(1,100)),y, color='black',label='r=0.95')
plt.xlabel('n')
plt.ylabel('f(n)')

y=[logistic(2,i) for i in range(1,100)]
plt.plot(list(range(1,100)),y, color='blue',label='r=2')
plt.xlabel('n')
plt.ylabel('f(n)')

y=[logistic(3.2,i) for i in range(1,100)]
plt.plot(list(range(1,100)),y, color='brown',label='r=3.2')
plt.xlabel('n')
plt.ylabel('f(n)')

y=[logistic(3.8,i) for i in range(1,100)]
plt.plot(list(range(1,100)),y, color='orange',label='r=3.8')
plt.xlabel('n')
plt.ylabel('f(n)')

y=[logistic(3.8,i) for i in range(1,100)]
plt.plot(list(range(1,100)),y, color='yellow',label='r=3.8')
plt.xlabel('n')
plt.ylabel('f(n)')

plt.legend()


# In[ ]:




