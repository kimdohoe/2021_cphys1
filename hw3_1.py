#!/usr/bin/env python
# coding: utf-8

# In[253]:


import numpy as np
import matplotlib.pyplot as plt
import math


# In[204]:


def leib(n):
    k=1
    t=0
    for i in range(1,n+1):
        t+=1*(-1)**(i+1)/(k+2*(i-1))
        
    return t

for j in range(1,100):
    print(leib(j)) 


# In[304]:


plt.figure(figsize=(9,6))
a= range(1,101)
b=[]
for i in range(100):
    b.append(leib(i+1))
    
plt.plot(a,b)
plt.xlabel ('n')

c= range(1,101)
d=[]
for i in range(100):
    d.append(math.pi/4)
plt.plot(c,d)
plt.legend(['Leibniz formula for π','π/4'])


# In[ ]:





# In[ ]:





# In[ ]:




