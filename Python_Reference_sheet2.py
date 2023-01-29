#!/usr/bin/env python
# coding: utf-8

# In[1]:


# list comprehension

my_list = [1,2,3,4,5]

[2*item for item in my_list]


# In[5]:


new_lst = list(range(100))
filtered_lst = [item for item in new_lst if item % 10 > 3  ]
print(filtered_lst)


# In[10]:


#list comprehensions with fnuctions

myString = 'My name is hari, I am from India'
myString.split(',')


# In[11]:


myString.split()


# In[12]:


# chaining functions in list comprehensions
def cleanWord(word):
    return word.replace( ",", " ").lower()
[cleanWord(word) for word in  myString.split()]


# In[13]:


[cleanWord(word) for word in  myString.split() if len(word) > 3] 


# In[20]:


# more on functions
def performOperation(num1, num2,  operation):
    if operation == "sum":
        return num1 + num2
    if operation == "multiply":
        return num1 * num2
    
performOperation(5, 4, "multiply")    


# In[28]:


# Named parameters

def performOperation(num1, num2, message = "what are we doing?", operation = "sum"):
    print(message)
    if operation == "sum":
        return num1 + num2
    if operation == "multiply":
        return num1 * num2
    
performOperation(5, 4, operation = "sum")   


# ### Arguments

# In[35]:


def doSomethingwithArgument(*args):
    return args 
doSomethingwithArgument(2,3,4)


# if we don't use * ahead of args in function this will return following

# TypeError: doSomethingwithArgument() takes 1 positional argument but 3 were given


# ### keywordArguments

# In[38]:


# Keyword arguments are dictionary, where as argumnets are tuple

def doSomethingwithArgument(*args, **kwargs):
    return args, kwargs 

doSomethingwithArgument(2,3,4, operation = "sum")

# Keywords arguments consider it in form of key and value pairs.


# In[66]:


import math

def performOperation(*args, operation):
    if operation == "sumv":
        return sum(args)
    else:
        return args * 5
    
performOperation(5, 4, operation="sum")    


# In[84]:


def University(program):
    message = "I'm a graduate studnet"
    print(program)
    def nested_function(name, Age):
        print(f' \\ student details :{locals()}')
       # print(f'student name: {name}, student_age:{Age}')
        
    nested_function("hari",23)
University("Data Analytics Engineering")  



# In[ ]:





# In[ ]:




