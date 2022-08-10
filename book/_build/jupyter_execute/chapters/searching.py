#!/usr/bin/env python
# coding: utf-8

# # Searching [^intro]
# 
# This Jupyter Notebook is based on external content related to algorithms (e.g. searching and sorting).

# _(c) 2021, Mark van den Brand, Eindhoven University of Technology_

# ## Table of Contents
# <div class="toc" style="margin-top: 1em;">
#     <ul class="toc-item">
#         <li>
#             <span><a href="#1.-Searching-for-Two-Largest-Values-in-a-List" data-toc-modified-id="1.-Searching-for-Two-Largest-Values-in-a-List">1. Searching for Two Largest Values in a List</a></span>
#         </li>
#         <li>
#             <span><a href="#2.-Timing-the-Functions" data-toc-modified-id="2.-Timing-the-Functions">2. Timing the Functions</a></span>
#         </li>
#         <li>
#             <span><a href="#3.-Searching" data-toc-modified-id="3.-Searching">3. Searching</a></span>
#         </li>
#     </ul>
# </div>

# ## 1. Searching for Two Largest Values in a List
# 
# Based on Chapter 11 of the book *Practical Programming* by P. Gries, J. Campbell, and J. Montojo.
# 
# Suppose we have the following list of data, for instance representing the number of seals treated in the Sealcentre in Pieterburen (NL).
# 
# 334 468 549 836 660 389 308 392 520 271
# 
# The first number, 334, represents the number of seals treated in 2009 and the last number, 271, the number of seals treated in 2018.
# 
# We start with a simpler problem, what is the highest number, and we can use the `list.index` to find the corresponding index.

# In[1]:


counts = [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
high = max(counts)
counts.index(high)


# Or, more concise:
# 

# In[2]:


counts = [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
counts.index(max(counts))


# Now, suppose we want to find the indexes of the 2 highest amounts. There is no direct method to do so.
# 
# We will present three alternative algorithms:
# 1. *Find, remove, find*: first find the index for highest amount, remove highest amount and then look for the index of the next highest amount. Insert the highest amount back, and adapt the second index if needed.
# 2. *Sort*: copy the list, and sort, and use the two highest amounts to find the corresponding indices in the original list.
# 3. *Walk through the list* and keep track of the two highest amounts found so far, update if a higher amount is found.
# 
# The ultimate question is of course which *one is the fastest solution*?

# ### Find, Remove, Find

# In[3]:


from typing import List, Tuple

def find_two_highest_remove(amounts : List[int]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two highest values in list amounts.
    >>> seals = [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    >>> find_two_highest_remove(seals)
    (3, 4)
    >>> seals == [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    True
    """
    # Find the index of the maximum in seals
    # Remove that item form the list
    # Find the index of the new maximum in the list
    # Put the highest item back in the list
    # If necessary, adjust the second index
    # Return the two indices


# As we have seen `max` and `list.index` do the for finding the index of the highest amount.

# In[4]:


from typing import List, Tuple

def find_two_highest_remove(amounts : List[int]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two highest values in list amounts.
    >>> seals = [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    >>> find_two_highest_remove(seals)
    (3, 4)
    >>> seals == [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    True
    """
    # Find the index of the maximum in seals
    highest : int = max(amounts)
    high_index1 : int = amounts.index(highest)
    # Remove that item form the list
    amounts.remove(highest)
#    print(high_index1)
    
    # Find the index of the new maximum in the list
    next_highest : int = max(amounts)
    high_index2 : int = amounts.index(next_highest)
#    print(high_index2)
    
    # Put the highest item back in the list
    # If necessary, adjust the second index
    # Return the two indices
    
find_two_highest_remove([334, 468, 549, 836, 660, 389, 308, 392, 520, 271])


# Since we removed the highest amount, we have to put it back and if necessary adapt the index of the second-highest amount, if the highest amount was before the second-highest amount in the list.

# In[5]:


from typing import List, Tuple

def find_two_highest_remove(amounts : List[int]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two highest values in list amounts.
    >>> seals = [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    >>> find_two_highest_remove(seals)
    (3, 4)
    >>> seals == [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    True
    """
    # Find the index of the maximum in seals
    highest : int = max(amounts)
    high_index1 : int = amounts.index(highest)
    # Remove that item form the list
    amounts.remove(highest)
    
    # Find the index of the new maximum in the list
    next_highest : int = max(amounts)
    high_index2 : int = amounts.index(next_highest)
    
    # Put the highest item back in the list
    amounts.insert(high_index1, highest)
    
    # If necessary, adjust the second index
    if high_index1 <= high_index2:
        high_index2 += 1
        
    # Return the two indices
    return (high_index1, high_index2)

find_two_highest_remove([334, 468, 549, 836, 660, 389, 308, 392, 520, 271])


# In[6]:


import doctest
doctest.testmod(verbose=True)  # with details


# <div class="alert alert-success">
#     <b>Do It Yourself!</b><br>
#     Create the function <i>find_two_lowest_remove</i>, which finds the indexes of the 2 lowest numbers of a list of integers received as parameter. Use the <b>find, remove, find</b> algorithm to compute the expected output. 
# </div>

# In[7]:


# Remove this line and add your code here


# ### Sort
# 
# In the next cell you will find the refined algorithm based on sorting.

# In[8]:


from typing import List, Tuple

def find_two_highest_sort(amounts : List[int]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two highest values in list amounts.
    >>> seals = [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    >>> find_two_highest_sort(seals)
    (3, 4)
    >>> seals == [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    True
    """
    # Sort a copy of amounts
    # Get the two highest values
    # Find their indices in the original list
    # Return the two indices


# We have to refine the sorting and obtaining the index. Note that we sort the list in reverse order!

# In[9]:


from typing import List, Tuple

def find_two_highest_sort(amounts : List[int]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two highest values in list amounts.
    >>> seals = [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    >>> find_two_highest_sort(seals)
    (3, 4)
    >>> seals == [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    True
    """
    # Sort a copy of amounts
    temp_amounts : List[int] = sorted(amounts, reverse = True)
    print(temp_amounts)
    # Get the two highest values
    highest : int = temp_amounts[0]
    next_highest : int = temp_amounts[1]
    print(highest)
    print(next_highest)
    
    # Find their indices in the original list
    # Return the two indices
    
find_two_highest_sort([334, 468, 549, 836, 660, 389, 308, 392, 520, 271])


# We need to find the indices for both values in the original list.

# In[10]:


from typing import List, Tuple

def find_two_highest_sort(amounts : List[int]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two highest values in list amounts.
    >>> seals = [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    >>> find_two_highest_sort(seals)
    (3, 4)
    >>> seals == [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    True
    """
    # Sort a copy of amounts
    temp_amounts : List[int] = sorted(amounts, reverse = True)

    # Get the two highest values
    highest : int = temp_amounts[0]
    next_highest : int = temp_amounts[1]
    
    # Find their indices in the original list
    high_index1 : int = amounts.index(highest)
    high_index2 : int = amounts.index(next_highest)
    
    # Return the two indices
    return (high_index1, high_index2)

find_two_highest_sort([334, 468, 549, 836, 660, 389, 308, 392, 520, 271])


# In[11]:


doctest.testmod(verbose=True)  # with details


# <div class="alert alert-success">
#     <b>Do It Yourself!</b><br>
#     Create the function <i>find_two_lowest_sort</i>, which finds the indexes of the 2 lowest numbers of a list of integers received as parameter. Use the <b>sort</b> algorithm to compute the expected output. 
# </div>

# In[12]:


# Remove this line and add your code here


# ### Walk through the list
# 
# In the next cell you will find the refined algorithm where walk over the list to find the highest two values.

# In[13]:


from typing import List, Tuple

def find_two_highest_walk(amounts : List[int]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two highest values in list amounts.
    >>> seals = [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    >>> find_two_highest_walk(seals)
    (3, 4)
    >>> seals == [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    True
    """

    # Examine each value in the list in order
    # Keep track of the indices of the two highest values found so far
    # Update the indices when a new higher value is found
    # Return the two indices


# We start with swapping the first and second line of the refinement steps. Furthermore, the updating of the indices is a step in the loop.

# In[14]:


from typing import List, Tuple

def find_two_highest_walk(amounts : List[int]) -> Tuple[int, int]:
    """Return a tuple of the indices of the tow highest values in list amounts.
    >>> seals = [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    >>> find_two_highest_walk(seals)
    (3, 4)
    >>> seals == [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    True
    """

    # Keep track of the indices of the two highest values found so far
    # Examine each value in the list in order
    #     Update the indices when a new higher value is found
    # Return the two indices 


# In[15]:


from typing import List, Tuple

def find_two_highest_walk(amounts : List[int]) -> Tuple[int, int]:
    """Return a tuple of the indices of the tow highest values in list amounts.
    >>> seals = [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    >>> find_two_highest_walk(seals)
    (3, 4)
    >>> seals == [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    True
    """

    # Keep track of the indices of the two highest values found so far
    if amounts[0] > amounts[1]:
        high_index1, high_index2 = 0, 1
    else:
        high_index1, high_index2 = 1, 0
        
    # Examine each value in the list in order
    #     Update the indices when a new higher value is found
    # Return the two indices 


# We will now use a for loop over the indices, because we are interested in the indices and not in the values themselves.
# 
# There are alternative solutions, like using a while loop or a for loop to iterate over the values.

# In[16]:


from typing import List, Tuple

def find_two_highest_walk(amounts : List[int]) -> Tuple[int, int]:
    """Return a tuple of the indices of the tow highest values in list amounts.
    >>> seals = [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    >>> find_two_highest_walk(seals)
    (3, 4)
    >>> seals == [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    True
    """

    # Keep track of the indices of the two highest values found so far
    if amounts[0] > amounts[1]:
        high_index1, high_index2 = 0, 1
    else:
        high_index1, high_index2 = 1, 0
        
    # Examine each value in the list in order
    for i in range(2, len(amounts)):
    #     Update the indices when a new higher value is found
    # Return the two indices   


# We need to update the indices if the value at the current index is higher than one of the current values.
# 
# 1. We have to update both indices if the value at the current index is higher than the highest values seen so far. In this case both indices have to be updated
# 2. The value at the current index is between the both highest values seen so far. Only the index of the lowest highest values has to be updated.
# 3. The value at the current index is lower than the highest values seen so far. Nothing needs to be done.

# In[ ]:


from typing import List, Tuple

def find_two_highest_walk(amounts : List[int]) -> Tuple[int, int]:
    """Return a tuple of the indices of the tow highest values in list amounts.
    >>> seals = [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    >>> find_two_highest_walk(seals)
    (3, 4)
    >>> seals == [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    True
    """

    # Keep track of the indices of the two highest values found so far
    if amounts[0] > amounts[1]:
        high_index1, high_index2 = 0, 1
    else:
        high_index1, high_index2 = 1, 0
        
    # Examine each value in the list in order
    for i in range(2, len(amounts)):
    #     Update the indices when a new higher value is found
        if amounts[i] > amounts[high_index1]:
            high_index2 = high_index1
            high_index1 = i
        elif amounts[i] > amounts[high_index2]:
            high_index2 = i
        
    # Return the two indices 
    return (high_index1, high_index2)

find_two_highest_walk([334, 468, 549, 836, 660, 389, 308, 392, 520, 271])


# In[ ]:


doctest.testmod(verbose=True)  # with details


# <div class="alert alert-success">
#     <b>Do It Yourself!</b><br>
#     Create the function <i>find_two_lowest_walk</i>, which finds the indexes of the 2 lowest numbers of a list of integers received as parameter. Use the <b>walk through the list</b> algorithm to compute the expected output. 
# </div>

# In[ ]:


# Remove this line and add your code here


# ## 2. Timing the Functions
# 
# First we are going to generate a huge list of arbitrary unique numbers.

# In[ ]:


import random
from typing import List

i : int = 0
rdlst : List[int] = []
    
while i < 80000:
    rdnr : int = random.randint(0,1000000)
    if rdnr not in rdlst:
        rdlst = rdlst + [rdnr]
    i += 1
    
#print(rdlst)


# Via profiling you get insight in the efficiency of your code.

# In[ ]:


import time

t1 = time.perf_counter()
#find_two_highest_remove([334, 468, 549, 836, 660, 389, 308, 392, 520, 271])
find_two_highest_remove(rdlst)
t2 = time.perf_counter()
print("The remove code took {:.2f}ms".format((t2 - t1) * 1000))

t1 = time.perf_counter()
#find_two_highest_sort([334, 468, 549, 836, 660, 389, 308, 392, 520, 271])
find_two_highest_sort(rdlst)
t2 = time.perf_counter()
print("The sort code took {:.2f}ms".format((t2 - t1) * 1000))

t1 = time.perf_counter()
#find_two_highest_walk([334, 468, 549, 836, 660, 389, 308, 392, 520, 271])
find_two_highest_walk(rdlst)
t2 = time.perf_counter()
print("The walk code took {:.2f}ms".format((t2 - t1) * 1000))


# <div class="alert alert-success">
#     <b>Do It Yourself!</b><br>
#     Report the time taken by each of the three functions to return the indices of the lowest numbers of the list of integers.
# </div>

# In[ ]:


# Remove this line and add your code here


# ## 3. Searching
# 
# Searching elements in a list is a frequently used operation, as we saw in the cells above. In these cells we use the built-in method `index` on lists. 
# 
# We are going to present a number of different search algorithms for unsorted lists, eventually we will produce a more efficient algorithm if the list elements are sorted.

# ### Linear Search
# 
# Linear search starts with the index `0` and looks at each list item one by one, in order to see whether the element at the given index is the element we are looking for?
# 
# We will give two variants, each of the variants uses a loop.

# In[ ]:


from typing import Any

def linear_search(lst : list, value : Any) -> int:
    """Return the index of the first occurrence of value in lst,
    return -1 if value is not in lst.
    
    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    0
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)
    -1
    """
    
    # Examine the items at each index i in lst, starting at index 0
    # Is lst[i] the value we are looking for? If so, stop searching. 


# We will first present a solution using a while-loop and an auxilary variable representing the index.

# In[ ]:


from typing import Any

def linear_search(lst : list, value : Any) -> int:
    """Return the index of the first occurrence of value in lst,
    return -1 if value is not in lst.
    
    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    0
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)
    -1
    """
    
    # Start at index 0
    i : int = 0
    # Examine the items at each index i in lst
    # Is lst[i] the value we are looking for? If so, stop searching. 
    while i != len(lst) and lst[i] != value:
        i += 1
        
    # If we have inspected all elements
    if i == len(lst):
        return -1
    else:
        return i


# In[ ]:


import doctest

doctest.testmod(verbose=True)  # with details


# The next solution present uses a for-loop and an auxilary variable representing the index.

# In[ ]:


from typing import Any

def linear_search(lst : list, value : Any) -> int:
    """Return the index of the first occurrence of value in lst,
    return -1 if value is not in lst.
    
    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    0
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)
    -1
    """
    
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


# In[ ]:


doctest.testmod(verbose=True)  # with details


# Suppose the list is sorted, would you use the same search function?

# ### Binary Search
# 
# Binary search is only applicable if the elements in the list are sorted. The basic idea of binary search is the find the middle of the list, compare the value with the middle element, if the two are the equal, then the index of the middle element is returned. Otherwise two options are possible, the value is smaller the middle element then the search is continued in the first half, else the search is continued in the second half.
# 
# The advantage is that the number of steps to find the index in a list with 1.000.000 is about 20!

# In[ ]:


from typing import Any

def binary_search(lst : list, value : Any) -> int:
    """ Return the index of the first occurrence of the value in lst, 
    or return -1 if the value is not found in lst.
    
    >>> binary_search([1, 2, 4, 4, 5, 7, 9, 10], 1)
    0
    >>> binary_search([1, 2, 4, 4, 5, 7, 9, 10], 4)
    2
    >>> binary_search([1, 2, 4, 4, 5, 7, 9, 10], 5)
    4
    >>> binary_search([1, 2, 4, 4, 5, 7, 9, 10], 10)
    7
    >>> binary_search([1, 2, 4, 4, 5, 7, 9, 10], -3)
    -1
    >>> binary_search([1, 2, 4, 4, 5, 7, 9, 10], 11)
    -1
    >>> binary_search([1, 2, 4, 4, 5, 7, 9, 10], 3)
    -1
    >>> binary_search([], -3)
    -1
    >>> binary_search([1], 1)
    0
    """
    
    # Mark the left and right indices of the part of the list to be searched
    i : int = 0
    j : int = len(lst) - 1
    
    while i != j + 1:
        m = (i + j) // 2
        if lst[m] < value:
            i = m + 1
        else:
            j = m - 1
    
    if 0 <= i < len(lst) and lst[i] == value:
        return i
    else:
        return -1

    
binary_search([1, 2, 4, 4, 5, 7, 9, 10, 12, 15, 
               20, 20, 25, 33, 33, 44, 55, 60, 
               61, 62, 64, 67, 70, 73, 76, 78], 55)


# In[ ]:


import doctest

doctest.testmod(verbose=True)  # with details


# There are a lot of test cases because the test cases cover:
# * The value is the first item.
# * The value occurs twice, we want the index of the first occurrence.
# * The value is exactly in the middle of the list.
# * The value is the last item of the list.
# * The value is smaller than all elements in the list.
# * The value is larger than all elements in the list.
# * The value is not in the list, but is larger than some but smaller than others.
# * The list has no items.
# * The list has exactly one item.

# <div class="alert alert-success">
#     <b>Do It Yourself!</b><br>
#     Use the linear and the binary search to find the word <i>done</i> in the list. Profile each function and compare the time taken by each one of them.
# </div>

# In[ ]:


lst = ['we', 'are', 'almost', 'done', 'with', 'the', 'course']

# Remove this line and add your code here


# Again some timing measurements.

# In[ ]:


import time

t1 = time.perf_counter()

idx1 : int = linear_search(rdlst, 202123)
t2 = time.perf_counter()
print("The linear search code took {:.2f}ms".format((t2 - t1) * 1000))
print(idx1)

rdlst.sort()

t1 = time.perf_counter()
idx2 : int = binary_search(rdlst, 202123)
t2 = time.perf_counter()
print("The binary search code took {:.2f}ms".format((t2 - t1) * 1000))
print(idx2)

