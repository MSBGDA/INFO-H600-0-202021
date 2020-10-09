#!/usr/bin/env python
# coding: utf-8

# # 1)

# In[ ]:


´#function to simplify
def f(a,b): 
    if a > 0: 
        if b > 1: 
            print(a) 
        else: 
            print(b) 
    else: 
        if b > 1: 
            print(a+b) 
        else: 
            print(b)


# In[5]:


def f2(a,b):
    if not(b>1):
        print(b)
    else:
        if a>0:
            print(a)
        else:
            print(a+b)


# # 2)

# In[16]:


a = 2 
b = 3 
c = 4 
test1 = True 
test2 = (b >= a) and (c >= b) # True and True = True
test3 = test1 or test2        # True or True = True
arret = test3 and (not test2) # True and not(True) = True and False = False


# In[17]:


a += 1 
b -= 1 
c -= 2 
test1 = True 
test2 = (b >= a) and (c >= b) # False and True = False
test3 = test1 or test2        # True or False = True
arret = arret or test2        # False or False = False
print('a=',a, 'b=',b, 'c=', c)


# # 3)

# In[20]:


def my_test(a=8): 
    print(a)

a = 5 
my_test(9)
my_test()
print(a)


# # 4)

# In[24]:


def valid_loto(a):
    return a >= 1 and a <= 42

valid_loto(5), valid_loto(50)


# # 5)

# In[26]:


16%4, 17%4


# In[28]:


def leap_year(year):
    return year % 4 == 0 and not(year % 100 == 0) or year % 400 == 0


# In[35]:


list_of_leap_year = []
year = 2000
while year < 2041:
    if leap_year(year) == True:
        list_of_leap_year.append(year)
    year += 1    
list_of_leap_year       


# # 7)

# In[36]:


def my_range_while(a,b):
    l = []
    while a < b:
        l.append(a)
        a += 1
    return(l)    


# In[37]:


my_range_while(3,13)


# In[43]:


def my_range_for(a,b):
    l = []
    for i in range(a,b):
        l.append(i)
    return(l)    


# In[44]:


my_range_for(3,13)


# # 8)

# In[45]:


def my_range_step_while(a,b,step):
    l = []
    while a < b:
        l.append(a)
        a += step
    return(l)  


# In[46]:


my_range_step_while(3,19,3)


# In[47]:


def my_range_step_for(a,b,step):
    l = []
    for i in range(a,b,step):
        l.append(i)
    return(l)


# In[48]:


my_range_step_for(3,19,3)


# # 9)

# In[49]:


def power2(number):
    l = []
    for i in range(number):
        l.append(number**2)
    return(l)    


# In[50]:


power2(6)


# # 10)

# In[51]:


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False       #iteration break with this condition
    return True    


# In[55]:


is_prime(6),is_prime(7)


# In[56]:


def list_prime(upper_num):
    l = []
    for i in range(upper_num):
        if is_prime(i) == True:
            l.append(i)
    return(l)        


# In[57]:


list_prime(17)


# # 11)

# In[60]:


def increasing(a,b,c):
    l = [a,b,c]
    m = []
    while len(l) != 0:
        m.append(min(l))
        del l[l.index(min(l))]
    return(m)    


# In[61]:


increasing(56,9,102)


# # 12)

# In[76]:


def two_highest_number(a,b,c):
    l = [a,b,c]
    m = []
    while len(m) < 2:
        m.append(max(l))
        del l[l.index(max(l))]
    return(m)    


# In[77]:


two_highest_number(56,9,102)


# # 13)

# In[89]:


import math as m
def second_degree_sol(a,b,c):
    delta = b**2 - 4*c*a
    if delta > 0:
        x1 = (-b - m.sqrt(delta)) / (2*a)
        x2 = (-b + m.sqrt(delta)) / (2*a)
        print('x_1 =',x1, 'AND x_2 =',x2)
    elif delta == 0:
        x = -b/(2*a)
        print('x=',x)
    else:
        print('No real solution dude')


# In[90]:


second_degree_sol(4,-5,7)


# In[91]:


second_degree_sol(1,0,-4)


# In[93]:


second_degree_sol(1,2,1)


# # 14)

# In[110]:


def next_instant(h,m,s):
    instant = [h,m,s]
    instant[2] += 1
    if instant[2] == 60:
        instant[2] = 0
        instant[1] += 1
    if instant[1] == 60:
        instant[1] = 0
        instant[0] += 1
    if instant[0] == 24:
        instant[0] = 0
    return(instant)


# In[111]:


next_instant(5,32,22)


# In[112]:


next_instant(23,59,59)


# # 16)

# In[140]:


def triangle_list(number):
    l = []
    m = []
    for i in range(1,number + 1):
        for j in range(1,i + 1):
            l.append(j)        
        m.append(l)
        l = []
    return(m)    


# In[141]:


triangle_list(4)


# In[ ]:




