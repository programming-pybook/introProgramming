#!/usr/bin/env python
# coding: utf-8

# # NumPy Arrays
# 
# This Jupyter Notebook is based on Chapter 2 of the book "Python Data Science Handbook" by Jake VanderPlas.

# _(c) 2021, Lina Ochoa Venegas, Eindhoven University of Technology_

# ## Table of Contents
# 
# * [1. Introduction](#introduction) 
# * [2. Create NumPy Arrays](#arrays)  
# * [3. Multidimensional Arrays](#multidimensional)  
# * [4. Array Attributes](#attributes)
# * [5. Indexing](#indexing)
# * [6. Slicing](#slicing)
# * [7. Masking](#masking)

# ## 1. Introduction <a class="anchor" id="introduction"></a>
# 
# NumPy stands for *Numerical Python*. It is a Python library that supports large multi-dimensional arrays. NumPy also offers mathematical functions designed to operate over this type of array. But why not use normal Python data types–such as lists or tuples? The main reason is that NumPy arrays are way more efficient when storing and manipulating large amounts of data. Why are they more efficient? Mainly, because NumPy arrays are fixed-type arrays, meaning that they can contain items of a specific type–contrary, to `list` structures that handle diverse types at the same type. This fixed-type array condition makes NumPy arrays less flexible but more efficient, placing them at the basis of the data science ecosystem in Python.

# To start using NumPy you need to add the following code.

# In[1]:


import numpy as np


# By convention, the `numpy` module is renamed to `np`, so your code is less verbose.

# ## 2. Create NumPy Arrays <a class="anchor" id="arrays"></a>
# 
# You can create NumPy arrays out from Python lists or from scratch.
# 
# ### NumPy Array from `list`
# When creating NumPy arrays out from Python lists you first need to create a Python list. For example, in the following cell, we create a Python list that contains prime numbers greater than 0 and less than 30.

# In[2]:


# Create Python list
primes: list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

print(type(primes))
primes


# We notice that all elements within the `primes` list are integers. Therefore, we can create a NumPy array with integer values out from this list.

# In[3]:


# Creat NummPy array out from Pyton list
np_primes: np.ndarray = np.array(primes)

print(type(np_primes))
np_primes


# If it happens that your list contains different types, NumPy will attempt to upcast them. For instance, the following list has both integers and float point numbers. Integers can then be upcasted to floats.

# In[4]:


scores: list = [10, 9.6, 4.3, 8, 7.1, 6.1, 8]
np_scores: np.ndarray = np.array(scores)
np_scores


# You can go further and specify the data type of the items in the array by using the `dtype` keyword parameters. NumPy has a set of predefined types such as `bool_` (for Booleans), `int_` (for integers), `float_` (for floating-point numbers), and `str_` (for strings). When creating arrays, NumPy's default type is `float_`. The whole list of types can be found [here](https://numpy.org/doc/stable/reference/arrays.scalars.html#built-in-scalar-types).
# 
# In the following cell, we take the list of integers `scale`, and we convert it into a NumPy array with floating-point numbers.

# In[5]:


scale: list = [1, 2, 3, 4, 5]
np_scale: np.ndarray = np.array(scale, dtype='float_')
np_scale


# ### NumPy Array from Scratch
# 
# When dealing with large arrays it is better to create them from scratch instead of using Python lists. To do so, you can use diverse built-in functions provided by NumPy.
# 
# For instance, you can use the `zeros()` function, which creates an array with `n` number of zeros. In the following cell, we create an array with `8` zeros. Notice that by default the numbers are created as floats. If you want to change the type you can also use the `dtype` keyword.

# In[6]:


# Create an array with 8 zeros
zeros: np.ndarray = np.zeros(8)
zeros


# The `ones()` function works similar to the `zeros()` one, the only difference is that it creates `1`s instead of `0`s.

# In[7]:


ones: np.ndarray = np.ones(8, dtype='int')
ones


# You can also pick a specific number to fill in your array using the `full()` function. Look into the following cell. The first parameter of the function receives the number of items of the array; while the second parameter gets the value that should be copied in each location of the array.

# In[8]:


pi_numbers: np.ndarray = np.full(8, 3.1418)
pi_numbers


# ## 3. Multi-dimensional Arrays <a class="anchor" id="multidimensional"></a>
# 
# NumPy also supports the creation of multi-dimensional arrays (or matrices). The previous example can be altered, so we can define the number of rows and columns that our array will have. If both the numbers of rows and columns are greater than 1, we will end up with a multi-dimensional array.
# 
# For instance, in the following cell, we use again the `full()` function to create the `pi_matrix`, which consists of 4 rows and 8 columns. Therefore, instead of passing an integer as the first argument, we pass a tuple whose first item is the number of **rows** (i.e. `4`) and the number of **columns** (i.e. `8`).

# In[9]:


pi_matrix: np.ndarray = np.full((4, 8), 3.1418)
pi_matrix


# You can also create an array out of regular Python nested lists: inner lists become rows in the matrix.

# In[10]:


nested_lists: list = [list(range(i, i + 3)) for i in [1, 4, 7]]
print(nested_lists)

np.array(nested_lists)


# Some other interesting functions for creating multi-dimensional arrays include:
# - `arange()`: creates a linear sequences. It is similar to the `range()` function.

# In[11]:


# Creates a linear sequence between 0 and 10. It steps by 2.
np.arange(0, 10, 2)


# - `linspace()`: creates an array of evenly spaced numbers.

# In[12]:


# Creates an array of 5 items, evenly spaced between 0 and 1.
np.linspace(0, 1, 5)


# - `random.random()`: creates an array with random numbers between 0 and 1.

# In[13]:


# Creates a matrix (3 rows and 4 columns) with random numbers between 0 and 1.
np.random.random((3, 4))


# - `random.randint()`: creates an array with random integers in a given interval.

# In[14]:


# Creates a 4x4 matrix with random integers between 0 and 100
np.random.randint(0, 100, (4, 4))


# - `random.normal()`: creates a normally distributed array with random numbers. You must set the mean and the standard deviation values.

# In[15]:


# Creates a normally distributed 4x4 matrix with random numbers. 
# The mean is set to 0 and the standard deviation to 1.
np.random.normal(0, 1, (4, 4))


# ## 4. Array Attributes <a class="anchor" id="attributes"></a>
# 
# Every NumPy array has the following set of attributes:
# 
# | Attribute | Description |
# |-----------|-------------|
# | `ndim` | Number of dimensions |
# | `shape` | Size of each dimension |
# | `size` | Number of elements in the array |
# | `dtype` | Data type of the array |
# | `itemsize` | Size in bytes of each array element |
# | `nbytes` | Size in bytes of the array |
# 
# Hereafter, we will create three different arrays (one-dimensional, two-dimensional, and three-dimensional arrays) to see the output of these attributes.

# In[16]:


# One-dimensional array
one_dim: np.ndarray = np.random.randint(10, size=6)
one_dim


# In[17]:


# Two-dimensional array
two_dim: np.ndarray = np.random.randint(10, size=(2, 6))
two_dim


# In[18]:


# Three-dimensional array
three_dim: np.ndarray = np.random.randint(10, size=(2, 3, 6))
three_dim


# Let us explore now the `ndim`, `shape`, and `size` attributes.

# In[19]:


print(f'One-dimensional array: ndim={one_dim.ndim}, shape={one_dim.shape}, size={one_dim.size}')
print(f'Two-dimensional array: ndim={two_dim.ndim}, shape={two_dim.shape}, size={two_dim.size}')
print(f'Three-dimensional array: ndim={three_dim.ndim}, shape={three_dim.shape}, size={three_dim.size}')


# What about the `dtype`?

# In[20]:


print(f'One-dimensional array: dtype={one_dim.dtype}')
print(f'Two-dimensional array: dtype={two_dim.dtype}')
print(f'Three-dimensional array: dtype={three_dim.dtype}')


# The `int64` data type refers to a signed integer (can be both positive or negative) that uses 64 bits for its representation.
# 
# Finally, let us look into the `itemsize` and `nbytes` attributes. Notice that `nbytes` is equal to $itemsize \times size$.

# In[21]:


print(f'One-dimensional array: itemsize={one_dim.itemsize} bytes, nbytes={one_dim.nbytes} bytes')
print(f'Two-dimensional array: itemsize={two_dim.itemsize} bytes, nbytes={two_dim.nbytes} bytes')
print(f'Three-dimensional array: itemsize={three_dim.itemsize} bytes, nbytes={three_dim.nbytes} bytes')


# ## 5. Indexing <a class="anchor" id="indexing"></a>
# 
# Indexing in NumPy arrays is pretty similar to Python list indexing. Actually, when dealing with one-dimensional arrays there is no difference at all. To see this, let us redefine and use the `primes` array–now as a NumPy array.

# In[22]:


primes: list = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
primes


# If we want to access the first element in the array, we can use the `0` value between the squared brackets.

# In[23]:


primes[0]


# To access, the last item in the array, we refer to the length of the array minus one position. Otherwise, we will get an out-of-bounds index error.

# In[24]:


primes[len(primes) - 1]


# We can also opt for accessing items backwards by using negative indices. For instance, if we want to access the last item in the array, we can employ the `-1` index.

# In[25]:


primes[-1]


# When dealing with **multi-dimensional arrays**, you need to specify a comma-separated sequence of indices. To see how it works, let us create the `integers` two-dimensional array.

# In[26]:


integers: np.ndarray = np.array([list(range(i, i + 3)) for i in [1, 4, 7]])
integers


# If we want to access the item located in the first row of the matrix, second column (i.e. `2`), we use the `[0, 1]` index (remember that we start counting from 0).

# In[27]:


integers[0, 1]


# To access the element placed at the middle of the `integers` matrix (i.e. `5`), we can find the middle point of each dimension as follows. (Notice that the following code will only work for a matrix whose dimension sizes are both odd!)

# In[28]:


rows, columns = integers.shape
middle_rows: int = rows // 2
middle_columns: int = columns // 2
    
print(f'Middle index rows: {middle_rows}, Middle index columns: {middle_columns}')

integers[middle_rows, middle_columns]


# Finally, to access the last item in the two-dimensional array–that is, the element in the bottom-right corner (i.e. `9`), we can consider the size of each element and subtract `1` unit to each one of them. Then we use these new values as part of the sequence of indices.

# In[29]:


rows, columns = integers.shape
last_rows: int = rows - 1
last_columns: int = columns - 1
    
print(f'Last index rows: {last_rows}, Last index columns: {last_columns}')

integers[last_rows, last_columns]


# NumPy arrays are mutable, meaning that you can directly modify their values. In the following cell, we modify the first element of the matrix `integers`.

# In[30]:


integers[0, 0] = 100
integers


# ## 6. Slicing <a class="anchor" id="slicing"></a>
# 
# Array slicing also works like the regular slicing of Python lists. That is, we use the squared brackets (`[]`) and the colon symbol (`:`) to play around and choose the items we are interested in. The regular slicing notation looks as follows:
# 
# `x[start:stop]`
# 
# However, there is one extra attribute you can define when slicing (this also applies to other Python sequences such as lists and strings): the `step`, which only considers every $n^{th}$ item in the sequence–being $n$ the value you assign to it. Notice that the last colon and attribute are always optional in Python.
# 
# `x[start:stop:step]`
# 
# If you do not specify a value for any of these three attributes, they will get their default value. All default values are shown in the following table.
# 
# | Attribute | Default value |
# |:---------:|:-------------:|
# | `start`   | `0` |
# | `stop`    | Size of dimension |
# | `step`    | `1` |

# ### One-dimensional Array
# 
# Now, let us go back to our `primes` array and let us slice it in different ways.

# In[31]:


primes: np.ndarray = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
primes


# In the following cell, we only consider the first five items of the `primes` array. Notice that the element placed at the 5$^{th}$ position won't be included.

# In[32]:


first_five: np.ndarray = primes[:5]
first_five


# Computing the middle point manually might be error-prone. We can, therefore, compute the index in an integer variable (a.k.a. `middle`), and use it to define where half of the array starts. In the following cell, we consider all items placed in the second half of the array.

# In[33]:


middle: int = len(primes) // 2 
last_half: np.ndarray = primes[middle:]
last_half


# In the following cell, we specify both the `start` and `stop` attributes to take the two middle values of the array.

# In[34]:


two_middle: np.ndarray = primes[4:6]
two_middle


# Finally, we can start using the `step` attribute. If we set it to `2` without specifying any other value for the `start` and `stop` attributes, we will get every two elements from the array.

# In[35]:


every_two: np.ndarray = primes[::2]
every_two


# We can go further and decide to consider every two elements only in the last half of the array.

# In[36]:


middle: int = len(primes) // 2 
every_two_half: np.ndarray = primes[middle::2]
every_two_half


# ### Multi-dimensional Arrays
# 
# Slicing works similarly when dealing with multi-dimensional arrays. You only need to separate every slicing criterion for each dimension with a `comma`.
# 
# `x[start_dim1:stop_dim1:step_dim1, start_dim2:stop_dim2:step_dim2, ...]`
# 
# Let us have a look at the `integers` matrix.

# In[37]:


integers: np.ndarray = np.array([list(range(i, i + 3)) for i in [1, 4, 7]])
integers


# In[38]:


# Pick first two rows and first two columns
integers[:2, :2]


# In[39]:


# Pick last two rows and last two columns
integers[1:, 1:]


# In[40]:


# Pick all rows and column in position 2 (last column)
integers[:, 2]


# In[41]:


# Pick first row and all columns
integers[0, :]


# In[42]:


# Pick first row and all columns (another way)
integers[0]


# In[43]:


# Pick all rows and every two steps pick a column
integers[:, ::2]


# ### Copies of Arrays
# 
# A difference of foremost importance between NumPy arrays and Python lists is that array slices return **views** instead of **copies** of the data. This means that if you modify the array slices you are actually modifying the underlying data. This property is very useful especially when dealing with large datasets: we can focus on the data we need to modify and there is no need to handle extra copies. 

# In[44]:


sub_integers: np.ndarray = integers[:2, :2]
sub_integers


# In[45]:


# Change the first value of the view
sub_integers[0, 0] = 100
sub_integers


# In[46]:


# the integers matrix has been also updated
integers


# However, the *views* property comes at a cost: if you just wanted to experiment with your data without really aiming at modifying it, you can end up with a polluted dataset. If you prefer to work with a copy, you need to be explicit about it. Luckily, NumPy provides the method `copy()`, which will help you in this regard.

# In[47]:


integers: np.ndarray = np.array([list(range(i, i + 3)) for i in [1, 4, 7]])
integers


# In[48]:


# Create a copy instead
sub_integers: np.ndarray = integers[:2, :2].copy()
sub_integers


# In[49]:


# Update first item of the copy
sub_integers[0, 0] = 100
sub_integers


# In[50]:


# The integers matrix is intact
integers


# ## 7. Masking
# 
# We can use Boolean arrays to mask (or filter) values in the array. Suppose that we would like to get all values from the `integers` array that are greater than or equal to 5. Let us first create the Boolean array and see how it looks like.

# In[51]:


integers >= 5


# You can see that NumPy checks the Boolean expression against all values in the array, then it creates a new NumPy array with Boolean values stating if the condition is satisfied by the item in a given position.
# 
# Now, if we want to mask the `integers` array and consider the subset of data points that are greater than or equal to 5, we need to use the Boolean array to index on the boolean condition.

# In[52]:


integers[integers >= 5]


# Notice that NumPy returns a one-dimensional array with all the values that meet the condition.
