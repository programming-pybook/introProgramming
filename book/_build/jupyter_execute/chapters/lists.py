#!/usr/bin/env python
# coding: utf-8

# # Lists [^intro]
# 
# [^intro]: This Jupyter Notebook is based on Chapter 8 of {cite}`Severance2016` and Chapter 10 of {cite}`thinkPython`.

# ## A List is a Sequence
# 
# Like a string, a list is a sequence of in principle *arbitrary* values, as we have seen with *string*s. 
# 
# In a string, the values are characters; in a list,
# they can be any type. 
# 
# The values in a list are called **elements** or **items**.
# 
# A new list can be created in different ways.
# 
# The simplest way is to put the elements between square (`[` and `]`) brackets.
# 
# Lists can be assigned to variables.

# In[1]:


int_list : list = [10, 20, 30, 40]

print(int_list)
type(int_list)


# This is a list of four integers.

# In[2]:


str_list : list = ['data science', 'computer science', 'programming', 'statistics']

print(str_list)
type(str_list)


# This is a list of four strings.
# 
# However, it is not necessary that the elements of a list are of the same type.
# 
# We can even have other lists as elements.
# 
# A list within another list is said to be **nested**.

# In[3]:


messy_list : list = ['data science', 2, 3.14, [7, 42]]

print(messy_list)
type(messy_list)


# Of course, you can assign list values to variables.

# In[4]:


bikes : list = ['Gazelle', 'Trek', 'Sparta', 'Specialized']
numbers : list = [7, 42, 6*42]
empty_list : list = []

print(bikes, numbers, empty_list)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Create a list of strings, where each string represents the name of a dutch artist. Assign the list to the variable <i>dutch_artists
# ```

# In[5]:


# Remove this line and add your code here


# ## Lists are Mutable
# 
# In contrast to strings, list elements can be changed.
# 
# The syntax for accessing elements of a list is the same as for accessing characters of a string: the bracket operator.
# 
# The expression inside the brackets is the index of the list element.

# In[6]:


bikes[0]


# Lists are mutable, so we can change the value of a list element via an assignment. 
# 
# 

# In[7]:


bikes[0] = 'Merida'

print(bikes)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Change the last item of your list `dutch_artists`. Think of another artist that you have not included before.
# ```

# In[8]:


# Remove this line and add your code here


# List indices work the same way as string indices:
# 
# * Any integer expression can be used as an index.
# 
# * If you try to read or write an element that does not exist, you get an IndexError.
# 
# * If an index has a negative value, it counts backward from the end of the list.

# In[9]:


'Grape'[-5]


# In[10]:


bikes[-1]


# The operator `in` works also for lists.

# In[11]:


'Sparta' in bikes


# In[12]:


'JanJanssen' in bikes


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Check if numbers 3 and 252 are in the list stored in the variable `numbers`.
# ```

# In[13]:


# Remove this line and add your code here


# ## Traversing a List
# 
# The most common way of traversing a list is by means of using a `for` loop. 
# 
# The syntax is the same as for strings.
# 
# ````{margin}
# ```{admonition} EXTRA
# The name of the *iterator* can be short, because it is typically a local variable.
# ```
# ````

# In[14]:


for b in bikes:
    print(b)


# This way of traversing lists works fine if you only want to read the elements.
# 
# If you iterate over the elements of a list and you do not need to update them, an iterator over the elements of the list is sufficient. 
# 
# If you need to *update* the elements of the list you have to iterate using explicit *integer indices*.
# 
# A common way to do that is to combine the built-in functions `range` and `len`, as shown in the next cell.

# `len` returns the length of the list.

# In[15]:


len(numbers)


# While `range` returns a list of indices ranging from `0` to `n-1`, where `n` is the length of the list, obtained via the function `len`.

# In[16]:


range(len(numbers))


# In[17]:


print(numbers)

for i in range(len(numbers)):
    numbers[i] *= 2
    
print(numbers)


# This loop traverses the list and updates each individual element.
# 
# Each iteration of the loop `i` gets the index of the next element in the range. 
# 
# The assignment statement in the body uses `i` to read the old value of the element and to assign the new value.

# In[18]:


for x in []:
    print('This never happens.')


# Is this a useful `for` loop?

# A `for` loop with an empty list never executes its body.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Iterate the `dutch_artists` list and change its items so all names appear in capital letters.
# ```

# In[19]:


# Remove this line and add your code here


# ## List Operations
# 
# A few useful list operations are `+` and `*`. 
# 
# Actually, we have seen these operations for strings as well. 
# 
# The `+` operator concatenates two lists as it happens with strings.

# In[20]:


a : list = [1, 2, 3]
b : list = [4, 5, 6]
c : list = a + b
c


# The `*` operator repeats a list for a given number of times.

# In[21]:


a : list = [1, 2, 3] * 5
a


# ## List Slices
# 
# Similar to strings it is also possible to take a slice of a list.

# In[22]:


subjects : list = ['data science', 'computer science', 'programming', 'statistics']

subjects[1:3]


# Recall, that if you omit the first index, the slice starts at the beginning. 

# In[23]:


subjects[:4]


# If you omit the second, the slice goes to the end. 

# In[24]:


subjects[2:]


# If you omit both, the slice is a copy of the entire list.

# In[25]:


subjects[:]


# Lists are mutable, so it is possible to use the slice operator in the left hand side of an assignment.
# However, beware, this changes the list. If you do not want this, make a copy.
# 
# A slice operator on the left side of an assignment can update multiple elements.

# In[26]:


subjects[3:4] = ['software engineering', 'machine learning']

subjects


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Slice the `dutch_artists` list. We require all items except the first one.
# ```

# In[27]:


# Remove this line and add your code here


# ## List Methods
# 
# Python provides methods that operate on lists. For example, `append` adds a new element
# to the end of a list.

# In[28]:


subjects : list = ['data science', 'computer science', 'programming', 'statistics']

subjects.append('software engineering')

subjects


# An alternative way of appending elements to a list is shown in the following cell.

# In[29]:


subjects : list = ['data science', 'computer science', 'programming', 'statistics']

print(subjects[4:])

subjects[4:] = ['software engineering']

subjects


# However, beware that this way of concatenating is error prone: if you use the wrong index, you will end up replacing instead of appending.

# In[30]:


print(subjects[4:])

subjects[4:] = ['system engineering']

subjects


# The method `extend` appends the list given argument to the list it is applied to. 
# 
# The list given as argument is not changed.

# In[31]:


subjects1 : list = ['data science', 'computer science', 'programming', 'statistics']
subjects2 : list = ['software engineering', 'artificial intelligence']

subjects1.extend(subjects2)

print(subjects1)
print(subjects2)


# The method `sort` sorts the elements of the list to which it is applied.
# 
# It uses the alphabetical order or from low to high if the elements are integers or floats.

# In[32]:


subjects1.sort()

subjects1


# In[33]:


numbers : list = [9, 5, 6, 2, 7, 1, 8, 4, 3]
numbers.sort()

numbers


# In order to be able to sort a list, the `sort` method should be defined on element *type*s.
# 
# So, sorting a list consisting of integers and strings is not possible, but a list of integers and floats can be sorted.

# In[34]:


ns_list : list = [3, 5, 2, 7, 'abc', 1, 'xyz']
ns_list.sort()

ns_list


# In[ ]:


ns_list : list = [3, 5, 2, 7, 4.0, 1, 1.5]
ns_list.sort()

ns_list


# Most list methods are void, that means they are non-fruitful functions. 
# 
# They modify the list and return `None`. 
# 
# Observe what happens if you write `nums = nums.sort()`.

# In[ ]:


nums : list = [9, 5, 6, 2, 7, 1, 8, 4, 3]
nums = nums.sort()

print(nums)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Use the `append` method to add a new artist to the `dutch_artists` list. Then sort all items.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Map, Filter and Reduce
# 
# We have seen in the previous section a number of operations that can be applied to lists.
# 
# We will continue discussing a number of operations that can be applied to the elements of a list.
# 
# Suppose you want to add all numerical values of a list. You would probably write the following function
# using a `for` statement.

# If you want to use a list as argument or result of a function together with a type hint you have to add the following line to your code:
# 
# `from typing import List`
# 
# If you know the type of the elements, for instance all elements are integers, you can write `nums : List[int]`. If you do not know the elements or the list contains elements of different types, you can write `elems : List[any]`.

# In[ ]:


from typing import List


# In[ ]:


def add_all(nums : List[int]) -> int:
    """accumulates the values of a list of integers
    """
    
    total : int = 0;
    for n in nums:
        total += n
    return total

print(add_all([9, 5, 6, 2, 7, 1, 8, 4, 3]))


# As the loop runs, `total` accumulates the sum of the elements; a variable used this way is
# sometimes called an **accumulator**.
# 
# Adding up the elements of a list is such a common operation that Python provides it as a
# built-in function, `sum`.

# In[ ]:


nums : List[int] = [9, 5, 6, 2, 7, 1, 8, 4, 3]

sum(nums)


# An operation like this combines a sequence of elements into a single value and is called **reduce**.
# 
# Sometimes you want to apply an operation to all elements of a list and construct on the fly a new list.
# 
# Suppose you want to capitalize all strings in a list.

# In[ ]:


def capitalize_all(lst : List[str]) -> List[str]:
    """capitalizes the first letter of all string elements
    """
    
    rlst : List[str] = []
    for e in lst:
        rlst.append(e.capitalize())
    return rlst

print(subjects1)
print(capitalize_all(subjects1))


# `rlst` is initialized with an empty list; each time through the loop, we append the next element.
# 
# So `rlst` is another kind of accumulator.
# 
# An operation like `capitalize_all` is sometimes called a **map** because it “maps” a function
# (in this case the method capitalize) onto each of the elements in a sequence.

# Another common operation is to select some of the elements from a list and return a sublist.
# 
# For example, the following function takes a list of numbers and returns a list that contains
# all numbers greater than 5.

# In[ ]:


def gtr_than_five(nums : List[int]) -> List[int]:
    """filters all numbers less than or equal to 5
    """
    
    result_nums : List[int] = []
    for n in nums:
        if n > 5:
            result_nums.append(n)
    return result_nums

print(nums)
print(gtr_than_five(nums))


# An operation like `gtr_than_five` is called a **filter** because it selects some of the elements and
# filters out the others.
# 
# Map, filter and reduce allow a concise but powerful way of manipulating list, certainly if combined

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Change all items in the `dutch_artists` list, so now they are shown in lower case. Is this a map, filter or reduce function?
# ```

# In[ ]:


# Remove this line and add your code here


# ## Deleting Elements
# 
# There are several ways of removing elements of a list, which one to choose depends on what kind of behaviour you want.
# 
# We start with the `pop` method. This operation removes an element at certain index (if given), otherwise it removes the last element of the list.
# 
# The `pop` method is a fruitful function: it returns the element that was removed.

# In[ ]:


topics : list = ['data science', 'computer science', 'programming', 'statistics']

elem : str = topics.pop(1)

print(topics)
print(elem)


# If you are not interested in the removed element, you can use the method `del`.

# In[ ]:


topics : list = ['data science', 'computer science', 'programming', 'statistics']

del(topics[1])
print(topics)


# If you want to remove specific element from a list you can use `remove`.
# 
# The return value of `remove` is `None`.

# In[ ]:


topics : list = ['data science', 'computer science', 'programming', 'statistics']

topics.remove('programming')
print(topics)


# If a consecutive number of elements have to be removed from a list, it is better to use a slice.

# In[ ]:


topics : list = ['data science', 'computer science', 'programming', 'statistics']

del(topics[1:3])
print(topics)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Remove the last item of the `dutch_artists` list. What operation did you choose and why?
# ```

# In[ ]:


# Remove this line and add your code here


# ## Lists and Functions
# 
# We already saw that we can use the function `sum` to add all items in a list, and the function `len` to get the size of a list.
# 
# There are other handy functions that you can use to compute values without writing your own loops.
# 
# Some of these functions are `min` and `max`.

# We use the function `max` to get the maximum number of a list.

# In[ ]:


max(numbers)


# We use the function `min` to get the minimum number of a list.

# In[ ]:


min(numbers)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Can you compute the average of the list `numbers` without using any loop?
# ```

# In[ ]:


# Remove this line and add your code here


# ## Lists and Strings
# 
# A string is a sequence of characters and a list is a sequence of values, but a list of characters is not the same as a string. 
# 
# To convert from a string to a list of characters, you can use `list`.

# In[ ]:


s : str = 'data science'

lst : list = list(s)
print(lst)


# Because `list` is the name of a built-in function, you should avoid using it as a variable
# name.
# 
# The `list` function breaks a string into individual characters. 
# 
# If you want to break a string (sentence) into words, you can use the `split` method.

# In[ ]:


claim : str = 'Data science is younger than computer science or not?'

words : list = claim.split()
print(words)


# An optional argument called a **delimiter** specifies which characters to use as word boundaries.
# 
# The following example uses a hyphen `-` as a delimiter.

# In[ ]:


big_word : str = 'Multi-language-programming'

words : list = big_word.split('-')
print(words)


# The function `join` is the inverse of the `split` operation.
# 
# It takes a list of strings (words) and concatenates the elements.
# 
# `join` is a string method and has to be invoked on the delimiter and
# pass the list as a parameter.

# In[ ]:


words : list = ['Data', 'science', 'is', 'fun!']
sentence : str = ' '.join(words)
print(sentence)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Can you change dots in the following message by spaces?
# ```

# In[ ]:


msg = 'We.want.to.modify.this.message'

# Remove this line and add your code here


# We usually read files to extract interesting information from it. 
# 
# To do so, we first need to find *interesting* lines that contain *interesting* information required by our program. To find this information we need to **parse** the interesting lines.

# Let's look at this example. We want to detect lines that have the following form:
# 
# ```python
# 'INFO Sending email [01-09-2020T07:44:11.144] from:bob@mail.nl to:alice@mail.nl'
# ```
# 
# We want to extract the sender of the email of all lines that start with the "INFO Sending email" string.
# 
# Later in the course we will see a more powerful mechanism, *regular expressions* to find patterns in strings.

# In[ ]:


def printSender() -> None:
    """ Look for interesting lines and print the sender of an email
    """
    logs = open('datasets/logs.txt') # Get lines from the logs.txt file
    
    for line in logs:
        line.rstrip() # Remove white spaces at the end of the string
        
        if line.startswith('INFO Sending email'): # Pick interesting lines
            words : list = line.split() # Split line into words
            print(words[4]) # Print the sender of the email

printSender()


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Can you now print the receiver of the email?
# ```

# In[ ]:


# Remove this line and add your code here


# ## Objects and Values
# 
# There is a subtle difference between *objects* and *values*. 
# 
# Even when two objects represent the same value, they may be considered to be distinct.

# In[ ]:


a : str = 'Data'
b : str = 'Data'

a == b


# `a` and `b` refer both to the string `"Data"`, but do they actually refer to the same string?
# 
# See Figure 8.1 from the book *Python for Everybody*.
# 
# ```{image} assets/figure102.png
# :align: center
# ```
# 
# `a` and `b` can refer to two different **objects** that have the same value, or they refer to the same **object**.
# 
# We can check this by means of the `is` operator.

# In[ ]:


a : str = 'Data'
b : str = 'Data'

print(a is b)

print(a == b)


# In this case Python creates one string object.

# Observe what happens if you change both strings in "Data science". 
# 
# Try to explain this based on the <i>split</i> method from the previous section.

# In[ ]:


a : str = 'Data science'
b : str = 'Data science'

print(a is b)

print(a == b)


# So, `list` objects are not the same.

# In[ ]:


a : list = [1, 2, 3]
b : list = [1, 2, 3]
a is b


# If you create two lists which are exactly the same: same number of elements and in the same order, two different objects are created.
# 
# The two lists are **equivalent**, they have the same elements, but they are not **identical**, they are not the same object.
# 
# If two objects are identical, they are also equivalent, but if they are equivalent, they are not necessarily identical.
# 
# If you want to be precise with your terminology, then you say that an object has a value.
# 
# If you evaluate `[1, 2, 3]`, you get a list object whose
# value is a sequence of integers. 
# 
# If another list has the same elements, we say it has the
# same value, but it is not the same object.

# ## Aliasing
# 
# What will be the result of the following Python fragment?

# In[ ]:


a : list = [1, 2, 3]
b : list = a
b is a


# 
# The assocication of a variabe with an object is called a **reference**.
# 
# In the previous example, both `a` and `b` refer to the same object:
# 
# ```{image} assets/figure104.png
# :align: center
# ```
# 
# If an object has more than one reference then the object is **aliased**.
# 
# If the aliased object is mutable, then changes made via one variable affects the other.

# In[ ]:


a : list = [1, 2, 3]
b : list = a
b[1] = 42

print(b)
print(a)


# In this case `a` and `b` are aliases for the same object.
# 
# **aliasing** is useful, but dangerous. 
# 
# It hinders the understandability of programs, you have to keep all references in mind.
# 
# It is safer to avoid aliasing when you are working with mutable objects.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Read about the `copy()` method. Can you modify the following code so only <i>b</i> is modified?
# ```

# In[ ]:


a = [1, 2, 3]
b = a
b[1] = 42

print(b)
print(a)


# ## List as Arguments
# 
# If you pass a list as an argument to a function, you have to be aware of the aliases.
# 
# The function gets a reference to the lists, which is a mutable object, so every modification
# to the list has effect on the original list.
# 
# 

# In[ ]:


def delete_head(lst : List[any]) -> None:
    """ Remove the head of a list
    """
    
    del lst[0]
    
topics = ['Data science', 'Computer science', 'Programming']

delete_head(topics)

print(topics)


# The parameter `lst` and the variable `topics` refer to the same object, are aliases.
# 
# ````{margin}
# ```{admonition} EXTRA
# Such a function has a so-called **side effect**, when developing functions make sure they are side effect free
# in order to increase the understandability of your software.
# ```
# ````
# 
# 
# It is important to distinguish between operations that modify lists and operations that create
# new lists. 
# 
# The `append` method modifies a list, whereas the `+` operator creates a
# new list.

# In[ ]:


lst1 : list = [1, 2]
lst2 : list = lst1.append(3)

print(lst1)
print(lst2)


# The return value of the function `append` is `None`.

# In[ ]:


lst3 : list = lst1 + [4]

print(lst1)
print(lst3)


# It is important to beware of aliases when you are writing functions that are supposed to modify lists.
# 
# The following function does not delete the head of a list.
# 

# ````{margin}
# ```{admonition} EXTRA
# The type hint of the `lst` argument of `bad_delete_head` is `List[any]` because this
# function operates on lists with arbitrary elements.
# ```
# ````

# In[ ]:


print(lst3)

def bad_delete_head(lst : List[any]) -> None:
    """ Removes the head of a list
    """
    
    lst = lst[1:]   #WRONG!
    print(lst)
    
bad_delete_head(lst3)
print(lst3)


# At the beginning of `bad_delete_head`, `lst` and `lst3` refer to the same list. 
# 
# At the end, `lst` refers to a new list, but `lst3` still refers to the original, unmodified list.
# 
# An alternative is to write a function that creates and returns a new list. For example, `tail`
# returns all but the first element of a list.

# In[ ]:


def tail(lst : List[any]) -> List[any]:
    """ Removes the head of a list
    """
    
    return lst[1:]
    
letters = ['a', 'b', 'c']

rest = tail(letters)

print(rest)

