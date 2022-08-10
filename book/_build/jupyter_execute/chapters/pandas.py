#!/usr/bin/env python
# coding: utf-8

# # Pandas DataFrames
# 
# This Jupyter Notebook is based on Chapter 3 of the book "Python Data Science Handbook" by Jake VannderPlas.

# _(c) 2021, Lina Ochoa Venegas, Eindhoven University of Technology_

# ## Table of Contents
# 
# * [1. Introduction](#introduction) 
# * [2. The Series Object](#series)  
# * [3. The DataFrame Object](#dataframe)  
# * [4. The Index Object](#index)
# * [5. Indexing and Selection](#indexing)

# In[1]:


import numpy as np


# ## 1. Introduction <a class="anchor" id="introduction"></a>
# 
# Pandas is one of the most important data science-oriented libraries. It is built atop NumPy. One of its most important contributions is an efficient implementation of a data frame. A `DataFrame` is a multi-dimensional array (just as NumPy multi-dimensional arrays) with additional information (e.g. labels) and support for heterogeneous data (e.g. different types, missing data). Besides the `DataFrame` data type, Pandas also offers two other important structures, namely `Series` and `Index`. We will dive into these three different structures and some basic operations along with this chapter.

# To start using NumPy you need to add the following code.

# In[2]:


import pandas as pd


# By convention, the `pandas` module is renamed to `pd`, so your code is less verbose.

# ## 2. The `Series` Object <a class="anchor" id="series"></a>
# 
# A Pandas `Series` is a one-dimensional indexed array. It is like having the NumPy array but with an extra structure that saves the indices of the items in the array independently. Now, it does not mean that the NumPy array does not have an index–without it, we would not be able to access its items–; what it truly means is that the `Series` object handles the index in an independent and different way as of the one of the NumPy array.
# 
# A `Series` object can be created out from a sequence of values, a dictionary, or an array as follows. (The type of the items in the array–`dtype`–are printed after the `Series` object is printed.)

# In[3]:


# Create a Series object out from a Python sequence
vowels: pd.Series = pd.Series(['a', 'e', 'i', 'o', 'u'])
vowels


# In[4]:


# Create a Series object out from a Python dictionary
municipalities: dict = {
    'drenthe': 12,
    'flevoland': 6,
    'friesland': 18,
    'gelderland': 51,
    'groningen': 10,
    'limburg': 31,
    'noord-brabant': 61,
    'noord-holland': 47,
    'overijssel': 25,
    'zuid-holland': 52,
    'utrecht': 26,
    'zeeland': 13
}

provinces: pd.Series = pd.Series(municipalities)
provinces


# In[5]:


# Create a Series object out from a NumPy array
rand: pd.Series = pd.Series(np.random.random(8))
rand


# Notice that each value in the one-dimensional array is placed in front of an integer or string value. In the case of the `vowels` and `rand` variables, the integer values range between `0` and `n - 1`, where `n` is the number of items in the array. In the case of the `provinces` variable, we have string values representing the keys of the dictionary. The sequence of these values–in the three cases–is what we know as the index array of the `Series` object.
# 
# To access the values of the `Series` we can use the `values` attribute, and the `index` attribute to access the index array.

# In[6]:


# Access only the values of the Series object
vowels.values


# In[7]:


# Access the index array of the Series object
vowels.index


# Notice that the values of the `Series` object is a NumPy array!

# In[8]:


type(vowels.values)


# However, this is not the case with the index array. This value is in fact an object of the Pandas `Index` type.

# In[9]:


type(vowels.index)


# Moreover, to access specific items in the `Series` object or to slice it, you can proceed just as we do with NumPy arrays or Python lists.

# In[10]:


# Extract the 2nd item of the Series
vowels[2]


# In[11]:


# Slice the Series object
vowels[1:3]


# Going back to the explicit index capability of `Series` objects, we might ask ourselves: what is the actual difference with regards to NumPy indices? Due to the possibility of defining it independently, you can have indices that can be of other types different from integers (like with the `provinces` variable), which is not the case with Numpy arrays–they are always integers. You do not always need to specify the index of the `Series` object. When you avoid doing that you get an **implicit index**. When you specify the index array you get an **explicit index**. These terms will be useful when slicing (c.f. Section 5).
# 
# Let us have a look at the creation of another `Series` object with a string index.

# In[12]:


linear: pd.Series = pd.Series(np.linspace(0, 1, 5), index=['a', 'b', 'c', 'd', 'e'])
linear


# Notice that we use the `index` keyword to pass the sequence representing the index of the object. If you want to access the value `0.75`, you can refer to the corresponding index `d`.

# In[13]:


linear['d']


# You can also apply slicing to indices that are not integers. For instance, in the following cell, we want all the items that are in between `'b'` and `'d'`. In this case, Pandas will return all the observations that appear in-between–given the order of the observations.

# In[14]:


linear['b':'d']


# ## 3. The `DataFrame` Object <a class="anchor" id="dataframe"></a>
# 
# A `DataFrame` object is the equivalent of a two-dimensional array or a matrix with flexible column names and row indices. you can think of it as a sequence of `Series` objects (each one representing a column) that share the same index array. Let us have a look at this last property. To do so, we will consider the `municipalities` dictionary representing the number of municipalities per Dutch province presented in the previous section.

# In[15]:


municipalities: dict = {
    'drenthe': 12,
    'flevoland': 6,
    'friesland': 18,
    'gelderland': 51,
    'groningen': 10,
    'limburg': 31,
    'noord-brabant': 61,
    'noord-holland': 47,
    'overijssel': 25,
    'zuid-holland': 52,
    'utrecht': 26,
    'zeeland': 13
}
municipalities


# We will also create the `area` dictionary containing the total area of each province. Notice that both dictionaries share the same keys (the names of the 13 Dutch provinces).

# In[16]:


area: dict = {
    'drenthe': 2680,
    'flevoland': 2412,
    'friesland': 5749,
    'gelderland': 5136,
    'groningen': 2960,
    'limburg': 2210,
    'noord-brabant': 5082,
    'noord-holland': 4092,
    'overijssel': 3421,
    'zuid-holland': 3308,
    'utrecht': 1560,
    'zeeland': 2933
}
area


# Now, we will create two `Series` out of these dictionaries.

# In[17]:


# Create a Series out from the municipalities dictionary
municipalities_series: pd.Series = pd.Series(municipalities)
municipalities_series


# In[18]:


# Create a Series out from the area dictionary
area_series: pd.Series = pd.Series(area)
area_series


# Finally, to create our data frame, we will use the type constructor and we will pass a dictionary whose keys are the names of the matrix columns, and its values point to the two `Series` objects `municipalities_series` and `area_series`.

# In[19]:


data: dict = {
    'municipalities': municipalities_series, 
    'area': area_series
}
    
provinces: pd.DataFrame = pd.DataFrame(data)
provinces


# Just as with the `Series` objects, you can access the data frame index via the `index` attribute.

# In[20]:


provinces.index


# But also the columns of the data frame via the `columns` attribute.

# In[21]:


provinces.columns


# Notice that both objects are of type `Index`.

# ### Create `DataFrame` Objects
# 
# We have already seen some approaches to create a `DataFrame` object, however, there are some additional alternatives. We will list the most common ways of creating Pandas data frames hereafter:
# 
# * **From a `Series` object:** We already know that a `DataFrame` is a sequence of `Series` objects. You can create one starting from just *one* `Series` instance. Let us revisit our `municipalities_series` example. In this case, you pass the `Series` object and the name of the column to the initializer of the type.

# In[22]:


municipalities: dict = {
    'drenthe': 12,
    'flevoland': 6,
    'friesland': 18,
    'gelderland': 51,
    'groningen': 10,
    'limburg': 31,
    'noord-brabant': 61,
    'noord-holland': 47,
    'overijssel': 25,
    'zuid-holland': 52,
    'utrecht': 26,
    'zeeland': 13
}
    
# Create a Series out from the municipalities dictionary
municipalities_series: pd.Series = pd.Series(municipalities)
municipalities_series


# In[23]:


# Create the DataFrame object out from the municipalities_series
pd.DataFrame(municipalities_series, columns=['municipalities'])


# * **From a list of dictionaries:** Pandas aggregates all the keys from all the dictionaries and creates a column for each one of them. Each dictionary will represent a row or a case in the data frame. If a dictionary is missing information, it will fill in the position with a `NaN` (short for Not A Number) value. (Have a look at the missing values in `dict2` and `dict3`).

# In[24]:


import random as rd

dict1: dict = {'a': rd.randint(0, 100), 'b': rd.randint(0, 100), 'c': rd.randint(0, 100)}
dict2: dict = {'b': rd.randint(0, 100), 'c': rd.randint(0, 100)}
dict3: dict = {'a': rd.randint(0, 100), 'b': rd.randint(0, 100)}
    
pd.DataFrame([dict1, dict2, dict3])


# * **From a dictionary of `Series` objects:** We already covered this case when introducing the `provinces` data frame. Let us look at another example with random numbers. In this example, we create three `Series` objects with 5 random integers from 0 to 10 (`values_10`), 0 to 100 (`values_100`), and 0 to 1000 (`values_1000`). The indices we use in both cases are `'a'`, `'b'`, `'c'`, `'d'`, and `'e'`. 

# In[25]:


import random as rd

values_10: pd.Series = pd.Series([rd.randint(0, 10) for _ in range(5)], index=['a', 'b', 'c', 'd', 'e'])
values_100: pd.Series = pd.Series([rd.randint(0, 100) for _ in range(5)], index=['a', 'b', 'c', 'd', 'e'])
values_1000: pd.Series = pd.Series([rd.randint(0, 1000) for _ in range(5)], index=['a', 'b', 'c', 'd', 'e'])

pd.DataFrame({'values_10': values_10, 
              'values_100': values_100,
              'values_1000': values_1000})


# * **From a NumPy array:** We can also create a `DataFrame` object out from a NumPy array as follows.

# In[26]:


pd.DataFrame(np.random.randint(0, 100, (4, 3)),
            columns=['apples', 'bananas', 'pears'],
            index=['A', 'B', 'C', 'D'])


# ## 4. The `Index` Object <a class="anchor" id="index"></a>
# 
# We already discovered that both the `Series` and `DataFrame` objects have a special attribute that stores the index array. This array is of type `Index`, and it is also offered by the Pandas library. The `Index` type is an immutable array that might contain repeated values. It behaves pretty much like a NumPy array, the main difference between both data structures is that `Index` objects are immutable. 
# 
# Additionally, you can create your own `Index` object without creating a `Series` or `DataFrame` object first. To do so, you can pass a sequence of values as the argument of the initializer method.

# In[27]:


ind: pd.Index = pd.Index([1, 3, 5, 7, 9])
ind


# You can use Python lists indexing and slicing capabilities to interact with the `Index` object values.

# In[28]:


# Access index located at the 2nd position
ind[2]


# In[29]:


# Slice the array: every two steps take an element starting from position 1
ind[1::2]


# However, if you try to modify an element within the array you will get an error–recall that `Index` objects are immutable.

# In[30]:


ind[3] = 100


# `Index` objects count with attributes similar to the ones offered by NumPy arrays such as `size`, `shape`, `ndim`, and `dtype`.

# In[ ]:


# Get the Index object size
ind.size


# In[ ]:


# Get the Index object shape
ind.shape


# In[ ]:


# Get the Index object ndim (number of dimensions)
ind.ndim


# In[ ]:


# Get the Index object dtype (data type)
ind.dtype


# ## 5. Indexing and Selection <a class="anchor" id="indexing"></a>
# 
# ### In `Series` Objects
# 
# `Series` objects work very similarly to both NumPy arrays and Python dictionaries, that is why they provide the same mechanisms to select a subset of data. On the one hand, when seen as one-dimensional NumPy arrays, `Series` objects can be sliced and masked.
# Let us create again a `Series` object with random numbers (from 0 to 1).

# In[ ]:


# Create a Series object with random numbers
rand: pd.Series = pd.Series(np.random.random(8))
rand


# In[ ]:


# Slice the Series object: every two steps take an element starting from index 1 and ending at index 6
rand[1:6:2]


# In[ ]:


# Alternative to the previous code using a negative index
rand[1:-1:2]


# Let us recall how it works when dealing with non-integer indices.

# In[ ]:


# Create a Series object with random numbers
rand: pd.Series = pd.Series(np.random.random(5), index=['a', 'b', 'c', 'd', 'e'])
rand


# In[ ]:


# Get all items between 'b' and 'e'
rand['b':'e']


# In[ ]:


# Same as the previous cell but with the step value
rand['b':'e':2]


# Notice that when we employ the *explicit* index (the `['a', 'b', 'c', 'd', 'e']`) we do **include** the last item, while when using the *implicit* one the final index is **excluded**. Be careful when using one or the other!
# 
# We can also mask our data in the same way we did with NumPy.

# In[ ]:


# Take all the values that are greater than 0.25 and smaller than 0.75
rand[(rand > 0.25) & (rand < 0.75)]


# The use of explicit and implicit integer indices can cause additional confusion. Let us have a look at the following example. We create the `linear` `Series` object, this time with an explicit integer index.

# In[ ]:


linear: pd.Series = pd.Series(np.linspace(0, 1, 5), index=[1, 3, 5, 7, 9])
linear


# What value will the following expression yield: `linear[1]`?

# In[ ]:


linear[1]


# Instead of displaying the value at *implicit* index 1 (counting from 0 to 4), it will display the value at *explicit* index 1 (for the index array `[1, 3, 5, 7, 9]`). But what will it happen if we try the next slicing expression: `linear[1:3]`?

# In[ ]:


linear[1:3]


# This time, Pandas will use the *implicit* index to produce the slice! Indeed confusing!
# 
# To avoid these confusing behaviour, Pandas provide the so-called **indexer** attributes, that make explicit the indexing scheme to be used. There are two possible indexers: 
# 
# * **`loc`:** indexing and slicing will always refer to the *explicit index*.
# * **`iloc`:** indexing and slicing will always refer to the *implicit index*.

# In[ ]:


# Indexing with loc
linear.loc[1]


# In[ ]:


# Slicing with loc
linear.loc[1:3]


# In[ ]:


# Indexing with loc
linear.iloc[1]


# In[ ]:


# Slicing with loc
linear.iloc[1:3]


# "The Zen of Python" guidelines mention that "explicit is better than implicit", so it is highly recommended to always use the `loc` or `iloc` indexer instead of just going for the default hybrid behaviour!

# ### In `DataFrame` Objects
# 
# When selecting data from a `DataFrame` object, we can follow the dictionary-style indexing that indexes based on the column name. This type of indexing will retrieve the whole column in the form of a `Series` object. To see it, let us go back to the Dutch `provinces` data frame.

# In[ ]:


# Get the data as dictionaries
municipalities: dict = {
    'drenthe': 12,
    'flevoland': 6,
    'friesland': 18,
    'gelderland': 51,
    'groningen': 10,
    'limburg': 31,
    'noord-brabant': 61,
    'noord-holland': 47,
    'overijssel': 25,
    'zuid-holland': 52,
    'utrecht': 26,
    'zeeland': 13
}
    
area: dict = {
    'drenthe': 2680,
    'flevoland': 2412,
    'friesland': 5749,
    'gelderland': 5136,
    'groningen': 2960,
    'limburg': 2210,
    'noord-brabant': 5082,
    'noord-holland': 4092,
    'overijssel': 3421,
    'zuid-holland': 3308,
    'utrecht': 1560,
    'zeeland': 2933
}

# Create the Series objects out from the dictionaries
municipalities_series: pd.Series = pd.Series(municipalities)
area_series: pd.Series = pd.Series(area)
    
# Create the Pandas DataFrame object
provinces: pd.DataFrame = pd.DataFrame({
    'municipalities': municipalities_series, 
    'area': area_series
})
provinces


# In[ ]:


# Indexing of the area column in a dictionary-style manner
area_s: pd.Series = provinces['area']
print(type(area_s))
area_s


# We can also index the data frame in an attribute-style manner: `data_frame.column_name`. You will get exactly the same output as the one obtained in the previous cell. However, this method won't always work. Cases where you should go for dictionary-style indexing include:
# * Non-string column names
# * Conflicts between column names and `DataFrame` methods

# In[ ]:


# Indexing of the area column in an attribute-style manner
area_s: pd.Series = provinces.area
print(type(area_s))
area_s


# You can also use indexing to create new columns in your data frame. For instance, let us imagine that we can know the area per municipality if you split equally the total province area by the number of its municipalities.

# In[ ]:


provinces['area_municipality'] = round(provinces['area'] / provinces['municipalities'], 2)
provinces


# The $area \div municipalities$ operation is applied to each row of the `DataFrame` object. This capability is known as **element-by-element arithmetic**.
# 
# We can also use the `values` attribute to access the raw data of the data frame.

# In[ ]:


provinces.values


# But what happens if we type `provinces.values[0]`? Will we get the first *column* or the first *row* of the data frame?

# In[ ]:


provinces.values[0]


# In that line of thought, what is the output of the expression `provinces['zeeland']`?

# In[ ]:


provinces['zeeland']


# We get a `KeyError`! When using the `values` attribute we get the first row, while when using dictionary-style indexing we consider columns. This gives birth to potential confusion. Fortunately, Pandas already offered us the `loc`, `iloc`, and `ix` indexers.

# In[ ]:


# Get all rows between 'groningen' and 'utrecht' + all columns
provinces.loc['groningen':'utrecht']


# In[ ]:


# Get all rows between 'groningen' and 'utrecht' + all columns unntil 'area'
provinces.loc['groningen':'utrecht', :'area']


# In[ ]:


# Get all rows between indices 4 and 10 + all columns
provinces.iloc[4:10]


# In[ ]:


# Get all rows between indices 1 and 10 + all columns between indices 0 and 2
provinces.iloc[4:10, :2]


# We can also use the `loc` indexer to apply data masking to our `DataFrame` object as follows.

# In[ ]:


# Get all cases where the number of municipalities is greater than 50
provinces.loc[provinces['municipalities'] > 50]


# Moreover, any of the previous conventions can be used to modify data.

# In[ ]:


provinces


# In[ ]:


# Swap the municipalities values between drenthe (iloc[0, 0]) and zeeland (iloc[12, 0])
provinces.iloc[0, 0], provinces.iloc[len(provinces) - 1, 0] = provinces.iloc[len(provinces) - 1, 0], provinces.iloc[0, 0]
provinces


# The previous code written with the `iloc` indexer can be rewritten with the `loc` indexer as follows.

# In[ ]:


# Swap the municipalities values between drenthe and zeeland
provinces.loc['drenthe', 'municipalities'], provinces.loc['zeeland', 'municipalities'] = provinces.loc['zeeland', 'municipalities'], provinces.loc['drenthe', 'municipalities']
provinces

