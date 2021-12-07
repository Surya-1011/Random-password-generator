#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random
import string

def generate_random_pass():
    
    length = int(input("Enter the length of your desired random password : "))
    Lcase = string.ascii_lowercase
    Ucase = string.ascii_uppercase
    Spl_char = string.punctuation
    number = string.digits
    
    combination = Lcase + Ucase + Spl_char + number
    temp = random.sample(combination,length)
    random_password = "".join(temp)

        return random_password

generate_random_pass()


# In[ ]:




