#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a = np.matrix([[1,2],[3,8]])
print (a)
print (a*a)


# In[3]:


a = np.array ([[0, 1, 3],
              [2, 3, 5],
              [3, 5, 7]])
b = np.array ([-1, 3, 6])
print(np.linalg.inv(a) @ b)


# In[18]:


from scipy.integrate import quad, odeint
from scipy.special import erf

def f(x):
    return np.cos(x**2)+np.sin(x**2)

res, err = quad(f, 0, 10)
print (res)
print (err)


# In[22]:


from scipy.integrate import quad, odeint
from scipy.special import erf

def f(x):
    return np.exp(-x**2)

res, err = quad(f, 0, float("inf"))
print (res)
print (err)


# In[33]:


from scipy.integrate import quad, odeint
from scipy.special import erf

def f(x):
    return np.sign(x**3)

res, err = quad(f, 0, 2)
print (res)
print (err)


# In[35]:


np.poly([6, 7, 5])


# In[41]:
# In[ ]:





# In[ ]:




