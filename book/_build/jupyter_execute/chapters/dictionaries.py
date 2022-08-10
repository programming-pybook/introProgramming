#!/usr/bin/env python
# coding: utf-8

# # Dictionaries [^intro]
# 
# [^intro]: This Jupyter Notebook is based on Chapter 9 of {cite}`Severance2016` and Chapter 11 of {cite}`thinkPython`.

# ## A Dictionary is a Mapping
# 
# We know the concept of a dictionary already since our childhood, a dictionary is a list of (alphabet) list of words with, among others, their meaning or translation.
# 
# The **dictionary** data type in Python is similar to a list, but quite different from 
# the dictionaries we know from daily life.
# 
# In a list, the indices have to be integers; in a dictionary they can be (almost) any type.
# 
# A dictionary contains a collection of indices, which are called **keys**, and a collection of
# **values**, every key is associated with a single value. 
# 
# The association of a key and a value is called a **key-value pair** or sometimes an **item**.

# In mathematical language, a dictionary represents a mapping from keys to values, so you
# can also say that each key “maps to” a value. 
# 
# Consider a dictionary from English to Dutch words, both the keys and values are strings.

# The function `dict` creates a new dictionary with no items. 
# 
# Because `dict` is the name of a built-in function, you should avoid using it as a variable name.

# If you want to use a dictionary as argument or result of a function together with a type hint you have to add the following line to your code:
# 
# `from typing import Dict`

# In[1]:


from typing import Dict


# In[2]:


eng2dut : Dict = dict()
print(eng2dut)


# The curly-brackets, `{}`, represent an empty dictionary. 
# 
# To add items to the dictionary, you can use square brackets.

# In[3]:


eng2dut['one'] = 'een'


# We have now created one entry with the key `'one'` and the value `'een'`.
# 
# If we print our dictionary we will see one key-value pair, where the key and value are separated by a colon.

# In[4]:


print(eng2dut)


# You can also create a dictionary as follows.

# In[5]:


eng2dut : Dict = {'one': 'een', 'two': 'twee', 'three': 'drie', 'four': "vier"}
print(eng2dut)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Create a dictionary <i>capitals</i> that maps countries to capital cities. Use the country as key of the pair. Include the following: The Netherlands - Amsterdam, Brazil - Brasilia, Australia - Canberra, Cuba - Havana, Kenya - Nairobi, Canada - Ottawa, Japan - Tokyo.
# ```

# In[6]:


# Remove this line and add your code here


# We can add via the *key* index a *value* to the dictionary.

# In[7]:


eng2dut['five'] = 'vijf'
print(eng2dut)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Add two new pairs to the dictionary `capitals`.
# ```

# In[8]:


# Remove this line and add your code here


# When the dictionary is printed the order of the key-value pairs may have changed, as we saw.
# 
# The order of the items in the dictionary is unpredictable.
# 
# The order is no issue, because the retrieval of values is done via the keys and **not** via indices.

# In[9]:


eng2dut['two']


# If you try to retrieve a value for a non-existing key, you will get a `KeyError` exception.

# In[10]:


eng2dut['six']


# The function `len` will give you the number of key-value pairs in the dictionary.

# In[ ]:


len(eng2dut)


# The `in` operator also works on dictionaries. 
# 
# It tells you whether something is used as a key.

# In[ ]:


'one' in eng2dut


# In[ ]:


'een' in eng2dut


# If you want to check whether a **value** is stored in the dictionary, you have first to retrieve all values through the `values()` method.

# In[ ]:


dutch_words = eng2dut.values()

print(dutch_words)
'twee' in dutch_words


# The `in` uses a different algorithm to find the elements in a list or dictionary.
# 
# In a list, it uses a linear search algorithm: the longer the list gets the more time it will cost.
# 
# In a dictionary, a **hash table** is used: the `in` operator takes about the same amount of time no matter how many items are in the dictionary. This property makes dictionaries a very powerful data structure when storing large amounts of data.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Check if the `capitals` dictionary contains the key <i>Mexico</i>.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Dictionary as a Set of Counters
# 
# Suppose you are given a string and you want to count how many times each letter appears, the so-called letter frequency. 
# 
# It is not hard to imagine that this type of exercise is useful, but you will have to do more often in the future, think of the frequency of words in a text, names in an archive, purchases per customer, etc.
# 
# We are computing a **histogram**, which is a statistical term for a set of frequencies.

# There are multiple ways of doing this:
# 1. You could create 26 variables, one for each letter of the alphabet. 
#    Then you could traverse
# the string and, for each character, increment the corresponding counter, probably
# using a chained conditional.
# It is not hard to imagine that this does not work for arbitrary words in a text.

# 2. You could create a list with 26 elements. 
# Then you could convert each character to
# a number (using the built-in function `ord`).
# Again, this does not work for arbitrary names in a text, because what is an (efficient) way to convert a word into an index.

# 3. You could create a dictionary with characters as keys and counters as the corresponding
# values. The first time you see a character, you would add an item to the dictionary.
# After that you would increment the value of an existing item.
# This is actually a very general and reusable solution.
# 
# This is, by the way, a typical example where you have to think carefully before choosing your data representation.
# 
# A simple, but wrong, choice may work for a small set of elements, but may get complicated or expensive if the data
# becomes more bulky.

# An **implementation** is a way of performing a computation; some implementations are more efficient than others.
# 
# For example, an advantage of the dictionary implementation is that we
# do not have to know ahead of time which letters appear in the string and we only have to
# make room for the letters that do appear.

# In[ ]:


from typing import List


# In[ ]:


def histogram(word : str) -> Dict:
    """Creates a dictionary for counting the number of letters in a word
    """
    
    dct : Dict = dict()
    for ch in word:
        if ch not in dct:
            dct[ch] = 1
        else:
            dct[ch] += 1
    return dct

letter_hist : Dict = histogram('datascience')
print(letter_hist)


# The `dict` data type offers a number of built in methods, one of them is `get`.
# 
# The `get` method takes a *key* as first argument and a *default* value as second.
# 
# If the `key` is not found in the dictionary, an *item* is created with the first argument is `key` and the second argument as `value`.

# In[ ]:


def histogram(word : str) -> Dict:
    """Creates a dictionary for counting the number of letters in a word
    """
    
    dct : Dict = dict()
    for c in word:
        dct[c] = dct.get(c, 0) + 1
    return dct

letter_hist : Dict = histogram('computerscience')

print(letter_hist)


# ````{margin}
# ```{admonition} EXTRA
# Now we can use some useful Python libraries to plot our histogram.
# ```
# ````
# 
# In this case we use `matplotlib.pyplot` and `pandas` libraries.

# In[ ]:


# import the relevant libraries, see 
import matplotlib.pyplot as plt
import pandas as pd

get_ipython().run_line_magic('matplotlib', 'inline')

import pandas as pd

df = pd.DataFrame.from_dict(letter_hist, orient="index")
df.plot.bar(color="r")


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Call the `histogram` function with different inputs and print it to see how the histogram changes from case to case.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Dictionaries and Files
# 
# Now we want to count the occurrence of words in a file.
# 
# For this task we will consider a piece of text taken from *Romeo and Julliet* by William Shakespeare. This text has been altered in the sense that it does not include any punctuation.

# In[ ]:


try:
    fhand : str = open('datasets/romeo.txt')
except:
    print('File cannot be opened:', fname)
    exit()
    
romeo_dict : Dict = dict()
for line in fhand:
    words : list = line.split()
    for word in words:
        if word not in romeo_dict:
            romeo_dict[word] = 1
        else:
            romeo_dict[word] += 1
            
print(romeo_dict)


# In the previous code we use two `for` loops. The first one iterates over the lines of the document while the second one iterates over the words of the current line in the first loop.
# 
# This pattern is quite common and is known as **nested loops**. The first loop is called the **outer loop** while the second one is named the **inner loop**.

# In addition we have use the abbreviation of `counts[word] = counts[word] + 1` as `counts[word] += 1`. 
# 
# This abbreviation is also used with `-=`, `*=`, and `/=`.

# Now, let us consider a piece of text that does have punctuation marks and capital letters. 
# 
# In this regards, cases such as 'soft' and 'soft!', and 'Who' and 'who' will be considered as different words.
# 
# To solve both problems we can rely on the `lower` and `translate` string methods. 
# 
# The `translate` method receives a translation tables as input. To create this table we rely on the `maketrans` function, which get three parameters: characters to be replaced, characters to replace previous ones, and characters to delete. For our challenge we only need to define the third parameter.
# 
# We will also use the string constant `punctuation`, which defines the list of punctuation marks. We will need to import the module `string` to have access to this value.

# In[ ]:


import string
print(string.punctuation)


# In[ ]:


import string

try:
    fhand : str = open('datasets/romeo-full.txt')
except:
    print('File cannot be opened:', fname)
    exit()
    
romeof_dict : Dict = dict()
for line in fhand:
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words : list = line.split()
    for word in words:
        if word not in romeof_dict:
            romeof_dict[word] = 1
        else:
            romeof_dict[word] += 1
            
print(romeof_dict)


# ## Dictionaries and Lists
# 
# Lists can be used as values in a dictionary.
# 
# Suppose you want to create a dictionary where the frequency of the letters is the key and the value is a list of letters with that frequency.
# 
# In fact, you invert the dictionary, creating a dictionary that maps frequencies to letters.

# In[ ]:


def invert_dict(dct: Dict) -> Dict:
    inv_dct : Dict = dict()
    for key in dct:
        val = dct[key]
        if val not in inv_dct:
            inv_dct[val] = [key]
        else:
            inv_dct[val].append(key)
    return inv_dct


# Each time through the loop, `key` gets a key from `dct` and `val` gets the corresponding value.
# 
# If `val` is not in `inv_dct`, that means we haven’t seen it before, so we create a new item and
# initialize it with a **singleton** (a list that contains a single element). 
# 
# Otherwise we have seen this value before, so we append the corresponding key to the list.

# In[ ]:


new_dct : Dict = invert_dict(letter_hist)
#print(letter_hist)
print(new_dct)


# Lists can be values in a dictionary, as this example shows, but they cannot be keys. 

# In[ ]:


t : list = [1, 2, 3]
d : Dict = dict()
d[t] = 'oops'


# The keys must be **hashable**, or to put it more correctly, must be
# usable as argument for a hash function.
# 
# A **hash** is a function that takes a value (of almost any kind) and returns an integer. 
# 
# Dictionaries use these integers, called **hash values**, to store and look up key-value pairs.
# 
# A value must not be mutable in order to be usable for hashing, lists are mutable, so not suited for hashing.
# 
# When you create a key-value pair, Python hashes the key
# and stores it in the corresponding location. 
# 
# If you modify the key and then hash it again, it
# would go to a different location. 
# 
# In that case you might have two entries for the same key,
# or you might not be able to find a key.
# 
# So, dictionaries themselves are not suitable for hashing, because they are mutable as well.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Use the `invert_dict` function to invert the `romeo_dict` dictionary.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Looping and Dictionaries
# 
# If you use a dictionary in a `for` statements, the keys are used for traversing.
# 
# Consider the following `print_histogram` function.

# In[ ]:


def print_histogram(hst : Dict) -> None:
    """prints the dictionary
    """
    for key in hst:
        print(key, hst[key])
        
print_histogram(letter_hist)


# The keys are printed in an unsorted order. 
# 
# The built-in function `sorted` can be used if you want the keys to be sorted.

# In[ ]:


def print_histogram(hst : Dict) -> None:
    """prints the dictionary in a sorted manner
    """
    
    for key in sorted(hst):
        print(key, hst[key])
        
print_histogram(letter_hist)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Sort the keys of the <i>capitals</i> dictionary, and print each pair.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Reverse Lookup
# 
# Given a key it is easy to find the corresponding value, this is a so called **lookup**.
# 
# Suppose you have a value and you want to find the corresponding key.
# 
# There are two challenges: 
# 
# 1. A value may appear multiple times in the dictionary, keys are unique, but values not.
# Consider the translation of the English words: the noun "lettuce" and the verb "beat"; the Dutch word in both cases is "sla".
# Depending on the application, you might be able to pick one, or you create a list that contains all relevant keys.
# 
# 2. There is no simple syntax to do a reverse lookup; you have to search explicitly.
# 

# In[ ]:


def reverse_lookup(dct : Dict, val : any) -> any:
    for key in dct:
        if dct[key] == val:
            return key
    raise LookupError()


# In[ ]:


def reverse_lookup(dct : Dict, val : any) -> List[any]:
    rlist : List[any] = []
    for key in dct:
        if dct[key] == val:
            rlist.append(key)
    
    return rlist


# This function is again a typical application of the search pattern, however if the value is not found,
# we **raise** an exception.
# 
# The **raise statement** raises an exception, in our case it causes a `LookupError`, this is a built-in
# exception to indicate that a lookup operation failed.

# In[ ]:


his : Dict = histogram('programming')
key = reverse_lookup(his, 2)
key


# In[ ]:


his : Dict = histogram('programming')
key = reverse_lookup(his, 4)
key


# The effect when you raise an exception is the same as when Python raises one: it prints a
# traceback and an error message.
# 
# The `raise` statement can take a detailed error message as an optional argument. 
# 
# ```Python
# raise LookupError('value does not appear in the dictionary')
# ```
# 
# Beware that the reverse lookup is not efficient, in case of a large dictionary your program may become slow.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Use the `reverse_lookup` function to look for existing and non-existing keys in the `capitals` dictionary.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Global Variables
# 
# Variables that are created outside functions belong to the special frame called **__main__** and they are called **global**.
# 
# They can be accessed from any function. 
# 
# Unlike local variables, which disappear when their
# function ends, global variables persist from one function call to the next.

# It is common to use global variables for **flags**; that is, boolean variables that indicate (“flag”) whether a condition is true. 
# 
# For example, some programs use a flag named verbose to
# control the level of detail in the output.

# In[ ]:


verbose : bool = True

def example1():
    if verbose:
        print('Running example1')
        
example1()


# You can not just reassign a global variable.

# In[ ]:


been_called : bool = False

def example2():
    been_called = True       # WRONG
    print(been_called)
    
print(been_called)
example2()
print(been_called)


# What went wrong?

# The value of `been_called` did not change, because `been_called` in the function `example2` is considered a local variable.
# 
# The local variable goes
# away when the function ends, and has no effect on the global variable.
# 
# To reassign a global variable inside a function you have to declare the global variable before
# you use it.

# In[ ]:


been_called : bool = False

def example2():
    global been_called
    been_called = True
    print(been_called)
    
print(been_called)
example2()
print(been_called)


# The **global statement** tells the interpreter: “In this function, when I say
# `been_called`, I mean the global variable; do not create a local one.”
# 
# Another example is presented in the following cell.

# In[ ]:


count : int = 0

def example3(): 
    count += 1       # WRONG

example3()
print(count)


# In[ ]:


count : int = 0

def example3(): 
    global count
    count += 1

    
example3()
example3()
print(count)


# How about the following, is this correct?

# In[ ]:


known : Dict = dict()

def example5():
    known["a"] = 1
    
example5()
print(known)


# In[ ]:


known : Dict = {}

def example5():
    known["a"] = 1
    
example5()
print(known)


# In[ ]:


known : Dict = []

def example5():
#    known = ['b']
    known.append('a')
    
example5()
print(known)


# When working with variables that are mutable, you are allowed to change the values in the dictionary.

# ````{margin}
# ```{admonition} EXTRA
# Global variables can be useful, but if you have a lot of them, and you modify them frequently, they can make your programs hard to debug.
# ```
# ````
