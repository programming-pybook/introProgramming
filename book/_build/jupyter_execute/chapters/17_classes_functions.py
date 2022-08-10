#!/usr/bin/env python
# coding: utf-8

# # Classes and Functions
# 
# This Jupyter Notebook is based on Chapter 16 of {cite}`thinkPython`.

# _(c) 2020, Mark van den Brand, Eindhoven University of Technology_

# The next step is to develop functions that manipulate the programmer-defined types. We will see how these types can be passed as arguments to functions and be returned as results.
# 
# In this chapter a functional programming style will be used.

# ## Time
# 
# We will start with introducing another programmer-defined type: the class `Time`.

# In[1]:


class Time:
    """Represents the time of day.
    
    attributes: hour, minute, second
    """


# We can now create `Time` objects and assign values to the attributes: `hours`, `minutes`, and `seconds`.

# In[2]:


time : Time = Time()
time.hour : int = 11
time.minute : int = 59
time.second : int = 33


# In the next cell, a new way of formatting strings is shown. See https://pyformat.info for more information.

# In[3]:


def print_time(time : Time) -> None:
    """ prints a Time object
    """
    print('({:02d}:{:02d}:{:02d})'.format(time.hour,time.minute,time.second))

print_time(time)


# In[4]:


def is_after(time1 : Time, time2 : Time) -> bool:
    """ gets 2 Time objects as argument and 
        returns a boolean to indicate whether time1 is greater than time2
    """
    return time1.hour > time2.hour or time1.minute > time2.minute or time1.second > time2.second

new_time : Time = Time()
new_time.hour : int = 11
new_time.minute : int = 59
new_time.second : int = 31

is_after(time,new_time)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Create the function `print_time_meridiem(time : Time)`, which takes an instance of type Time and prints the time following the 12-hour convention (e.g. 12:05 pm, 11:46 am).
# ```

# In[5]:


# Remove this line and add your code here


# ## Pure Functions
# 
# We will develop functions that allows us to manipulate `Time` objects: **pure functions** and **modifiers**.
# 
# The strategy for developing these functions is based on **prototype and patch**;
# a way of tackling a complex problem by
# starting with a simple prototype and incrementally dealing with the complications.
# 
# The next cell shows a simple prototype of the `add_time` function.

# In[6]:


def add_time(t1 : Time, t2 : Time) -> Time:
    """ returns a new Time object containing the sum of the 2 argument Time objects
    """
    sum : Time = Time()
    sum.hour : int = t1.hour + t2.hour
    sum.minute : int = t1.minute + t2.minute
    sum.second : int = t1.second + t2.second
    return sum


# This function creates a new `Time` object (`sum`), its attributes are initialized by adding
# the values of the attributes of the arguments, and eventually returns the created object.
# 
# This is called a **pure function** because it does not have any side effects:
# * it does not modify any of the objects passed to it as arguments and 
# * it has no effect, like displaying a value or getting user input, other than returning a value.
# 
# The function of the previous cell can be tested by creating and adding 2 `Time` objects.

# In[7]:


start : Time = Time()
start.hour : int = 21
start.minute : int = 45
start.second : int = 0

duration : Time = Time()
duration.hour : int = 1
duration.minute : int = 35
duration.second : int = 0

finished = add_time(start, duration)
print_time(finished)


# This is of course an illegal time.
# 
# The problem is caused by the fact that we did not keep track of the fact that there are only `60` seconds in a minute, `60` minutes in an hour, and `24` hours in a day, *or do we allow more hours in a `Time` object?*
# 
# What were the exact **requirements**?
# 
# Let us assume that there are only `24` hours in a day.
# 
# So, we are representing the *time of the day*, not a time frame.
# 
# We need to *carry* over seconds to minutes and minutes to hours.

# In[8]:


def add_time(t1 : Time, t2 : Time) -> Time:
    """ returns a new Time object containing the sum of the 2 argument Time objects
    """
    sum : Time = Time()
    sum.hour : int = t1.hour + t2.hour
    sum.minute : int = t1.minute + t2.minute
    sum.second : int = t1.second + t2.second

# fix the seconds if greater than 60
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

# fix the minutes if greater than 60
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
        
# fix with hours if greater than 24
    if sum.hour >= 24:
        sum.hour -= 24
        
    return sum


# This function does the job, this solution is slightly more elaborated.
# 
# The function is quite long and a more concise solution will be presented.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Create the pure function <i>convert_utc(time : Time, utc_units : int) -> Time</i>, which takes an instance of type Time (representing the Coordinated Universal Time -UTC) and the number of UTC units. This function adds the integer to the <i>hours</i> attribute. Remember that an hour must be equal or greater to zero, and less than 24.
# ```

# In[9]:


# Remove this line and add your code here


# ## Modifiers
# 
# It may be useful for a function to modify the objects it gets as parameters. 
# 
# In that case, the changes are visible to the caller. 
# 
# Functions that work this way are called **modifiers**.
# 
# In the next cell, a first version of the function `increment` is presented.

# In[10]:


def increment2(time : Time, seconds : int) -> None:
    """ adds the seconds (2nd argument) to the Time object
    """
    time.second += seconds
    
# fix the seconds if greater than 60
    while time.second >= 60:
        time.second -= 60
        time.minute += 1
        
# fix the minutes if greater than 60
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1

# fix with hours if greater than 24
    while time.hour >= 24:
        time.hour -= 24 


# The function starts with adding the `seconds` to `time.second`; the remainder deals with the special cases we
# saw before.
# 
# This function is not correct, when the amount of seconds to be added is larger than `60`.
# 
# It is then necessary to add more minutes to `time.minutes` than just `1`.
# 
# A straightforward solution is to use a `while` loop, but this may not be very efficient.
# 
# Anything that can be done with modifiers can also be done with pure functions. 
# 
# In fact, some programming languages, also known as **functional programming languages**, 
# only allow pure functions. 
# 
# There is some evidence that programs that use pure functions are faster to develop and less error-prone than programs
# that use modifiers. 
# 
# But modifiers are convenient at times, and functional programs tend to be less efficient.
# 
# It is, therefore, good practice to develop **pure functions** instead of **modifiers**.

# In[11]:


def increment(time : Time, seconds : int) -> None:
    """ adds the seconds (2nd argument) to the Time object
    """
    (hours, seconds) = divmod(seconds, 3600)
    time.hour += hours
    
    (minutes, seconds) = divmod(seconds, 60)
    time.minute += minutes
    
    time.second += seconds
    
# fix the seconds if greater than 60
    if time.second >= 60:
        time.second -= 60
        time.minute = 1

# fix the minutes if greater than 60
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1

# fix with hours if greater than 24
    while time.hour >= 24:
        time.hour -= 24 
        
print_time(start)
increment(start, 3660)
print_time(start)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Let's introduce some changes to the previous exercise. Create the modifier <i>convert_utc_modifier(time : Time, utc_units : int) -> Time</i>, which takes an instance of type Time (representing the Coordinated Universal Time -UTC) and adds the number of UTC units to it. This function adds the integer to the <i>hours</i> attribute. Remember that an hour must be equal or greater to zero, and less than 24.
# ```

# In[12]:


# Remove this line and add your code here


# ## Prototyping vs. Planning
# 
# The development strategy used so far in this chapter has been *prototype and patch*.
# 
# The problem with this approach is that the code becomes bulky, it may contain code to deal with a lot of corner cases.
# 
# This approach can be effective, especially if you do not have yet a deep understanding
# of the problem, but it may involve a lot of testing.
# 
# An alternative is *designed development*, in which high-level insight into the problem can
# make the programming much easier. 
# 
# For instance, to realize that the conversion from time to seconds and back allows us just to manipulate time
# in terms of the amount of seconds; `1` minute is `60` seconds and `1` hour is `3600` seconds.
# 
# So, if we convert the `Time` object to an integer value representing seconds and back, we are done.

# In[13]:


def time_to_int(time : Time) -> int:
    """ converts a Time object into an integer value representing seconds
    """
    minutes : int = 60 * time.hour + time.minute
    seconds : int = 60 * minutes + time.second
    return seconds

print_time(start)
print(time_to_int(start))


# We need now to develop the inverse function: `int_to_time`.
# 
# This function takes an integer value as argument and returns a `Time` object.
# 
# We will use a special data type: tuples. We will dive deeper into this type in coming topics, for now let us just see how to use them.

# In[14]:


def int_to_time(seconds : int) -> Time:
    """ converts an integer value representing seconds into a Time object
    """
    time : Time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    
# fix with hours if greater than 24
    if time.hour >= 24:
        time.hour -= 24
        
    return time


# One way to check that both functions are correct is by means of using a *consistency check*. 
# 
# In this case, we will verify with the expression `time_to_int(int_to_time(x)) == x`.

# In[15]:


x = 86300
time_to_int(int_to_time(x)) == x


# However, the solutions presented in the book "Think Python" do not deal with the fact that there are only `24` hours in a day.
# 
# Thus, the proposed test, `time_to_int(int_to_time(x)) == x`
# does not work for values equal or greater than `86400`.
# 
# This is a typical case of getting the right **requirements**.

# In[16]:


print_time(int_to_time(86399+1))


# In[17]:


time_to_int(int_to_time(86399+1)) == 86400


# Once we are convinced that both functions are correct (according to our specifications), we can reimplement
# the `add_time` and `increment` functions.

# In[18]:


def add_time(t1 : Time, t2 : Time) -> Time:
    """ returns a new Time object containing the sum of the 2 argument Time objects
    """
    seconds : int = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


# In[19]:


def increment(t1 : Time, s : int) -> Time:
    """ returns a new Time object containing the sum of the 2 argument Time objects
    """
    seconds : int = time_to_int(t1) + s
    return int_to_time(seconds)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# These time conversion functions allow us to develop also a <i>sub_time(t1 : Time, t2 : Time) -> Time</i> function, that subtracts two time intervals. Again, make sure you that your are not 'travelling back to the future', or end up with a negative time.
# ```

# In[20]:


# Remove this line and add your code here


# ## Testing
# 
# Whenever you have defined a variable or a function, **verify** it, _before_ using it. 
# Do not rely on them blindly.
# 
# * Inspect the value of the variable
# * Apply the function to some arguments, and inspect the results
#     
# **Advice**: Keep such test code in your notebook, so that you can rerun it and use it as a kind of documentation.

# ### Testing of functions
# 
# Testing is a way of convincing yourself that the implementation of the function is correct. Testing is not equivalent to giving a formal proof. 
# 
# In order to be able to test, you should first execute the function yourself in your head or on paper. Suppose you have written a function to sort elements of a list, then you could start with a non-empty list of unsorted elements, and do the sorting of the list of elements yourself resulting in a sorted list of elements. This already shows that you should start with manageable input. You should not start with a list with more than 100 elements.
# 
# * Choose appropriate arguments
# * Apply function and gather results
# * Decide on pass or fail

# ### Manual testing
# 
# A simple but rather labor-intensive way of testing is manual testing. You write in one cell the function body and in a few following cells, the various tests for the function. 
# 
# When testing you have to think of corner cases, for instance, empty lists, the elements at the first or last index of a list.
# 
# * Call the function for various arguments in a code cell, such that it shows some result (either via `print` or as last expression in code cell).
# 
# ```
# sorted_list = sort([4, 3, 9, 1])
# print(sorted_list) # This should give [1, 3, 4, 9]
# ```
# * Visually, check those results.

# In[21]:


from typing import List
import random

def roll_dice(n: int) -> List[int]:
    """Roll n dice.
    Assumption: n >= 0.
    """
    
    rolls : List[int] = list()
    
    for _ in range(n):
        rolls.append(random.randint(1, 6))
    
    return rolls


# In[22]:


#Test 1: boundary case
roll_dice(100)


# In[23]:


#Test 2: test the length of the resulting list
len(roll_dice(3))


# In[24]:


#Test 3: test whether all rolls are valid
rolls_bool : List[bool] = list()

for roll in roll_dice(10):
    rolls_bool.append(roll in range(1, 6 + 1)) # list of Booleans

print(rolls_bool)
all(rolls_bool) # check if all Booleans in the list are True


# ### More on function testing 
# 
# The challenge with function testing is to convince yourself that you have dealt with all possible cases that the function needs to handle.
# 
# * Testing a function in just one call is hardly ever enough.
# * Pick a _few_ _important_ arguments, for which you can check the corresponding result.
# * Boundary cases, and small typical case
#     * Strive for **code coverage**
#     * Code that is not executed during the call, is not tested
#     * Cover all branches of `if-elif-else`
# * You do not need to check the result directly; could test it indirectly. For instance, by checking the number of elements in a list instead of inspecting the list.
# 
# Suppose you need to write a function that merges 2 lists. A sufficient test can be to check whether the length of the resulting list is the same as the length of both argument lists.

# ### Automated testing via docstring
# 
# A good programming practice is to add **usage examples** to the docstring:
# * You can do it in such a format
#     that these examples are **automatically executable and checkable**
# 
# Format of examples/test cases in docstring:
# 
# ```
# >>> expression with function call
# expected result
# ...
# ...
# >>> expression with function call
# expected result
# ```

# In[25]:


from typing import List
import random

def roll_dice(n: int) -> List[int]:
    """Roll n dice.
    
    Assumption: n >= 0.
    
    Examples and test cases:
    >>> roll_dice(0)  # boundary case
    []
    >>> len(roll_dice(3))  # test length
    3
    >>> all(roll in range(1, 6 + 1) for roll in roll_dice(10))  # test values
    True
    """
    
    rolls : List[int] = list()
    
    for _ in range(n):
        rolls.append(random.randint(1, 6))
    
    return rolls


# How to run test cases for function with docstring tests:
# 
# * `import doctest`
# * `doctest.run_docstring_examples(func, globals(), verbose=True, name='...')`  
#     runs all test cases of `func`, reporting details
# * `doctest.run_docstring_examples(func, globals(), verbose=False)`  
#     runs all test cases, only reporting failures

# In[26]:


import doctest


# In[27]:


doctest.run_docstring_examples(roll_dice, globals(), verbose=True, name='roll_dice')


# In[28]:


doctest.run_docstring_examples(roll_dice, globals(), verbose=False, name='roll_dice')


# One more example of tests in docstring:

# In[29]:


from typing import Dict
from collections import defaultdict

def count_text(text: str) -> Dict[str, int]:
    """Return dictionary with count for each letter in text.
    
    >>> count_text("")  # boundary case
    {}
    >>> count_text("dad")
    {'d': 2, 'a': 1}
    """
    counts : dict = defaultdict(int)  # use 0 when key is not present
    
    for letter in text:
        counts[letter] += 1

    return dict(counts)


# In[30]:


count_text("dad")


# In[31]:


doctest.run_docstring_examples(count_text, globals(), verbose=True, name='count_text')


# How to run test cases for all functions with docstring tests:
# 
# * `doctest.testmod(verbose=True)` runs all test cases, reporting details
# * `doctest.testmod(verbose=False)` runs all test cases, showing a summary

# In[32]:


doctest.testmod(verbose=True)  # with details


# In[33]:


doctest.testmod(verbose=False)  # without details


# ### Invariants
# 
# A `Time` object is well-formed if the values of minute and second are between 0 and 60
# (including 0 but not 60) and if hour is between 0 and 24.
# 
# Requirements like these are called **invariants** because they should always be true. 
# 
# To put it a different way, if they are not true, something has gone wrong.
# 
# Writing code to check invariants can help detect errors and find their causes. 
# 
# The next cell contains the function `valid_time(time : Time)` that takes a `Time` object and returns `False` if it
# violates an **invariant**.

# In[34]:


def valid_time(time : Time) -> bool:
    """ checks whether we are dealing with a correct Time object
    """
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.hour >= 24 or time.minute >= 60 or time.second >= 60:
        return False
    return True


# At the beginning of each function you could check the arguments to make sure they are
# valid.

# In[35]:


def add_time(t1 : Time, t2 : Time) -> Time:
    """ returns a new Time object containing the sum of the 2 argument Time objects
    """
    
    if not valid_time(t1) or not valid_time(t2):
        raise ValueError('invalid Time object in add_time')
    seconds : int = time_to_int(t1) + time_to_int(t2)
    
    return int_to_time(seconds)


# Or you could use an **assert statement**, which checks a given invariant and raises an exception
# if it fails.

# In[36]:


def add_time(t1 : Time, t2 : Time) -> Time:
    """ returns a new Time object containing the sum of the 2 argument Time objects
    """
    
    assert valid_time(t1) and valid_time(t2)
    seconds : int = time_to_int(t1) + time_to_int(t2)
    
    return int_to_time(seconds)


# **Assert statements** are useful because they distinguish code that deals with normal conditions
# from code that checks for errors.
