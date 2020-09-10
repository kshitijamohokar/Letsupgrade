#!/usr/bin/env python
# coding: utf-8

# ## Question 1     

# In[ ]:


lst=[ 5,4,1,6,1,7,6,5,4 ]
sublist = [1,1,7]
for i in range(len(lst)): 
    if lst[i] == sublist[0]:
        for j in range(i+1,len(lst)): 
            if lst[j] == sublist[1]:
                for k in range(j+1,len(lst)): 
                    if lst[k] == sublist[2]:
                        print("Its a Match") 
                        break
                break

        break
else:
    print("Its gone")


# ## Question 2
# 

# In[ ]:


def test_prime(n):
    for i in range(2,n):
        if(n%i ==0):
            return False
    return True
lst = list(filter(test_prime,range(1,2500)))
print(lst)


# ## Question 3

# In[ ]:


lst = [' hi this is manikanta , i am from india']


# In[ ]:


Result = list(map(lambda x : x.title(),lst))


# In[ ]:


print(Result)

