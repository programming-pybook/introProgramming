#!/usr/bin/env python
# coding: utf-8

# # Sets [^intro]
# 
# [^intro]: This Jupyter Notebook is based on Chapter 10 of {cite}`Severance2016` and on Chapters 12, 13 and 19 of {cite}`thinkPython`.

# In[1]:


from typing import Dict, List, Tuple
import random


# This notebook presents three more built-in types, **tuples**, **sets**, and **relations**, and then shows how these data types and previous ones work together. 
# 
# Additionally, the gather and scatter operators, a useful feature for variable-length argument lists, are presented.

# ## Sequences of Sequences
# 
# In many contexts, the different kinds of sequences (strings, lists and tuples) can be used interchangeably. 
# 
# So how should you choose one over the others?

# **Option 1: Strings**
# 
# To start with the obvious, strings are more limited than other sequences because the elements have to be characters. 
# 
# They are also immutable. 
# 
# If you need the ability to change the
# characters in a string (as opposed to creating a new string), you might want to use a list of characters instead.

# **Option 2: Lists**
# 
# Lists are more common than tuples, mostly because they are mutable.

# **Option 3: Tuples**
# 
# There are a few cases where you might prefer tuples over lists:
# 1. In some contexts, like a return statement, it is syntactically simpler to create a tuple than a list.
# 2. If you want to use a sequence as a dictionary key, you have to use an immutable type like a tuple or string.
# 3. If you are passing a sequence as an argument to a function, using tuples reduces the potential for unexpected behavior due to aliasing.

# Because tuples are immutable, they do not provide methods like `sort` and `reverse`, which modify existing lists. 
# 
# But Python provides the built-in function `sorted`, which takes any
# sequence and returns a new list with the same elements in sorted order, and `reversed`,
# which takes a sequence and returns an iterator that traverses the list in reverse order.

# ## Sets
# 
# Python provides another **mutable** built-in type known as **set**.
# 
# A set is an **unordered** collection of elements that has **no duplicated** items.
# 
# We can create a set by listing its elements within curly braces (i.e. `{}`).

# In[2]:


fruits : set = {'apple', 'pear', 'papaya', 'mango', 'banana', 'apple'}
fruits


# Notice that we added `'apple'` twice but the set only considers one occurrence.

# To create a set we can use the `set()` function.

# In[3]:


candies : set = set()
type(candies)


# To add a new element to the set, we use the `add()` method.

# In[4]:


candies.add('chocolate')
candies.add('chocolate')
candies.add('marshmallow')
candies


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Create a set of `proteins` and add some items to it.
# ```

# In[5]:


# Remove this line and add your code here


# Sets provide methods and operators to compute common set operations (e.g. difference, union, intersection).
# 
# To compute the **union** between sets, we use the `union()` method or the `|` operator.

# In[6]:


food_fun : set = fruits.union(candies)
food_op : set = fruits | candies

print(food_fun)
print(food_op)


# To compute the **intersection** between sets, we can use the `intersection()` method or the `&` operator.

# In[7]:


fruits2 : set = {'apple', 'mango', 'pineapple', 'lemon'}
fruits_inter_fun : set = fruits.intersection(fruits2)
fruits_inter_op : set = fruits & fruits2

print(fruits_inter_fun)
print(fruits_inter_op)


# And to compute the **difference** between sets, we can use the `difference()` method or the `–` operator.

# In[8]:


fruits_diff_fun : set = fruits.difference(fruits2)
fruits_diff_op : set = fruits - fruits2

print(fruits_diff_fun)
print(fruits_diff_op)


# Some of exercises can be done concisely and efficiently with sets.
# 
# For example, let us consider a program that uses two dictionaries to find the words that appear in one dictionary but not in the other dictionary.

# In[9]:


words1 : dict = {'because': 3, 'you': 5, 'are': 2, 'mine': 2, 'not': 3,
    'I': 2, 'look': 1, 'die': 1, 'love': 1}

words2 : dict = {'you': 5, 'look': 1, 'die': 1, 'looking': 2}


res : dict = dict()
    
for word in words1:
    if word not in words2:
        res[word] = None
        
print(res)


# In all of these dictionaries, the values are `None` because we never use them. As a result, we waste some storage space.
# 
# There is a better way to solve this problem with sets.

# In[10]:


words1 : dict = {'because': 3, 'you': 5, 'are': 2, 'mine': 2, 'not': 3,
    'I': 2, 'look': 1, 'die': 1, 'love': 1}

words2 : dict = {'you': 5, 'look': 1, 'die': 1, 'looking': 2}

set(words1) - set(words2)


# The result is a set instead of a dictionary, but the behavior is the same.

# Let us see another example. Suppose we want to check if a list has duplicates. One way of doing it is using a `for` loop where we have an additional list to check wether the item is inlcuded there or not.

# In[11]:


def has_duplicates(lst: List[any]) -> bool:
    """ Check for duplicate elements in the list
    """
    
    lst_alt : List[any] = list()
    
    for elem in lst:
        if elem in lst_alt:
            return True
        else:
            lst_alt.append(elem)

    return False

lst1 = [1, 2, 3, 4, 5, 6, 2, 3]
lst2 = [1, 2, 3, 4, 5, 6, 7, 8]

print(has_duplicates(lst1))
print(has_duplicates(lst2))


# This function can be way simpler by using sets: we just need to check if the length of the list converted in a set is the same as the original list. Let's try.

# In[12]:


def has_duplicates(lst: List[any]) -> bool:
    """ Check for duplicate elements in the list
    """
    
    return len(set(lst)) < len(lst)

lst1 = [1, 2, 3, 4, 5, 6, 2, 3]
lst2 = [1, 2, 3, 4, 5, 6, 7, 8]

print(has_duplicates(lst1))
print(has_duplicates(lst2))


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Create a function that receives two dictionaries as input and prints the name of the keys shared by both of them. Use sets to solve this problem.
# ```

# In[13]:


dict1 = {'a' : 1, 'b': 2, 'c': 3}
dict2 = {'b': 1, 'z': 2, 'y': 3, 'c': 4}
# Remove this line and add your code here


# ## Data Structure Selection
# 
# You have seen the core data structures of Python.
# 
# We will now demonstrate which data structures are most suited to solve a specific problem.
# 
# Aspects that play a role when choosing a data structure are:
# * Ease of implementation
# * Runtime performance
# * Memory usage

# ### Word Frequency Analysis
# 
# The `string` module provides a predefined string `whitespace` that contains `space`, `tab`, `newline`, etc.

# In[14]:


import string
string.whitespace


# Furthermore, it contains a string `punctuation`, that contains punctuation characters.

# In[15]:


import string
string.punctuation


# Write a program that gets a file and breaks each line into words, strips whitespace and
# punctuation from the words, and converts them to lowercase.

# In[16]:


text = open('text.txt')


# In[ ]:


from typing import List, Dict

def split_text(text_arg : str) -> List[str]:
    """Splits a text into words which is returned as a list.
    The words are decapitalized (lower) and punctuation is stripped."""
    
    body : str = text_arg.read()
    
    stripped_words : list = []
    words : List[str] = body.split()
    for w in words:
        lower_w : str = w.lower()
        stripped_w : str = lower_w.strip(string.punctuation)
        stripped_words.append(stripped_w)
        
    return stripped_words

def histogram(words : List[str]) -> Dict:
    """transforms the list of words into dictionary
    """
    
    word_hist : dict = dict()
    for word in words:
        if word not in word_hist:
            word_hist[word] = 1
        else:
            word_hist[word] += 1
    return word_hist
 
text = open('text.txt') 

words = split_text(text)
print(len(words))

word_histo = histogram(words)
print(word_histo)


# In[ ]:


# import the relevant libraries, see 
import matplotlib.pyplot as plt
import pandas as pd

get_ipython().run_line_magic('matplotlib', 'inline')

import pandas as pd

df = pd.DataFrame.from_dict(word_histo, orient="index")

df.plot.bar(color="r")


# ### Word Histogram
# 
# The next cell contains a collection of functions to read a file and build a histogram.

# In[ ]:


def process_file(filename : str) -> Dict:
    """transforms the content of the given file into a dictionary of words 
    where the frequencies is counted
    """
    
    word_histo : dict = dict()
    fp  : TextIO = open(filename)
    
    for line in fp:
        process_line(line, word_histo)
        
    return word_histo

def process_line(line : str, histo : Dict) -> Dict:
    """add the words of a single line, after preprocessing, to the dictionary
    """
    
    line = line.replace('-', ' ')
    
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        histo[word] = histo.get(word, 0) + 1

hist = process_file('emma.txt')
print(hist)


# The function `process_file` process one-by-one the lines of the file, and passes them to `process_line`. 
# 
# The histogram `hist` is used as an accumulator.
# 
# The function `process_line` replaces hyphens with spaces, by the `replace` function before splitting, via `split`, the line into a list of strings.
# 
# It traverses the list of words and uses `strip` and `lower` to remove punctuation and convert to lower case. 
# 
# Finally, `process_line` updates the histogram by creating a new item (word) or incrementing an existing one.
# 
# To count the total number of words in the file, we can add up the frequencies in the histogram.

# In[ ]:


def total_words(hist : Dict) -> int:
    """counts the total number of words in the dictionary and thus original file
    """
    
    return sum(hist.values())

print(total_words(hist))


# The number of different words is just the number of items in the dictionary.

# In[ ]:


def different_words(hist : Dict) -> int:
    """counts the number of distinct words in the dictionary and thus original file
    """
    
    return len(hist)

print(different_words(hist))


# ### Most Common Words
# 
# To find the most common words, we can make a list of tuples, where each tuple contains a word and its frequency, and sort it.

# In[ ]:


from typing import Tuple

def most_common(hist : Dict) -> List[Tuple]:
    """transforms the dictionary in a list and sorts the list on most values
    """
    frequencies = []
    
    for key, value in hist.items():
        frequencies.append((value, key))
        
    frequencies.sort(reverse=True)
    #frequencies.sort()
    
    return frequencies


# In each tuple, the frequency appears first, so the resulting list is sorted by frequency. 

# In[ ]:


frequencies = most_common(hist)
print('The most common words are:')

for freq, word in frequencies[:10]:
    print(word, freq, sep='\t')


# This code can be simplified using the key parameter of the sort function.
# 
# If you are curious,
# you can read about it at https://wiki.python.org/moin/HowTo/Sorting.

# ### Optional Parameters
# 
# We have seen built-in functions and methods that take optional arguments.
# 
# It is possible to write programmer-defined functions with optional arguments, too. 
# 
# The next cell contains a function that prints the most common words in a histogram.

# In[ ]:


def print_most_common(hist : Dict, num : int = 10) -> None:
    """prints the top of the most common words, default number is 10
    """
    t = most_common(hist)
    print('The most common words are:')
    
    for freq, word in t[:num]:
        print(word, freq, sep='\t')


# The first parameter is required; the second is optional. 
# 
# The default value of `num` is `10`.

# In[ ]:


print_most_common(hist, 5)


# `num` gets the default value, unless you provide a second argument.

# In[ ]:


print_most_common(hist, 20)


# `num` gets the value of the second argument instead. 
# 
# In other words, the optional argument overrides the default value.
# 
# If a function has both required and optional parameters, all the required parameters have to come first, followed by the optional ones.

# ### Random Words
# 
# To choose a random word from the histogram, the simplest algorithm is to build a list with multiple copies of each word, according to the observed frequency, and then choose from the list.

# In[ ]:


import random 

def random_word(hist : Dict) -> str:
    """chooses a random word from a dictionary
    """
    word_lst : List[str] = []
    
    for word, freq in hist.items():
        word_lst.extend([word] * freq) # the word is added to the list as often as the frequency
    
    print(len(word_lst))
    return random.choice(word_lst)

print(random_word(hist))

