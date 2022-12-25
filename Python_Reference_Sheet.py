
## Basic ideas in Python

# ### Data Structures
# 
# #### Lists



## we can throw anything into a list, a buch of lists as well
my_list = [1,2, True, 'hari',324.535]
my_lists = [[], 90]
len(my_list)
len(my_lists)


##### we can add something to our list by append
my_list.append(4)
my_list


# #### Tuple
# ##### Tuples are best for storing x-y coordinates or indexes. They are memory efficient.
my_tuple = (12, 'car', 'dog')
len(my_tuple)

# This throws an error
# my_tuple.append()

##### Sets
my_set= {1,2,3,3,2,1}
my_set

another_set = {9,8,7,345,"set"}
another_set


#### Dictionaries
#### These are different types of datatypes, which stores key value pairs in Python.

countries = {'USA': 'Washington,D.C', 'India': 'New Delhi', 'UK':'London'}
countries

## Dictionary doesn't have append function
# countries.append({'srilanka':'colombo'})

#### Strings

#### slicing is a way of formating, we have control over strings and lists using slices/
name = 'my name is Harinath'

###Slicing a string
n1 =name[0:10]
n2 = name[10:]
n1, n2


#### More in  formating

'My ticket number is: ' + str(131)
f'My number is: {5}'
f'My number is {5}, and twice that is {2*5}'



import math




f'TT(pi) = {math.pi:.2f}'


# #### Python BYTE object


bytes(4)


ThumbsUpBytes = bytes('👍', 'utf-8')
ThumbsUpBytes



ThumbsUpBytes.decode('utf-8')





# ### Object oriented programming


class Dog:
    def __init__(self, name):
        self.name = name
        self.age = 2
              
    def speak(self):
        print(self.name + ' says bow bow')    


my_pet = Dog("tyson")
rahuls_pet = Dog("simba")




my_pet.speak()
rahuls_pet.speak()




