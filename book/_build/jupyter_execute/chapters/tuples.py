#!/usr/bin/env python
# coding: utf-8

# # Tuples [^intro]
# 
# [^intro]: This Jupyter Notebook is based on Chapter 10 of {cite}`Severance2016` and on Chapters 12, 13 and 19 of {cite}`thinkPython`.

# In[1]:


from typing import Dict, List, Tuple
import random


# This notebook presents three more built-in types, **tuples**, **sets**, and **relations**, and then shows how these data types and previous ones work together. 
# 
# Additionally, the gather and scatter operators, a useful feature for variable-length argument lists, are presented.

# ## Tuples are Immutable
# 
# A **tuple** is a sequence of values. 
# 
# The values in a tuple can be of arbitrary types.
# 
# The elements of a tuple are indexed via integers, in that they resemble lists.
# 
# Tuples are *immutable*, whereas lists are *mutable*.
# 
# The following cells show a tuple with 5 elements, in the second cell *parentheses* are used to denote the tuple.

# In[2]:


t : tuple = 'data', 'computer', 'science', 'artificial', 'intelligence'
print(t)
type(t)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Create a tuple with the name of some countries as elements.
# ```

# In[3]:


# Remove this line and add your code here


# If you want to create a tuple with just one element, then you have
# to add a comma as terminator

# In[4]:


t1 : tuple = 'programming',

print(t1)
type(t1)


# A single value between parantheses is *not* a tuple.

# In[5]:


t2 : tuple = ('statistics')

print(t2)
type(t2)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Create a tuple with your name as single element.
# ```

# In[6]:


# Remove this line and add your code here


# You can create a tuple via the built-in function `tuple`.

# In[7]:


t : tuple = tuple()

print(t)
type(t)


# If the argument of the `tuple` function is a sequence (string, list, or tuple), the result is a tuple with the elements of the sequence.

# In[8]:


t : tuple = tuple('engineering')

print(t)
type(t)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Create a tuple out of the <i>artists</i> list.
# ```

# In[9]:


artists = ['John Lennon', 'Amy Winehouse', 'Adele', 'Bon Jovi', 'The Rolling Stones']
# Remove this line and add your code here


# `tuple` is a built-in function, so avoid using `tuple` as variable name.
# 
# Most list operators also work on tuples. The bracket operator indexes an element.

# In[10]:


t : tuple = ('data', 'computer', 'science', 'artificial', 'intelligence')
t[len(t) - 1]


# The slice operator allows you to select a range of elements.

# In[11]:


t[2:4]


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Use slicing to only return the values of 'Adele' and 'Bon Jovi' from your artists tuple.
# ```

# In[12]:


# Remove this line and add your code here


# Tuples are immutable, so if you try to assign a value to a tuple element, you will get an error message.

# In[13]:


t[0] = 'Data'


# In order to replace elements in a tuple, you have to create a new one.
# 
# So, *tuples* have a strong resemblance with *strings*.

# In[12]:


print(t)
t : tuple = ('Data',) + t[1:]
print(t)


# This statement makes a new tuple and then makes `t` refer to it.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Add a new artists to your artists tuple.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Comparing Tuples
# 
# The relational operators work with tuples and other sequences; Python starts by comparing
# the first element from each sequence. 
# 
# If they are equal, it goes on to the next elements, and
# so on, until it finds elements that differ. 
# 
# Subsequent elements are not considered (even if
# they are really big).

# In[13]:


('abc',) == ('abc','def')


# In[14]:


(0, 3, 20) < (0, 3, 40000)


# The `sort()` function works in the same manner. 
# 
# It sorts based on the first element. 
# If there is a tie it considers the second one, and so on.
# 
# This feature is used within the **DSU pattern**:
# 
# - **Decorate** a sequence by creating a list of tuples with sort keys preceding the elements of the sequence.
# - **Sort** the list of tuples with the `sort()` function.
# - **Undecorate** by extracting the elements of the sequence.

# In[15]:


poem : str = 'My tactic is to talk to you and listen to you and construct with words an indestructible bridge'

words : list = poem.split()
length_words : list = list()

for word in words:
    length_words.append((len(word), word))
    
length_words


# In this example, we want to sort words from the longest to the shortest.
# 
# To do so, we consider our text (i.e. `poem`) and we create a list of words with the `split()` function.
# 
# Then, we iterate over the list and we append a tuple to the `length_words` list.
# 
# This tuple has the length of the word as first element, and the word itself as second element.
# With this we *decorate* the original sequence of words.

# In[16]:


length_words.sort(reverse=True)

length_words


# Afterwards, we *sort* the list of tuples (i.e. `length_words`).

# In[17]:


sort_words : list = list()

for length, word in length_words:
    sort_words.append(word)
    
print(sort_words)


# Finally, we iterate over the list of tuples (i.e. `length_words`) to *undecorate* te sequence, and we append each word to the new list `sort_words`.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Let's consider again the <i>poem</i> variable. We want to sort its words based on the number of times that the letter <i>a</i> appears on it. Use the DSU pattern.
# ```

# In[ ]:


poem = 'My tactic is to talk to you and listen to you and construct with words an indestructible bridge'
# Remove this line and add your code here


# ## Tuple Assignment
# 
# Python allows us to have a tuple on the left side of an assignment.
# 
# In this way, we can assign more than one variable at a time.
# 
# We usually omit the use of parentheses on the left side of an assignment statement.

# In[18]:


my_list : list = ['Data', 'Science']

a, b = my_list

print(a)
print(b)


# If you want to swap the value of two variables you can use a temporary variable.

# In[21]:


a : str = 'Data'
b : str = 'Computer'

tmp : str = a
a = b
b = tmp

print('a =', a)
print('b =', b)


# You can also use the **tuple assignment**.

# In[22]:


a : str = 'Data'
b : str = 'Computer'

print((b, a))

(a, b) = (b, a)

print('a =', a)
print('b =', b)


# The left side is a tuple of variables; the right side is a tuple of expressions. 
# 
# Each value is assigned to its respective variable. 
# 
# All the expressions on the right side are evaluated
# before any of the assignments.
# 
# The tuple assignment requires that both sides have the same number of elements.
# 

# ````{margin}
# ```{admonition} EXTRA
# Note that we are creating a new tuple and not updating an existing tuple.
# ```
# ````

# In[23]:


a, b = 'Data', 'Computer'

print(b)


# More generally, the right side can be any kind of sequence (string, list or tuple). 
# 
# For example,
# to split an email address into a user name and a domain, you could write:

# In[24]:


uname, domain = 'monty@python.org'.split('@')

print(domain)


# The return value from split is a list with two elements; the first element is assigned to `uname`, the second to `domain`.

# In[25]:


print('uname =', uname)
print('domain =', domain)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Assign the elements of the list <i>artist</i> to a tuple with three elements. Then, rearrange the tuple so we get them in the right order, i.e. The, Rolling, Stones.
# ```

# In[ ]:


artist = ['Rolling', 'Stones', 'The']
# Remove this line and add your code here


# ## Tuples as Return Values
# 
# A function/method can return only one single value.
# 
# By means of a tuple a function can return a collection of values.
# 
# Suppose you want to divide two integers and compute the quotient and remainder. 
# 
# It is inefficient to compute `x / y` and then `x % y`. 
# 
# It is better to compute them both at the same time via the function `divmod`.

# In[26]:


t : tuple = divmod(7, 3)
(quot, rem) = t
print('quotient =', quot)
print('remainder =', rem)


# Using the tuple assignment you can obtain the results separately.

# In[27]:


(quot, rem) = divmod(7, 3)
print('quotient =', quot)
print('remainder =', rem)


# The calculation of the `min` and `max` can be captured as follows, where
# `min` and `max` are built-in functions for finding the smallest and largest elements of a sequence.

# In[28]:


from typing import List, Tuple

def min_max(t : List[int]) -> Tuple:
    """given a list return the min and the max value in the list
    """
    
    return min(t), max(t)

min_max([2,5,1,7,4,9])


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Create a function that takes a list of strings and returns the shortest and longest words as a tuple.
# ```

# In[ ]:


words = ['What', 'matters', 'in', 'life', 'is', 'not', 'what', 'happens', 'to',
         'you', 'but', 'what', 'you', 'remember', 'and', 'how', 'you', 'remember', 'it']
# Remove this line and add your code here


# ## Variable-length Argument Tuples
# 
# Functions/methods can take a variable number of arguments.
# 
# A parameter name that starts with a `*` **gathers** arguments into a tuple.
# 
# The `gather` argument can have any name, but often the name `args` is used.

# In[29]:


def print_all(*args : any) -> None:
    print(args)
    
print_all(1, True, '42')


# The inverse of the gather is **scatter**, it splits the tuple in separate elements.

# In[31]:


t : tuple = (7, 3)

#type(t)

divmod(t)


# In[32]:


t : tuple = (7, 3)

divmod(*t)


# A number of built-in functions use variable-length argument tuples.

# In[33]:


max(1, 4, 7, 1, 25, 8)


# An exception is the `sum` function.

# In[34]:


sum((1, 2, 3), 0)


# In[35]:


def sum_all(*args : Tuple) -> int:
    print(type(args))
    return sum(args, 0)
    
x = sum_all(1,2,3,4,5,6,7,8,9)
print(x)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Create a function that receives a variable number of arguments and multiples all received items. Then, it returns the result.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Lists and Tuples
# 
# `zip` is a built-in function that takes two or more sequences and returns a list of tuples where each tuple contains one element from each sequence. 
# 
# The name of the function refers to a zipper.

# In[45]:


s = 'abc'
t = [0, 1, 2]

z = zip(s, t)
print(z)


# The result of the `zip` is a **zip object** that knows how to iterate through the elements.
# 
# The best way is to use a `for` loop.

# In[52]:


for pair in zip(s, t):
    print(pair)


# Observe the subtle difference between the code in the cell above and below, by running the cell below *twice* in a row.
# 
# The variable `z` does not contain a value representing the list of tuples, but the zip object.

# In[53]:


for pair in z:
    print(pair)


# In[48]:


z[0]


# A zip object is an iterator that iterates through a sequence.
# 
# There are 2 major differences:
# * indexing an element is not supported
# * the iteration cannot be repeated
# 
# If you want to use list operators and methods, you can use a zip object to make a list.

# In[54]:


list(zip(s, t))


# The result is a list of tuples consisting of a character and a digit.
# 
# If the lists you are zipping have not the same length, the result is a zip object with the length of the shortest list.

# In[ ]:


list(zip('Data', 'Computer'))


# You can use **tuple assignment** in a `for` loop to traverse a list of tuples.

# In[55]:


t : list = [('a', 0), ('b', 1), ('c', 2)]

for letter, number in t:
    print(number, letter)


# If you combine `zip`, a `for` loop and a tuple assignment, you get a useful idiom for traversing two (or more) sequences at the same time. 
# 
# The function `has_match()` takes two sequences, `t1` and `t2`, and returns `True` if there is an index `i` such that `t1[i] == t2[i]`.

# In[58]:


from typing import List

def has_perfect_match(t1 : List[any], t2 : List[any]) -> bool:
    """checks whether there is at least one matching element
    """
    
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False

has_perfect_match(['Data', 'Science', 'Statistics'], ['Computer', 'Science', "Programming"])


# The following cell shows the code if you want the index to be returned instead of a boolean value.

# In[59]:


from typing import List

def has_match(t1 : List[any], t2 : List[any]) -> int:
    """checks whether there is at least one matching element
    """
    i = 0
    for x, y in zip(t1, t2):
        if x == y:
            return i
        i += 1
    return -1

has_match(['Data', 'Science', 'Statistics'], ['Computer', 'Science', "Programming"])


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Use the `zip` function to create a list of tuples out of `nums1` and `nums2`. Then, iterate over the zip object and return True if there is at least one pair where the first number is divisible by the second one, False otherwise.
# ```

# In[ ]:


nums1 = [2, 3, 4, 4, 5]
nums2 = [5, 5, 3, 2, 5]
# Remove this line and add your code here


# If you need to traverse the elements of a sequence and their indices, you can use the built-in function `enumerate`.
# 
# The `enumerate` function has the same characteristics as the `zip` function.
# 
# It creates an **enumerate object** of which the elements can be accessed via iteration. 
# 
# Each pair contains an index (starting from 0) and an element from the given sequence.

# In[60]:


for index, element in enumerate('abcdef'):
    print(index, element)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Create a function that receives a list of integers and an integer as parameters. Use the <i>enumerate</i> function to traverse that list and return the position of the first number that is equal to the one received as parameter. If the number is not part of the list return -1.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Dictionaries and Tuples
# 
# Dictionaries are very handy to store values using keys. 
# 
# You can transform a dictionary into a **dict_items object**, which is similar to the **zip object** and the **enumerate object**.
# 
# You can transform a dictionary into a `dict_items` object via the built-in function `items`. 
# 
# This function returns a sequence of tuples, where each tuple is a key-value pair.

# In[61]:


d : dict = {'a': 0, 'b': 1, 'c': 2}

t = d.items()
t    


# The `dict_items` is an iterator that iterates over the key-value pairs.

# In[63]:


for key, value in d.items():
    print(key, value)


# You can use a list of tuples to create a dictionary.

# In[64]:


t : list = [('a', 0), ('c', 2), ('b', 1)]
d : dict = dict(t)
d


# Combining `dict` with `zip` yields a concise way to create a dictionary.

# In[65]:


d : dict = dict(zip('abcdef', range(6)))
d


# The dictionary method `update`  takes a list of tuples and adds them, as key-value pairs, to an existing dictionary.
# 
# It is common to use tuples as keys in dictionaries (primarily because you cannot use lists). 
# 
# For example, a telephone directory might map from last-name, first-name pairs to telephone numbers. 
# 
# Assuming that we have defined `last`, `first` and `number`, we could write the following statement.

# In[ ]:


directory : dict = dict()
directory['van den Brand', 'Mark'] = '2727'
directory['Ochoa', 'Lina'] = '2728'
directory['Seraj', 'Mazyar'] = '2729'

for last, first in directory:
    print(first, last, directory[last, first])


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Take the `eng_sp` dictionary and based on it create the `sp_eng` which swaps english words by spanish words. For instance, instead of having 'hello' : 'hola', the `sp_eng` dictionary will have 'hola' : 'hello'. Use the `items` method to achieve this goal.
# ```

# In[ ]:


eng_sp = {'hello' : 'hola', 'dog' : 'perro', 'cat': 'gato', 'love': 'amor', 'sport' : 'deporte'}
# Remove this line and add your code here

