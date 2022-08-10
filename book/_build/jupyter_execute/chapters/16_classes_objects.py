#!/usr/bin/env python
# coding: utf-8

# # Classes and Objects [^intro]
# 
# [^intro]: This Jupyter Notebook is based on Chapter 15 of {cite}`thinkPython`.

# There are multiple programming paradigms: **imperative**, **logical**, **functional**, and **object-oriented**, the logical and functional way of programming is sometimes called **declarative**.
# 
# So far, we have seen the imperative way of programming; creating data structures, and developing functions that manipulate the data structures. 
# 
# We will graduately introduce concepts from **object-oriented** programming.
# 
# The idea of object-oriented programming is to bring code and data closer together; this will increase the level of abstraction and facilitates encapsulation of data. 
# 
# Object-oriented (OO) paradigm enables information hiding, the underlying structure is invisible and the programmer can use, among others, so-called *getters* and *setters* to manipulate the data.

# ## 2. Programmer-defined Types
# 
# We have seen and used a number of built-in types of Python. 
# 
# We are now going to define our own types.
# 
# We will start by creating a type called `Point` that represents a point in a two-dimensional space.
# 
# In mathematical notation, points are often written in parentheses with a comma separating the coordinates. 
# 
# $(0, 0)$ represents the origin, and $(x, y)$ represents the point $x$
# units to the right and $y$ units up from the origin.
# 
# There are several ways we might represent points in Python:
# 
# * We could store the coordinates separately in two variables, `x` and `y`.
# * We could store the coordinates as elements in a list or tuple.
# * We could create a new type to represent points as objects.
# 
# Creating a new type is more complicated than the other options, but it offers numerous advantages as we will see later on.
# 
# A programmer-defined type is also called a **class**. 
# 
# The following cell shows the class definition for `Point`.

# In[1]:


class Point:
    """Represents a point in 2-D space."""


# A new class `Point` has been introduced. 

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Define the class *Dog*, which represents a dog (obviously). Include a docstring with the description of the class.
# ```

# In[2]:


# Remove this line and add your code here


# There is not much you can do so far with this `class Point`.
# 
# The body is a docstring that explains what the class defines or is used for.
# 
# Defining a class named `Point` creates a **class object**.

# In[3]:


Point


# Because `Point` is defined at the top level, its “full name” is `__main__.Point`.
# 
# The class object is like a **factory** for creating objects, it is a built-in mechanism that based on the class allocates pieces of memory to store the data. Every object is a separate allocated piece of memory.
# 
# To create a Point, you call `Point` as if it were a function.

# In[4]:


pnt = Point()
pnt


# The return value is a reference to a `Point` object, which we assign to the variable `pnt`.
# 
# Creating a new object is called **instantiation**, and the object is an **instance** of the class.
# 
# When you print an instance, Python tells you what class it belongs to and where it is stored in memory.
# 
# Every object is an instance of some class, so “object” and “instance” are interchangeable.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Create an instance of a Dog and assign its value to a the variable `doggy`.
# ```

# In[5]:


# Remove this line and add your code here


# ## Attributes
# 
# The class `Point` we have created in the previous section is not really useful. 
# 
# The next step is to assign values to an instance of the class `Point`.

# In[6]:


pnt.x : float = 3.0
pnt.y : float = 4.0


# The same syntax (notation) is used as for selecting a variable from a module, for instance `math.pi` or `string.whitespace`.
# 
# We use the `dot` notation to assign values to named elements of an object.
# 
# The elements are called **attributes**, see the corresponding visualisation of the corresponding **object diagram**.
# 
# |           | Point |
# |:----------|:----------|
# | pnt $\rightarrow$ | x $\rightarrow$ 3.0 |
# |   | y $\rightarrow$ 4.0 |
# 
# The variable `pnt` refers to a Point object, which contains two attributes. 
# 
# Each attribute refers to a floating-point number.
# 

# 
# ````{margin}
# ```{admonition} EXTRA
# Python is a dynamically typed language. This means you do not need to define the types of variables explicitly, Python will deduced them for you and report if there are inconsistencies. The **attributes** of a class do not need to be declared explicitly when creating a class.
# ```
# ````

# In[7]:


pnt.z : float = 5.0


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Add the attributes `name` and `breed` to the object doggy refers to. Set the values you prefer.
# ```

# In[8]:


# Remove this line and add your code here


# You can read the value of an attribute using the same syntax.

# In[9]:


print('x =', pnt.x)

y : float = pnt.y

print('y =', y)


# The expression `pnt.y` means, “Go to the object `pnt`
# refers to and get the value of `y`.” 
# 
# We assign that value to a variable named `y`. 
# 
# There is no conflict between the variable `y` and the attribute `y`;
# they live in 2 different worlds.
# 
# You can use dot notation as part of any expression, as we can see in the cells below.

# In[10]:


'(%g, %g)' % (pnt.x, pnt.y)


# In[11]:


import math

distance : float = math.sqrt(pnt.x**2 + pnt.y**2)
distance


# You can use an instance of a class as argument for a function in the usual way.
# 
# `print_point` takes a point as an argument and displays it in mathematical notation. 
# 
# To invoke it, you can pass `pnt` as an argument. 
# 
# The argument of the function has the type `Point`, the *type-hints* are very important to really document and understand the function.

# In[12]:


def print_point(p : Point) -> None:
    """prints a point object
    """
    print('(%g, %g)' % (p.x, p.y))
    
print_point(pnt)


# Inside the function, `p` is an alias for `pnt`, so if the function modifies `p`, `pnt` changes.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Create a function `print_dog(dog: Dog) -> None` that prints a message with the attributes of the dog. Use the dot notation to access the attributes of the dog object. Print a message that says: "This dog is called <i>name</i> and it is a <i>breed</i>". Use the doggy variable to verify the effect of your function.
# ```

# In[13]:


# Remove this line and add your code here


# ## The `init` Method
# 
# The init method (short for “initialization”) is a special method that gets invoked when an
# object is created. Its full name is `__init__` (two underscore characters, followed by
# init, and then two more underscores). 
# 
# Its purpose is to initialize a new object, this is the *constructor* method. When the object is created, for instance via `Time(11, 43, 51)`, the parameters are passed to the created object.
# 
# By convention, the first parameter of a method is called `self`.
# 
# An `init` method for the `Point` class is shown in the next cell.

# In[14]:


class Point:
    """Represents a point in 2-D space."""
    
    def __init__(self, x=0, y=0):
        """ creates a new Point object and initializes it
        """
        self.x : int = x
        self.y : int = y


# ## Rectangles
# 
# Sometimes it is obvious what the attributes of an object should be, but other times you have to make decisions. 
# 
# For example, imagine you are designing a class to represent rectangles.
# 
# What attributes would you use to specify the location and size of a rectangle? 
# 
# We assume that the rectangle is just in a vertical or horizontal position.
# 
# There are at least two possibilities:
# * You could specify one corner of the rectangle (or the center), the width, and the height.
# * You could specify two opposing corners.
# 
# At this point it is hard to say whether one is better than the other, so we will implement the first case, just as an example, so the combination of one corner with width and height.

# In[15]:


class Rectangle:
    """Represents a rectangle.
    
    attributes: width, height, corner.
    """
    
        
    def __init__(self, w=0, h=0, x=0, y=0):
        """ creates a new Point object and initializes it
        """
        self.width : float = w
        self.height : float = h
        self.corner : Point(x,y)


# The docstring lists the attributes: `width` and `height` are numbers; `corner` is a `Point` object that specifies the lower-left corner.
# 
# 
# ````{margin}
# ```{admonition} EXTRA
# Remember that Python is dynamically typed, the mentioning of the attributes in the docstring is not same as declaring them.
# ```
# ````

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Declare a new class called <i>DogOwner</i>. This class will have the following attributes: name, last_name, age, and dog. Include the docstring that describes this class.
# ```

# In[16]:


# Remove this line and add your code here


# To represent a rectangle, you have to instantiate a Rectangle object and assign values to the attributes.

# In[17]:


box : Rectangle = Rectangle(100.0, 100.0, 0, 0)
box.width : float = 100.0
box.height : float = 200.0
box.corner : Point = Point()
box.corner.x : float = 0.0
box.corner.y : float = 0.0


# The expression `box.corner.x` means, “Go to the object `box` refers to and select the attribute named `corner`; then go to that object and select the attribute named `x`.”
# 
# 
# |           | Rectangle |           |
# |:----------|:----------|:----------|
# | box $\rightarrow$ | width $\rightarrow$ 100.0 |  |
# |   | height $\rightarrow$ 200.0 | **Point**|
# |   | corner $\longrightarrow$ | x $\rightarrow$ 0.0 |
# |   |                          | y $\rightarrow$ 0.0 |
# 
# The figure shows the layout of this object. 
# 
# An object that is an attribute of another object is **embedded**.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Create a new dog owner and assign values to all of its attributes. Do not forget to assign values to his or her dog attributes!
# ```

# In[18]:


# Remove this line and add your code here


# ## Classes and Objects
# 
# Every class in Python is *derived* from the class `object`, so every *instance* of every class is an `object`.
# 
# The class `object` is a *superclass* of class `Rectangle`, and class `Rectangle` is a *subclass* of class `object`.
# 
# Class `object` has the following *attributes* (attributes are elements inside a class that refer to methods, functions, variables, or even other classes).

# In[19]:


dir(object)


# In[20]:


dir(Rectangle)


# If you compare these 2 lists, you observe that they are almost the same, except for `__dict__`, `__module__`, and `__weakref__`.
# 
# We can even get *help* on our `Rectangle` class.

# In[21]:


help(Rectangle)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Use the function `help()` to display the documentation of the class DogOwner.
# ```

# In[22]:


# Remove this line and add your code here


# ## Instances as Return Values
# 
# Functions can return instances. 
# 
# The function `find_center` takes a `Rectangle` as an argument
# and returns a `Point` that contains the coordinates of the center of the Rectangle.

# In[23]:


def find_center(rect : Rectangle) -> Point:
    """calculates the center of a rectangle
    """
    
    p : Point = Point()
    p.x : float = rect.corner.x + rect.width/2
    p.y : float = rect.corner.y + rect.height/2
    return p


# Here is an example that passes `box` as an argument and assigns the resulting `Point` to center.

# In[24]:


center : Point = find_center(box)
print_point(center)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Create the function `add_dog_lastname(owner: DogOwner) -> Dog`, which modifies the name of the dog by concatenating the last name of the owner to it. For example, if the dog's name is "Scooby" and the owner's last name is "Doo", the new name of the dog should be "Scooby Doo". Return the modified instance of the dog.
# ```

# In[25]:


# Remove this line and add your code here


# ## Objects are Mutable
# 
# You can change the state of an object by making an assignment to one of its attributes.
# 
# It is possible to change the size of a rectangle without changing its position.
# 
# In the cell below, the `width` and `height` are adapted.

# In[26]:


box.width = box.width + 50
box.height = box.height + 100


# You can also write functions that modify objects. 
# 
# For example, `grow_rectangle` takes a
# `Rectangle` object and two numbers, `dwidth` and `dheight`, and adds the numbers to the
# `width` and `height` of the rectangle.

# In[27]:


def grow_rectangle(rect : Rectangle, dwidth : int, dheight : int) -> None:
    """increases the size of the rectangle
    """
    rect.width += dwidth
    rect.height += dheight


# The next cell shows how to use this function and demonstrates its effect.

# In[28]:


print('width = ', box.width)
print('height = ', box.height)

grow_rectangle(box, 50, 100)
print('width = ', box.width)
print('height = ', box.height)


# Because `rect` is an alias for `box`, so if the function modifies `rect`, `box`
# changes as well.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Create the function `celebrate_birthday(owner : DogOwner)`, which adds 1 year to the age of the dog's owner. Do not return the new owner. Call the function and pass an instance of a DogOwner. Use the <i>print()</i> function to see how the attributes of the object have changes.
# ```

# In[29]:


# Remove this line and add your code here


# ## Copying
# 
# Aliasing can make a program difficult to read, it may even be dangerous, because changes in one place might have unexpected effects in another place. 
# 
# It is hard to keep track of all the variables that might
# refer to a given object and being changed unindented.
# 
# Copying an object is often an alternative to aliasing. 
# 
# The `copy` module contains a function
# called `copy` that can duplicate any object.

# In[30]:


p1 : Point = Point()
p1.x : float = 3.0
p1.y : float = 4.0

import copy
p2 : Point = copy.copy(p1)


# `p1` and `p2` contain the same data, but are different objects.

# In[31]:


print_point(p1)
print_point(p2)

p1 is p2


# The `is` operator indicates that `p1` and `p2` are not the same object, thus this explains the `False`.
# 
# The `==` operator is also defined for *programmer-defined types*, for 
# programmer-defined types the `==` and `is` operator have the same behaviour, although you may have expected differently.
# 
# The `==` operator yields `False` although these points contain the
# same data. 

# In[32]:


p1 == p2


# If you use `copy.copy` to duplicate a `Rectangle`, you will find that it copies the Rectangle object but not the embedded Point.

# In[33]:


box2 = copy.copy(box)
box2 is box


# In[34]:


box2.corner is box.corner


# |           | Rectangle |           |  Rectangle |           |
# |:----------|:----------|:----------|:----------|:----------|
# | box2 $\rightarrow$ | width $\rightarrow$ 100.0 |  |100 $\leftarrow$ width | $\leftarrow$ box|
# |   | height $\rightarrow$ 200.0 | **Point**|200.0 $\leftarrow$ height | | 
# |   | corner $\longrightarrow$ | x $\rightarrow$ 0.0 | $\longleftarrow$ corner ||
# |   |                          | y $\rightarrow$ 0.0 |||
# 
# The diagram above shows the object diagram.
# 
# The `copy.copy` operator is a so-called **shallow copy**.
# 
# It copies the object and any references it contains, but not the embedded
# objects.
# 
# In many cases this is not the desired behaviour, you want to copy the entire object structure.
# 
# In order to do that you need to use the `copy.deepcopy` function, this function implements the **deep copy**.

# In[35]:


box3 = copy.deepcopy(box)
box3 is box


# In[36]:


box3.corner is box.corner


# In[37]:


@Mark: make a view cells on the effect of changing copies.


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Create a dog owner instance, then create two copies of it: i) a shallow copy; and ii) a deep copy. Compare the dogs of the copies against the original dog with the <i>is</i> operator. What is the difference between both cases?
# ```

# In[ ]:


# Remove this line and add your code here

