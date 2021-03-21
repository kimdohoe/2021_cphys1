#!/usr/bin/env python
# coding: utf-8

# In[188]:


def logistic(r,n):
    r=4.5
    f=0.5
    for i in range(n):
        f=r*f*(1-f)
    return f

for j in range(1,20):
    print(logistic(4.5,j))


# In[189]:


def fibo(n):
    f1=1
    f2=1
    for i in range(n):
        f3=f1+f2
        f1=f2
        f2=f3
    return f3

print(fibo(3))


# In[ ]:




