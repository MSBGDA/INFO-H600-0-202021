#!/usr/bin/env python
# coding: utf-8

# In[20]:


print('Hello, my fellow')


# In[25]:


name = input("What's your name ?")
print('Nice to meet you,', name)


# In[26]:


print("This program computes the are of a rectangle.")
side_a = float(input("lenght of the rectangle in m ?"))
side_b = float(input("width of the rectangle in m ?"))
area = side_a * side_b
print('The area of the rectangle is %.2f m², congrats !' % area) #%f.2 -> 2 chiffres apres la virgule


# In[27]:


import numpy as np
print("Lets estimate now the circonference of a cercle.")
r = float(input("Give me a radius in m dude"))
circ = 2*r*np.pi
print("The circonference is %.3f m... Nice. Huh ?" % circ)


# In[56]:


print("Let's go for something... More ambitious," +name+ ".\nGive me two coordinates (X_a,Y_a) and (X_b,Y_b). I will estimate the euclidian distance between them")
A=[0,0]
B=[0,0]

A[0] = float(input("X_a ? "))
A[1] = float(input("Y_a ? "))
B[0] = float(input("X_b ? "))
B[1] = float(input("Y_b ? "))

d = np.sqrt( (A[0]-B[0])**2 + (A[0]-B[0])**2 ) 
print('The distance is %.3f ...Cool, cool, cool ?' % d)


# In[61]:


print('Bored ? Wait ! Last trick !')
word = input("Any last word?")
n = len(word)
print("**" + "*" * n+ "**\n* "+word+" *\n**"+ "*" * n+"**\nWow it's magic")


# In[ ]:




