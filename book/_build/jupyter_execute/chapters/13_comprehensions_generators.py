#!/usr/bin/env python
# coding: utf-8

# # Comprehensions and Generators [^intro]
# 
# [^intro]: This Jupyter Notebook is based on Chapter 19 (Sections 19.2-19.5) of {cite}`Severance2016`.
# The extra material presented is based on Jupyter notebooks developed by Tom Verhoeff (TU/e).

# ## Collections of Data
# 
# Comprehensions and generators are ways of transforming
# collections of data.
# So, let us first look at such data collections.
# 
# A collection of data can be **stored** in a **tuple**, **list**, **set**, or **dictionary**. The difference between using one or the other will depend on the properties you need to represent your data. In the following table, we briefly present the properties of each of these collections.
# 
# | Collection | Mutable | Ordered | Allows duplicates | Indexed | Representation |
# |------------|:-------:|:-------:|:----------------:|:-------:|:--------------:|
# | `tuple` | ✖︎ | ✔︎ | ✔︎ | ✔︎ | `(...)` |
# | `list`  | ✔︎ | ✔︎ | ✔︎ | ✔︎ | `[...]` |
# | `set`   | ✔︎ | ✖︎ | ✖︎ | ✖︎ | `{...}` |
# | `dict`  | ✔︎ | ✖︎ | ✖︎ | ✔︎ * | `{key: val, ...}` |
# 
# <sup>*</sup> You access key-value pairs via a key.
# 
# Additionally, we have already seen a number of built-in operations on lists, such as
# * **indexing**, to access an item at a given index:
#   `s[i]`, where `0 <= i < len(s)`
# * **slicing**, to extract a subsequence of items:
#   `s[a:b]` extracts the list of `s[i]` with `a <= i < b`,
#   or `s[a:b:c]` where `c` is the step size
# * **concatenation**: `s + t`
# * **length**: `len(s)`
# * **aggregation**: `sum(s)`, `min(s)`, `max(s)`
# * **sorting**: `sorted(s)`

# ## Iterables and Iterators
# 
# What collections of data have in common is that they are _iterable_.
# An **iterable** is any collection that you can step through one by one.
# To traverse an *iterable* you require an **iterator**.
# An *iterator* is an object that traverses your iterable and returns one element at a time. 
# To transform a collection into an iterator, we use the `iter()` method.
# Afterwards, each element in the iterator can be accessed by repeatedly calling the `next()` method.
# 
# ```{image} assets/iterable-iterator.png
# :alt: Iterables and Iterators
# :width: 500px
# :align: center
# ```
# 
# <div style="text-align:center">
#     <span style="font-size:0.9em; font-weight: bold;">Iterables and iterators in Python.</span>
# </div>

# In[1]:


# Create a list of integers, which is an iterable
iterable: list = [1, 2, 3, 4, 5]
print(type(iterable))
iterable


# In[2]:


from typing import Iterator 

# Create an iterator out from the "iterable" list
iterator: Iterator = iter(iterable)
type(iterator)


# In[3]:


# Traverse the iterable via the iterator
num_one = next(iterator)
print(f'First iteration: {num_one}')

num_two = next(iterator)
print(f'Second iteration: {num_two}')

num_three = next(iterator)
print(f'Third iteration: {num_three}')

num_four = next(iterator)
print(f'Fourth iteration: {num_four}')

num_five = next(iterator)
print(f'Fifth iteration: {num_five}')


# If the collection has been traversed and you call the `next()` function one more time, you will get a `StopIteration` error.

# In[4]:


next(iterator)


# Let us now use the `while` loop to iterate over our iterable in a smarter way.

# In[ ]:


iterable: list = [1, 2, 3, 4, 5]
iterator: Iterator = iter(iterable)
i: int = 0

while i < len(iterable):
    val: int = next(iterator)
    print(val)
    i += 1


# When using a `for` loop, you do not need to call these methods. The previous procedure is done under the hood by Python!
# 
# Furthermore, one *iterable* can be iterated over or traversed multiple times. Each new traversal involves a new *iterator*.
# In fact, multiple iterators can be active concurrently on the same collection, as it is the case of nested loops.

# In[ ]:


letters: tuple = ('a', 'b', 'c')

for i in letters:
    for j in letters:
        print('{}{}'.format(i, j), end=" ")
    print()


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Iterate over the list of words and add the words that start by 'a' to a new list.
# ```

# In[ ]:


words = ['age', 'bee', 'ask', 'cut', 'clean', 'zoo', 'add']
# Remove this line and add your code here


# ## Comprehensions
# 
# A **list comprehension** is an _expression_ that constructs a list
# based on some *iterable*.
# The items taken from the iterable can be _transformed_ in an expression
# before being collected in the list.
# 
# In the next example, the iterable is `range(10)`, and we collect the squares of the numbers in that range:

# In[ ]:


[n * n for n in range(10)]


# The list comprehension above defines the same list
# as the following program fragment
# with a **`for`** statement and an auxiliary variable (`aux`), but in a more compact way.

# In[ ]:


aux: list = []

for n in range(10):
    aux.append(n * n)

aux


# The comprehension is more compact, and
# does not need an explicit list variable.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Use a comprehension to create a list where all words in the given list are transformed into capital letters.
# ```

# In[ ]:


words = ['age', 'bee', 'ask', 'cut', 'clean', 'zoo', 'add']
# Remove this line and add your code here


# ## Selective Inclusion in a Comprehension
# 
# You can also _selectively_ include items in the constructed list,
# by using an `if` clause.
# For instance, the numbers less than 10
# that leave a remainder more than 2 when divided by 7:

# In[ ]:


[n for n in range(10) if n % 7 > 2]


# And here is the list of _squares_ of those numbers
# that leave a remainder more than 2 when divided by 7.

# In[ ]:


[n * n for n in range(10) if n % 7 > 2]


# Note that the condition is applied to the items
# _before_ they are transformed.
# 
# This is like putting an `if` statement inside the `for` loop.

# In[ ]:


aux: list = []
    
for n in range(10):
    if n % 7 > 2:
        aux.append(n * n)

aux


# In summary, a **list comprehension**
# ```python
# [E(v) for v in iterable if C(v)]
# ```
#   
# * takes items from an _**iterable**_:
#   ```python
#   for v in iterable
#   ```
# * _**selects**_ items based on a condition:
#   ```python
#   if C(v)
#   ```
# * _**transforms**_ the selected items using an expression:
#   ```python
#   E(v)
#   ```
# * and _**collects**_ the expression results in a list:
#   ```python
#   [...]
#   ```
# 
# Note the order: first select, then transform
# (even though you write the transformation first, and the selection last).

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Remember our fisr exercise in this notebook? Use a comprehension to iterate over the list of words and add the words that start by 'a' to a new list.
# ```

# In[ ]:


words = ['age', 'bee', 'ask', 'cut', 'clean', 'zoo', 'add']
# Remove this line and add your code here


# ## Nested Comprehensions
# 
# If you need to select _after_ transforming the items,
# then you can use a _nested_ comprehension
# (but do read the **warning** after the following example).

# In[ ]:


[sq for sq in [n * n for n in range(10)] if sq % 7 > 2]


# Observe that the result is different with `[n * n for n in range(10) if n % 7 > 2]`, why?

# `````{admonition} Warning
# :class: tip
# In a **nested comprehension**, the _inner_ comprehension is **completely evaluated and stored** before it is being used in the _outer_ comprehension.
# `````
# 

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# We have a list of lists. The internal lists have numbers as elements. We would like to flatten the outer list; i.e. instead of have lists of lists of numbers we just want to have a list of numbers. Use a nested comprehension to achieve this goal.
# ```

# In[ ]:


lst = [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10], [11], [12, 13, 14, 15]]
# Remove this line and add your code here


# ### Alternative Approaches for Selection _After_ Transformation
# 
# Perfom the transformation (in this case: squaring)
# also in the `if` clause:

# In[ ]:


[n * n for n in range(10) if n * n % 7 > 2]


# A disadvantage of this approach is that every transformation is done *twice*,
# which can be costly if the transformation is expensive.

# ## Set and Dictionary Comprehensions
# 
# * [Comprehensions also work for _sets_ and _dictionaries_](https://docs.python.org/3/reference/expressions.html#displays-for-lists-sets-and-dictionaries).
# * Comprehensions can involve multiple `for` and `if` clauses
#   (but always start with an expression and a `for` clause).
#   
# Here are some examples.
# The _set_ of non-prime numbers up to 100:

# In[ ]:


composites: set = {i * j for i in range(2, 10 + 1) for j in range(2, 100 // i + 1)}
composites


# Let us decompose this rather complex comprehension by looking what each step does, both as `list` and `set`.

# In[ ]:


[i for i in range(2, 10 + 1)]


# In[ ]:


{i for i in range(2, 10 + 1)}


# Let us add the second comprehension and first see the result when a list is being returned.

# In[ ]:


[j for i in range(2, 10 + 1) for j in range(2, 100 // i + 1)]


# In[ ]:


{j for i in range(2, 10 + 1) for j in range(2, 100 // i + 1)}


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# We would like to use a set comprehension to create a set with all words of length 4 that are part of a given list. Remember that sets do not have duplicates and that is why we eant to use them as data type.
# ```

# In[ ]:


lst = ['funny', 'that', 'little', 'yoke', 'sunny', 'side', 'up', 'in', 'the', 'span',
       'of', 'the', 'lake']
# Remove this line and add your code here


# A _dictionary_ that associates the numbers 13 through 32
# to their squares:

# In[ ]:


squares: dict = {n: n * n for n in range(13, 32 + 1)}
squares


# A _list_ of powers
# where the base is a prime less than 10 and
# exponents run from 2 through 5
# (it uses `composites` defined earlier);
# note the clause order `for if for`:

# In[ ]:


[base ** exp for base in range(2, 10 + 1) if base not in composites for exp in range(2, 5 + 1)]


# In order to understand it may be again helpful to look at the individual results of each comprehension.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Use a comprehension to create a dictionary that stores the words within the list <i>lst</i> as keys and tehir length as values.
# ```

# In[ ]:


lst = ['funny', 'that', 'little', 'yoke', 'sunny', 'side', 'up', 'in', 'the', 'span',
       'of', 'the', 'lake']
# Remove this line and add your code here


# ## Comprehensions Evaluation
# 
# Comprehensions are completely evaluated before further use.
# 
# What if you do not need the whole list constructed by the comprehension?
# Suppose, for instance, you only want the first element.
# Will the whole list still be computed?
# 
# To illustrate what we mean,
# we first show a version with explicit
# **`for`**, **`if`**, and **`break`** statements,
# that avoids computing all values in the list.
# It stops when the first item has been computed.

# In[ ]:


aux: list = []

for n in range(10):
    if n % 7 > 2:
        aux.append(n * n)
        break

print(aux)
aux[0]


# Let's try this with our comprehension,
# by extracting the first item (at index 0).

# In[ ]:


[n * n for n in range(20) if n % 7 > 2][0]


# Actually, we now cannot see whether the whole list got computed.
# So, let us introduce a function `f` with a **side effect**
# to make this visible.
# A *side effect* is the modification of any sort of state such as changing a mutable variable, using IO, or throwing an exception.
# As a function, `trail` does nothing to its argument:
# it returns _n_ unchanged.
# But it also prints a dot, and this is a (visible) side effect.

# In[ ]:


from typing import Any

def trail(n: Any) -> Any:
    """ Print a dot and return n.
    """
    print('.', end='')
    return n


# Let us try again.

# In[ ]:


[trail(n * n) for n in range(20) if n % 7 > 2][0]


# Apparently, the whole list got computed first.

# ## Generators
# 
# We can fix this by using a generator.
# * A [**generator expression**](https://docs.python.org/3/reference/expressions.html#generator-expressions) is like a comprehension:
# it _selectively_ takes items from an _iterable_ and
# _transforms_ them.
# * But a generator does not construct a list to store all items.
# * A generator is **lazy**,
# in the sense that a generator will not be computed completely in advance.
# (In fact, a generator can be endless/infinite.)
# * Instead,
# a generator is only evaluated to the extent that its values are needed.
# The evaluation of a generator is **demand driven**.
# 
# A generator is not a list, but it is itself again an _iterable_.
# In fact, a generator is an _iterator_.
# (A list is also an iterable, but a list is completely stored in memory.)
# 
# Let us define a function `first`
# that will only extract the first element of an iterable.
# (We need this function `first`,
# because we cannot extract the first item from an iterable by indexing it at 0,
# like we did with the list comprehension.)

# In[ ]:


from typing import Iterable

def first(iterable: Iterable) -> Any:
    """ Returns first item from iterable.
    """
    for item in iterable:
        return item  # and ignore everything else


# If we apply this to the list comprehension, we (again) see that the whole list still gets computed.

# In[ ]:


first([trail(n * n) for n in range(20) if n % 7 > 2])


# Now, let us apply it to the generator version of the comprehension.
# Note the use of **round parentheses** instead of square brackets.
# By the way, since the function call also involves round parentheses,
# we don't have to repeat another pair.

# In[ ]:


first(trail(n * n) for n in range(20) if n % 7 > 2)


# We see that now only one item got computed (the first one).

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Create the function `first_multiple_of_2` which gets an iterable as argument and returns the first number that is multiple of two. Build a generator that iterates over number from 1 to 10, and computes the result of multiplying a given number by 3. 
# ```

# In[ ]:


# Remove this line and add your code here


# ### A Generator Can be Used Only Once

# Because a generator is a (special kind of) iterator,
# it can be used only once.

# Let us store our generator in a variable:

# In[ ]:


my_gen = (trail(n * n) for n in range(10) if n % 7 > 2)


# You can then use this variable as an iterable.

# In[ ]:


first(my_gen)


# In[ ]:


for i in my_gen:
    print(i, end=" ")


# Observe that the generator continued where it left off after its first (partial) use.
# Once a generator is exhausted (has reached the end), it becomes useless.

# In[ ]:


for i in my_gen:
    print(i, end=" ")


# (There is no output, because the generator was already exhausted.)

# ## Factories
# 
# Since generators (like iterators) are not reusable,
# it is more common to define a **function that returns a fresh generator** on each call.
# Such a function is also known as a **factory**.
# If that function is parameterized,
# then you can produce _customized_ generators.
# 
# Here is an example of a parameterized factory:

# In[ ]:


from typing import Generator

def square_factory(m: int) -> Generator[int, None, None]:
    """ Returns a generator for the squares of numbers in the range [0, m).
    """
    return (n * n for n in range(m) if n % 7 > 2)


# The call `square_factory(10)` returns (a fresh copy of) the generator
# that we considered above.
# 
# Let's try the same things again, using this factory.

# In[ ]:


first(square_factory(10))


# In[ ]:


for i in square_factory(10):
    print(i, end=" ")
    
print()

for i in square_factory(10):
    print(i, end=" ")


# That looks better.
# The **`for`** loop starts all over again.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Create a factory function to return the generator you created before: the one related to computing the multiplication of a number by 3.
# ```

# In[ ]:


# Remove this line and add your code here

