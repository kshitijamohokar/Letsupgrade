#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[20]:


class bankAc():
    def __init__(self,ownerName,balance):
        self.owerName = ownerName
        self.balance = balance
    
    def deposit(self,d):
        self.balance += d
        print("you have added"+str(d)+"to your accont")
        print("your current bal is ",self.balance)
        
    def withdral(self,w):
        if w>self.balance:
            return "You have insuffficient balance"
        else:
            self.balance-=w
            print("you withdral amount is "+str(w)+" your current bal is"+str(self.balance))


# In[21]:


ac =bankAc("mani",5000)


# In[22]:


ac.deposit(2000)


# In[23]:


ac.withdral(1000)


# # Question 2 

# In[66]:


import math
class cone():
    def __init__(self,radius,height):
        self.radius = radius
        self.height = height
        
    def volume(self):
        ans = 1/3 *3.14*(self.radius**2)*self.height
        return  ans
    def surfaceArea(self):
        ans1 = 3.14*self.radius*(self.radius + math.sqrt(self.height**2+self.radius**2))
        return ans1
        


# In[67]:


ase = cone(4,5)


# In[68]:


ase.volume()


# In[69]:


ase.surfaceArea()


# In[ ]:




