#!/usr/bin/env python
# coding: utf-8

# # Classes and Methods [^intro]
# 
# [^intro]: This Jupyter Notebook is based on Chapter 17 of {cite}`thinkPython`.

# So far, we have seen a few object-oriented features of Python, but the relation between
# programmer-defined types and functions can be much stronger and allow for real encapsulation
# of the programmer-defined data and corresponding functionalities.
# 
# The next step is to change those functions into methods that make the relationships explicit.

# ## Object-oriented Features
# 
# Python is an **object-oriented programming language**, which means that it provides features
# that support object-oriented programming, which has these defining characteristics:
# 
# * Programs include class and method definitions.
# * Most of the computations are expressed in terms of operations on objects.
# * Objects often represent things in the real world, and methods often correspond to the ways things in the real world interact, for instance created, destroyed, updated, etc.

# The `Time` class corresponded to the way people consider
# the time of day, and the functions we defined corresponded to how people want to manipulate time.
# 
# So far, we have not taken advantage of the object-oriended features Python provides when writing code. 
# 
# These features were expressed using the known language constructs, but the object-oriented 
# alternative is more concise and more accurately conveys the structure of the program.
# 
# In case of the `class Time` and the functions defined for `Time` it can be observed that all
# functions take `Time` as an argument.

# This observation is the motivation for methods; a **method** is a function that is associated
# with a particular class. 
# 
# The objects representing strings, lists, dictionaries and tuples already provided methods for manipulations.
# 
# In this chapter, we will define methods for programmer-defined types.
# 
# Methods are semantically the same as functions, but there are two syntactic differences:
# 
# * Methods are defined inside a class definition in order to make the relationship between
# the class and the method more explicit.
# * The syntax for invoking a method is different from the syntax for calling a function.
# 
# The functions we defined in the previous two chapters will be gradually transformed into methods.

# ## Printing Objects
# 
# We defined the class `Time` and defined a function to print the time `print_time`.

# In[1]:


class Time:
    """Represents the time of day."""
    
def print_time(time : Time) -> None:
    """ prints a Time object
    """
    print('{:02d}:{:02d}:{:02d}'.format(time.hour,time.minute,time.second))


# This function uses a `Time` object as argument.

# In[2]:


start : Time = Time()
start.hour : int = 21
start.minute : int = 45
start.second : int = 0

print_time(start)


# To change `print_time` into a method, the function has to be declared inside the class definition. 
# 
# This is done by *increasing* the indentation.
# 
# ````{margin}
# ```{admonition} EXTRA
# If a function is transformed into a method, so moved into its corresponding class, the type information related to the class has to be removed!
# ```
# ````
# 

# In[3]:


class Time:
    """Represents the time of day."""
    
    def print_time(time) -> None:
        """ prints a Time object
        """
        print('{:02d}:{:02d}:{:02d}'.format(time.hour,time.minute,time.second))
        
start : Time = Time()
start.hour : int = 21
start.minute : int = 45
start.second : int = 0


# Note that the method `print_time` does not have the type hint `Time` for its argument `time` anymore. 
# 
# The type `Time` is not known within the class `Time`. 
# 
# This holds for all methods defined in a class!

# There are two ways to call `print_time`. 
# 
# The first (and uncommon) way is to use **function syntax**.

# In[4]:


Time.print_time(start)


# `Time` is the name of the class, `print_time` the method to be executed, and `start` the argument to be printed.
# 
# The second way is more concise: **method syntax**.

# In[5]:


start.print_time()


# `print_time` is the name of the method (again), and `start` is
# the object the method is invoked on, which is called the **subject**. 
# 
# Inside the method, the subject is assigned to the first parameter, so in this case `start` is
# assigned to `time`.
# 
# By convention, the first parameter of a method is called `self`.
# 
# The next cell shows a more common way to write `print_time`, using the `self` parameter.

# In[6]:


class Time:
    """Represents the time of day."""
    
    def print_time(self) -> None:
        """ prints a Time object
        """
        print('{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second))


# In[7]:


start : Time = Time()
start.hour : int = 22
start.minute : int = 31
start.second : int = 0

start.print_time()


# The reason for this convention is an implicit metaphor:
# 
# * The syntax for a function call, `print_time(start)`, suggests that the function is the
# active agent. It says something like, “Hey print_time! Here’s an object for you to
# print.”
# * In object-oriented programming, the objects are the active agents. A method invocation
# like `start.print_time()` says “Hey start! Please print yourself.”
# 
# Shifting responsibility from the functions onto the objects makes it possible to write more versatile functions (or methods), and makes it easier to maintain and reuse code.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Do you remember the <i>print_time_meridiem(time : Time)</i> function from previous chapter? It is time to include it as a method of the Time class. This method should print the time following the 12-hour convention (e.g. 12:05 pm, 11:46 am).
# ```

# In[8]:


# Remove this line and add your code here


# ## Another Example
# 
# Let us introduce a few extra useful methods to the class `Time`. 
# Actually, we saw them earlier as functions.
# 
# Let us start with defining the conversion function from time to seconds `time_to_int`.
# The next cells also contain simple manual tests.

# In[9]:


class Time:
    """Represents the time of day."""

    def print_time(self) -> None:
        """ prints a Time object
        """
        print('{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)) 
        
    def time_to_int(self) -> int:
        """ converts a Time object into an integer value respresenting seconds
        """
        minutes : int = 60 * self.hour + self.minute
        seconds : int = 60 * minutes + self.second
        return seconds


# In[10]:


start : Time = Time()
start.hour : int = 21
start.minute : int = 45
start.second : int = 1

start.time_to_int() == 78301


# The conversion function, `int_to_time`, which goes from seconds to time cannot be implemented as a method of the class `Time`, because it produces a `Time` object and takes an integer value.
# 
# Functions can be implemented as methods if they take an instantiated object as argument.

# In[11]:


class Time:
    """Represents the time of day."""

    def print_time(self) -> None:
        """ prints a Time object
        """
        print('{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)) 
        
    def time_to_int(self) -> int:
        """ converts a Time object into an integer value respresenting seconds
        """
        minutes : int = 60 * self.hour + self.minute
        seconds : int = 60 * minutes + self.second
        return seconds

def int_to_time(seconds : int) -> Time:
    """ converts a values representing seconds into a Time object
    """
    time : Time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    
    # fix with hours if greater than 24
    if time.hour >= 24:
        time.hour -= 24
        
    return time


# In[12]:


start : Time = Time()
start.hour : int = 21
start.minute : int = 45
start.second : int = 0

int_to_time(start.time_to_int()).print_time()

# Beware the following test fails!
print(int_to_time(start.time_to_int()) == start)

# Where as the next test succeeds!
print(int_to_time(78301).time_to_int() == 78301)


# The next cell shows an extension of the class `Time` with the `increment` method.

# In[13]:


class Time:
    """Represents the time of day."""

    def print_time(self) -> None:
        """ prints a Time object
        """
        print('{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)) 
        
    def time_to_int(self) -> int:
        """ converts a Time object into an integer value respresenting seconds
        """
        minutes : int = 60 * self.hour + self.minute
        seconds : int = 60 * minutes + self.second
        return seconds
            
    def increment(self, seconds : int):
        """ increments a Time object with an amount of seconds (represented as an integer)
        """
        seconds += self.time_to_int()
        return int_to_time(seconds)

def int_to_time(seconds : int) -> Time:
    """ converts a values representing seconds into a Time object
    """
    time : Time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    
    # fix with hours if greater than 24
    if time.hour >= 24:
        time.hour -= 24
        
    return time


# In[14]:


start : Time = Time()
start.hour : int = 21
start.minute : int = 45
start.second : int = 0

start.print_time()
end : Time = start.increment(1337)
end.print_time()

start.time_to_int()+1337 == end.time_to_int()


# The subject, `start`, gets assigned to the first parameter, `self`. 
# 
# The argument, `1337`, gets assigned to the second parameter, `seconds`.
# 
# This mechanism can be confusing, especially if you make an error. 
# 
# If you invoke increment with two arguments, you get the following error message.

# In[15]:


end : Time = start.increment(1337, 460)


# The error message is initially confusing, because there are only two arguments in parentheses.
# 
# But the subject is also considered an argument, so all together that is three.

# ## Another (Extended) Example
# 
# The transforming the function `is_after` into a method is more involved, because `is_after` takes two `Time` objects as parameters.
# 
# It is conventional to name the first parameter `self`
# and the second parameter `other`.

# In[19]:


class Time:
    """Represents the time of day."""

    def print_time(self) -> None:
        """ prints a Time object
        """
        print('{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)) 
        
    def time_to_int(self) -> int:
        """ converts a Time object into an integer value respresenting seconds
        """
        minutes : int = 60 * self.hour + self.minute
        seconds : int = 60 * minutes + self.second
        return seconds
            
    def increment(self, seconds : int):
        """ increments a Time object with an amount of seconds (represented as an integer)
        """
        seconds += self.time_to_int()
        return int_to_time(seconds)
    
    def is_after(self, other) -> bool:
        """ checks whether the current time is after the given time
        """
        return self.time_to_int() > other.time_to_int()

def int_to_time(seconds : int) -> Time:
    """ converts a values representing seconds into a Time object
    """
    time : Time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    
    # fix with hours if greater than 24
    if time.hour >= 24:
        time.hour -= 24
        
    return time


# In[20]:


start : Time = Time()
start.hour : int = 21
start.minute : int = 45
start.second : int = 0

end : Time = start.increment(1337)
end.is_after(start)


# One nice thing about this syntax is that it almost reads like English: “end is after start?”

# Additionally, arguments in a function of method can be either **positional arguments** or **keyword arguments**.
# 
# A *positional argment* does not have a parameter name. This is the case of all parameters we have introduced so far.
# 
# A *keyword argument* does have a parameter name. Let us consider a small example.
# 
# By the way, a positional argument is an argument that does not have a parameter name;
# that is, it is not a keyword argument. In this function call:
# sketch(parrot, cage, dead=True)
# parrot and cage are positional, and dead is a keyword argument.

# In[21]:


def print_event_time(time : Time, event="None"):
    print('{:02d}:{:02d}:{:02d} {}'.format(time.hour, time.minute, time.second, event))
          
print_event_time(start, event="Log in")
print_event_time(start)


# In this case, `time` is a positional argument, while `event` is a keyword argument.

# ## The `init` Method
# 
# The init method (short for “initialization”) is a special method that gets invoked when an
# object is created. Its full name is `__init__` (two underscore characters, followed by
# init, and then two more underscores). 
# 
# Its purpose is to initialize a new object, this is the *constructor* method. When the object is created, for instance via `Time(11, 43, 51)`, the parameters are passed to the created object.
# 
# An `init` method for the `Time` class is shown in the next cell.

# In[22]:


class Time:
    """Represents the time of day."""

    def __init__(self, hour=0, minute=0, second=0):
        """ creates a new Time object and initializes it
        """
        self.hour : int = hour
        self.minute : int = minute
        self.second : int = second
            
    def print_time(self) -> None:
        """ prints a Time object
        """
        print('{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)) 
        
    def time_to_int(self) -> int:
        """ converts a Time object into an integer value respresenting seconds
        """
        minutes : int = 60 * self.hour + self.minute
        seconds : int = 60 * minutes + self.second
        return seconds
            
    def increment(self, seconds : int):
        """ increments a Time object with an amount of seconds (represented as an integer)
        """
        seconds += self.time_to_int()
        return int_to_time(seconds)
    
    def is_after(self, other) -> bool:
        """ checks whether the current time is after the given time
        """
        return self.time_to_int() > other.time_to_int()

def int_to_time(seconds : int) -> Time:
    """ converts a values representing seconds into a Time object
    """
    time : Time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    
    # fix with hours if greater than 24
    if time.hour >= 24:
        time.hour -= 24
        
    return time


# In[24]:


start : Time = Time()
start.print_time()
end : Time = Time(25, 43, 51)
end.print_time()


# As you can see this results in an invalid time representation!
# 
# Here are two alternative implementations for `__init__`.

# In[27]:


class Time:
    """Represents the time of day."""

    def __init__(self, hour=0, minute=0, second=0) -> None:
        """ creates a new Time object and initializes it,
            if at least proper values are provided.
        """
        if (0 <= hour < 24 and 0 <= minute < 59 and 0 <= second < 59):
            self.hour : int = hour
            self.minute : int = minute
            self.second : int = second
        else:
            self.hour : int = 0
            self.minute : int = 0
            self.second : int = 0
            print("Trying to create an invalid time representation!")
            
    def print_time(self) -> None:
        """ prints a Time object
        """
        print('{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)) 
        
    def time_to_int(self) -> int:
        """ converts a Time object into an integer value respresenting seconds
        """
        minutes : int = 60 * self.hour + self.minute
        seconds : int = 60 * minutes + self.second
        return seconds
            
    def increment(self, seconds : int):
        """ increments a Time object with an amount of seconds (represented as an integer)
        """
        seconds += self.time_to_int()
        return int_to_time(seconds)
    
    def is_after(self, other) -> bool:
        """ checks whether the current time is after the given time
        """
        return self.time_to_int() > other.time_to_int()

def int_to_time(seconds : int) -> Time:
    """ converts a values representing seconds into a Time object
    """
    time : Time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    
    # fix with hours if greater than 24
    if time.hour >= 24:
        time.hour -= 24
        
    return time


# Or:

# In[30]:


class Time:
    """Represents the time of day."""

    def __init__(self, hour=0, minute=0, second=0) -> None:
        """ creates a new Time object and initializes it
        """
        (ignore, self.hour) = divmod(hour, 24)
        (ignore, self.minute) = divmod(minute, 60)
        (ignore, self.second) = divmod(second, 60)

    def print_time(self) -> None:
        """ prints a Time object
        """
        print('{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)) 
                
    def time_to_int(self) -> int:
        """ converts a Time object into an integer value respresenting seconds
        """
        minutes : int = 60 * self.hour + self.minute
        seconds : int = 60 * minutes + self.second
        return seconds
            
    def increment(self, seconds : int):
        """ increments a Time object with an amount of seconds (represented as an integer)
        """
        seconds += self.time_to_int()
        return int_to_time(seconds)
    
    def is_after(self, other) -> bool:
        """ checks whether the current time is after the given time
        """
        return self.time_to_int() > other.time_to_int()

def int_to_time(seconds : int) -> Time:
    """ converts a values representing seconds into a Time object
    """
    time : Time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    
    # fix with hours if greater than 24
    if time.hour >= 24:
        time.hour -= 24
        
    return time


# In[31]:


start : Time = Time()
start.print_time()
end : Time = Time(25, 43, 51)
end.print_time()


# If you provide one argument, it overrides `hour`:

# In[32]:


start : Time = Time(9)
start.print_time()


# If you provide two arguments, it overrides `hour` and `minutes`:

# In[ ]:


start : Time = Time(9, 45)
start.print_time()


# If you provide all three arguments, they override all three default values.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Do you remember the <i>Dog</i> class? Well, let's define it again but this time you should provide a constructor. The attributes of a dog are its name and its breed.
# ```

# In[ ]:


# Remove this line and add your code here


# ## The `__str__` Method
# 
# `__str__` is a special method, like `__init__`, that is supposed to return a string representation
# of an object.

# In[33]:


class Time:
    """Represents the time of day."""

    def __init__(self, hour=0, minute=0, second=0) -> None:
        """ creates a new Time object and initializes it
        """
        (ignore, self.hour) = divmod(hour, 24)
        (ignore, self.minute) = divmod(minute, 60)
        (ignore, self.second) = divmod(second, 60)
        
    def __str__(self) -> str:
        """ creates a string from the current Time object
        """
        return '{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)
    
    def time_to_int(self) -> int:
        """ converts a Time object into an integer value respresenting seconds
        """
        minutes : int = 60 * self.hour + self.minute
        seconds : int = 60 * minutes + self.second
        return seconds
            
    def increment(self, seconds : int):
        """ increments a Time object with an amount of seconds (represented as an integer)
        """
        seconds += self.time_to_int()
        return int_to_time(seconds)
    
    def is_after(self, other) -> bool:
        """ checks whether the current time is after the given time
        """
        return self.time_to_int() > other.time_to_int()

def int_to_time(seconds : int) -> Time:
    """ converts a values representing seconds into a Time object
    """
    time : Time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    
    # fix with hours if greater than 24
    if time.hour >= 24:
        time.hour -= 24
        
    return time


# In[35]:


start : Time = Time(25, 45, 30)
print(start)


# When you print an object, Python invokes the str method.
# 
# It is a good habit to start a class with the `__init__` method, in order to initialize, and
# to write `__str__`, for debugging.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Let's add a <i>__str__</i> method to the <i>Dog</i> class. You should return the string: "This dog is called <i>name</i> and it is a <i>breed</i>".
# ```

# In[ ]:


# Remove this line and add your code here


# ## A Bit of OO Theory
# 
# Classes and objects are powerful programming tools. They allow good programmers to be very effective, but if wrongly used they create a mess and hard to maintain code.
# 
# ### Encapsulation
# 
# *Encapsulation* means enclosing something in a kind of container. Encapsulation in programming means bringing data and code together in one place and hiding the details of both and the interaction between both.
# 
# Good encapsulation ensures that a programmer does not need to dive into the details of the implementation.
# 
# ### Polymorphism
# 
# *Polymorphism* means *having more than one form*. In programming, it means that a function can be applied to different data types and a type may influence the behaviour of the function.
# 
# To be discussed in more detail in the following section.
# 
# ### Inheritance
# 
# Polymorphism can be implemented by having a method with the same name implemented in various classes.
# 
# However, this approach is tedious and error prone: we need to copy a lot of *boilerplate* code. Forgetting to add such a method to your code can make it fail.
# 
# A better approach is to use another feature of object oriented programming: *inheritance*, which allows you to reuse code in a different way.
# 
# When you create a class, you are using *inheritance*: your created class inherits *all* attributes of the class `object`. This is similar to inheriting characteristics of your parents as their child.
# 
# To be discussed in more detail in the following chapter.

# ## Operator Overloading
# 
# By defining other special methods, you can specify the behavior of operators on
# programmer-defined types. 
# 
# If you define a method named `__add__` for the
# `Time` class, you can use the `+` operator on `Time` objects.

# In[36]:


class Time:
    """Represents the time of day."""

    def __init__(self, hour=0, minute=0, second=0) -> None:
        """ creates a new Time object and initializes it
        """
        (ignore, self.hour) = divmod(hour, 24)
        (ignore, self.minute) = divmod(minute, 60)
        (ignore, self.second) = divmod(second, 60)
        
    def __str__(self) -> str:
        """ creates a string from the current Time object
        """
        return '{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)
    
    def time_to_int(self) -> int:
        """ converts a Time object into an integer value respresenting seconds
        """
        minutes : int = 60 * self.hour + self.minute
        seconds : int = 60 * minutes + self.second
        return seconds
            
    def increment(self, seconds : int):
        """ increments a Time object with an amount of seconds (represented as an integer)
        """
        seconds += self.time_to_int()
        return int_to_time(seconds)
    
    def is_after(self, other) -> bool:
        """ checks whether the current time is after the given time
        """
        return self.time_to_int() > other.time_to_int()
    
    def __add__(self, other):
        """ adds a Time object to the current Time object
        """
        seconds : int = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

def int_to_time(seconds : int) -> Time:
    """ converts a values representing seconds into a Time object
    """
    time : Time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    
    # fix with hours if greater than 24
    if time.hour >= 24:
        time.hour -= 24
        
    return time


# In[37]:


start : Time = Time(9, 45, 30)
duration : Time = Time(0, 15, 30)
print(start + duration)


# When you apply the `+` operator to `Time` objects, Python invokes `__add__`. 
# 
# When you print the result, Python invokes `__str__`. 
# 
# Changing the behavior of an operator so that it works with programmer-defined types is
# called **operator overloading**. 
# 
# For every operator in Python there is a corresponding special
# method, like `__add__`. 
# 
# For more details, see http://docs.python.org/3/reference/datamodel.html#specialnames

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Overload the &gt; operator for the <i>Time</i> class. Use the definition provided for the method <i>is_after</i>.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Type-based Dispatch
# 
# The `__add__` method introduced in the previous section, adds two `Time` objects. 
# 
# It would be convenient to use the `__add__` method to add an integer value (representing an amount of seconds) to a `Time` object.
# 
# The following is a version of `__add__` that checks the type of
# other and invokes either `add_time` or `increment`.

# In[38]:


class Time:
    """Represents the time of day."""

    def __init__(self, hour=0, minute=0, second=0) -> None:
        """ creates a new Time object and initializes it
        """
        (ignore, self.hour) = divmod(hour, 24)
        (ignore, self.minute) = divmod(minute, 60)
        (ignore, self.second) = divmod(second, 60)
        
    def __str__(self) -> str:
        """ creates a string from the current Time object
        """
        return '{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)
    
    def time_to_int(self) -> int:
        """ converts a Time object into an integer value respresenting seconds
        """
        minutes : int = 60 * self.hour + self.minute
        seconds : int = 60 * minutes + self.second
        return seconds
            
    def increment(self, seconds : int):
        """ increments a Time object with an amount of seconds (represented as an integer)
        """
        seconds += self.time_to_int()
        return int_to_time(seconds)
    
    def is_after(self, other) -> bool:
        """ checks whether the current time is after the given time
        """
        return self.time_to_int() > other.time_to_int()
    
    def add_time(self, other):
        """ adds a Time object to the current Time object
        """
        seconds : int = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
    
    def __add__(self, other : any):
        """ adds a Time object or an amount of seconds to the current Time object
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

def int_to_time(seconds : int) -> Time:
    """ converts a values representing seconds into a Time object
    """
    time : Time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    
    # fix with hours if greater than 24
    if time.hour >= 24:
        time.hour -= 24
        
    return time


# In[40]:


start : Time = Time(9, 45, 30)
print(start + 3600)
duration : Time = Time(2)
print(start+duration)


# The built-in function `isinstance` takes a value and a class object, and returns `True` if the value is an instance of the class.
# 
# If other is a `Time` object, `__add__` calls `add_time`. 
# 
# Otherwise, it assumes that the parameter is a number and calls `increment`.
# 
# This operation is called a **type-based dispatch** because it dispatches the computation to different methods based on the type of the arguments.
# 
# In object-oriented languages this is a common concept; another name is **dynamic dispatch**.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Modify the definition of the &gt; operator for the <i>Time</i> class, so it also compares the Time object against an integer. Use the `time_to_int()` method to support the comparison.
# ```

# In[ ]:


# Remove this line and add your code here


# Unfortunately, this implementation of addition is not commutative. If the integer is the
# first operand, you get an error message.

# In[ ]:


print(3630 + start)


# The problem is, instead of asking the `Time` object to add an integer, Python is asking an
# integer to add a `Time` object, and it does not know how. 
# 
# But there is a clever solution for this problem: the special method `__radd__`, which stands for “right-side add”. 
# 
# This method
# is invoked when a `Time` object appears on the right side of the `+` operator. 

# In[ ]:


class Time:
    """Represents the time of day."""

    def __init__(self, hour=0, minute=0, second=0) -> None:
        """ creates a new Time object and initializes it
        """
        (ignore, self.hour) = divmod(hour, 24)
        (ignore, self.minute) = divmod(minute, 60)
        (ignore, self.second) = divmod(second, 60)
        
    def __str__(self) -> str:
        """ creates a string from the current Time object
        """
        return '{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)
    
    def time_to_int(self) -> int:
        """ converts a Time object into an integer value respresenting seconds
        """
        minutes : int = 60 * self.hour + self.minute
        seconds : int = 60 * minutes + self.second
        return seconds
            
    def increment(self, seconds : int):
        """ increments a Time object with an amount of seconds (represented as an integer)
        """
        seconds += self.time_to_int()
        return int_to_time(seconds)
    
    def is_after(self, other) -> bool:
        """ checks whether the current time is after the given time
        """
        return self.time_to_int() > other.time_to_int()
    
    def add_time(self, other):
        """ adds a Time object to the current Time object
        """
        seconds : int = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
    
    def __add__(self, other : any):
        """ adds a Time object or an amount of seconds to the current Time object
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other : any):
        """ flips the arguments if needed
        """
        return self.__add__(other)
    
def int_to_time(seconds : int) -> Time:
    """ converts a values representing seconds into a Time object
    """
    time : Time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    
    # fix with hours if greater than 24
    if time.hour >= 24:
        time.hour -= 24
        
    return time


# In[ ]:


start : Time = Time(9, 45, 30)
print(3630 + start)
print(3630 + start + 363)


# ## Polymorphism
# 
# Type-based dispatch is useful when it is necessary, but (fortunately) it is not always necessary.
# 
# Often you can avoid it by writing functions that work correctly for arguments with different types.
# 
# Many of the functions we wrote for strings also work for other sequence types. 
# 
# In Section 11.2 we used `histogram` to count the number of times each letter appears in a word.

# In[ ]:


def histogram(s : list) -> dict:
    """ creates a histogram from a list of elements
    """
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c] + 1
    return d


# The function `histogram` works on a list of words.

# In[ ]:


t = ['data', 'science', 'statistics', 'machine', 'learning', 'computer', 'science']
histogram(t)


# Or on a list of prime numbers.

# In[ ]:


p = [3, 7, 11, 13, 3, 5, 23, 13, 3]
histogram(p)


# Functions that work with several types are called **polymorphic**.
# 
# Polymorphism can facilitate code reuse.
# 
# For example, the built-in function `sum`, which adds the elements of a
# sequence, works as long as the elements of the sequence support addition.
# 
# Since `Time` objects provide an `add` method, they work with `sum`.

# In[ ]:


t1 : Time = Time(7, 43)
t2 : Time = Time(7, 41)
t3 : Time = Time(7, 37)

total_time : Time = sum([t1, t2, t3])
print(total_time)

total_value : int = sum([3, 7, 11, 13, 3, 5, 23, 13, 3])
print(total_value)


# In general, if all of the operations inside a function work with a given type, the function
# works with that type.
# 
# The best kind of polymorphism is the unintentional kind, where you discover that a function
# you already wrote can be applied to a type you never planned for.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Let's analyse the `len()` function. create a list of integers and string and store each value on a different variable. Then call the function with each one of them. Can we say that the `len()` function is polymorphic or not?
# ```

# In[ ]:


# Remove this line and add your code here


# ## Interface and Implementation
# 
# One of the goals of object-oriented design is to make software more maintainable, which means that you can keep the program working when other parts of the system change, and modify the program to meet new requirements.
# 
# A design principle that helps achieve that goal is to keep interfaces separate from implementations. This is called **encapsulation**.
# 
# For objects, that means that the methods a class provides should not depend on how the attributes are represented.
# 
# For example, in this chapter we developed a class that represents a time of the day. 
# 
# Methods provided by this class include `time_to_int`, `is_after`, and `add_time`.
# 
# We could implement those methods in several ways. 
# 
# The details of the implementation
# depend on how we represent time. 
# 
# In this chapter, the attributes of a `Time` object are `hour`,
# `minute`, and `second`.
# 
# As an alternative, we could replace these attributes with a single integer representing the
# number of seconds since midnight. 
# 
# This implementation would make some methods, like
# `is_after`, easier to write, but it makes other methods harder.
# 
# After you deploy a new class, you might discover a better implementation. 
# 
# If other parts
# of the program are using your class, it might be time-consuming and error-prone to change
# the interface.
# 
# But if you designed the interface carefully, you can change the implementation without
# changing the interface, which means that other parts of the program do not have to change.
