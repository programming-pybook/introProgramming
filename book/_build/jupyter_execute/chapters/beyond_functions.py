#!/usr/bin/env python
# coding: utf-8

# # Beyond Functions [^intro]
# 
# [^intro]: This Jupyter Notebook is based on Chapter 4 of {cite}`Severance2016` and Chapters 3 and 6 of {cite}`thinkPython`.

# ## Why Functions?
# 
# It may not be clear why it is worth the trouble to divide a program into functions. There
# are several reasons:
# 
# * Creating a new function gives you an opportunity to name a group of statements,
# which makes your program easier to read and debug.
# * Functions can make a program smaller by eliminating repetitive code. Later, if you
# make a change, you only have to make it in one place.
# * Dividing a long program into functions allows you to debug the parts one at a time
# and then assemble them into a working whole.
# * Well-designed functions are often useful for many programs. Once you write and
# debug one, you can reuse it.

# ## Flow of Execution
# 
# Functions have to be defined before they can be executed, this is similar to a variable
# definition. You cannot use a variable in the right hand side of an assignment if it is
# not introduced in the left hand side of a preceding assignment.
# 
# The execution of a Python script/progam always starts with the first statement of
# the program, this is also called the *flow of execution*.
# 
# Statements are run one at a time (*sequential*), from top to bottom.

# Function definitions do not alter the flow of execution of the program, but remember that
# statements inside the function do not run until the function is called.
# 
# You could consider a function call as a *detour* in the flow of execution of a program. 
# 
# Instead of going to the next statement,
# the flow jumps to the body of the function, runs the statements there, and 
# continues with the execution of the statements after the function call.
# 
# That sounds simple enough, until you remember that one function can call another. 
# 
# While in the middle of one function, the program might have to run the statements in another
# function. 
# 
# Then, while running that new function, the program might have to run yet another function, and so!
# 
# In principle this is going to stop because there are a finite number of functions.

# ## Encapsulation
# 
# If you want to re-use statements, you have to capture them in a function.

# In[1]:


def print_important_message():
    i : int = 0
    while i < 7:
        print('Computer science is important')
        print('Data science is more important')
        i += 1
        
print_important_message()


# Wrapping a piece of code up in a function is called **encapsulation**. 
# 
# One of the benefits of encapsulation is that it attaches a name to the code, which:
# 1. serves as a kind of documentation; and
# 2. facilitates re-use.
# 
# It is more concise to call a function multiple times than to **copy-and-paste** the code fragment of body multiple times!

# ````{margin}
# ```{admonition} EXTRA
# At this point we are going to be more strict than the books of the course.
# We are going to define explicitly the type of the arguments, in case of `important_message` the type of the argument is an `integer` value and therefor we use the type `int`. If the function returns a result, so we are dealing with *fruitful functions*, then we define the type of the result of the function by means of `-> type`. In case of `important_message` no value is returned. In this case we use `-> None`.
# ```
# ````

# ## Generalization
# 
# Suppose we want to re-use the function `important_message`, but with a different number of printed messages.

# In[2]:


def print_important_message(freq : int) -> None:
    i : int = 0
    while i < freq:
        print('Computer science is important')
        print('Data science is more important')
        i += 1
        
print_important_message(6)
print_important_message(17)


# Adding a parameter to a function is called generalization because it makes the function
# more general: in the previous version, the messages are printed 7 times; in this version it
# can be any number.
# 
# Another step in the generalization is to make the disciplines flexible. 

# In[3]:


def print_important_message(freq : int, discipline1 : str, discipline2 : str):
    i : int = 0
    while i <  freq:
        print(discipline1 + ' is important')
        print(discipline2, 'is more important')
        i += 1
        
print_important_message(3, 'Artificial intelligence', 'Statistics')


# When a function has more than a few numeric arguments, it is easy to forget what they are,
# or what order they should be in. 
# 
# In that case it is often a good idea to include the names of
# the parameters in the argument list:
# important_message(freq=7, discipline1='Computer science', discipline2='Statistics')
# 
# These are called keyword arguments because they include the parameter names as “keywords”
# (not to be confused with Python keywords like while and def).
# 
# This syntax makes the program more readable. 
# 
# It is also a reminder about how arguments
# and parameters work: when you call a function, the arguments are assigned to the parameters.

# In[4]:


print_important_message(freq=7, discipline1='Computer science', discipline2='Statistics')


# ## Interface Design
# 
# The **interface** of a function is a summary of how it is used: 
# * What are the parameters and their types? 
# * What does the function do? 
# * What is the return value and its type, if any? 
# 
# An interface is “clean” if it allows the caller to do what they want without dealing with unnecessary details of
# the body of the function.
# 
# A good interface can be defined by choosing a good name for the function and for its parameters and by providing the types of its arguments and result.
# 
# A short description, via comments, of the basic functionality of the function is also useful. This description can include the restrictions (so-called **pre-conditions**) for calling the function.

# ## Refactoring
# 
# After you have written a program it makes sense to study the code and see whether there are opportunities to improve the structure of the code. 
# 
# If you have copied and pasted instructions, it is advisable to introduced a separate function.
# 
# It may also be the case that you developed a function with a complex and bulky body. Then, consider the introduction of auxilary functions.
# 
# All these improvements are **refactorings**. 
# 
# Once you start coding, you understand the problem better. 
# 
# Sometimes refactoring is a sign that you have learned something.

# ## A Development Plan
# 
# A development plan is a process for writing programs. 
# 
# The process we use is “encapsulation and generalization”. 
# 
# The steps of this process are:
# 1. Start by writing a small program with no function definitions.
# 2. Once you get the program working, identify a coherent piece of it, encapsulate the
# piece in a function and give it a name.
# 3. Generalize the function by adding appropriate parameters.
# 4. Repeat steps 1–3 until you have a set of working functions. Copy and paste working
# code to avoid retyping (and re-debugging).
# 5. Look for opportunities to improve the program by refactoring. For example, if you
# have similar code in several places, consider factoring it into an appropriately general
# function.
# 
# This process has some drawbacks—we will see alternatives later—but it can be useful if
# you do not know ahead of time how to divide the program into functions. This approach
# lets you design as you go along.

# ## Incremental Development
# 
# The larger the program you need to develop the more useful it is to have a structured way of developing it.
# 
# There are multiple ways of structuring the development process and in fact your computational thinking. 
# 
# An important development paradigm is **divide and conquer**. You can, for example, try to split the problem in subproblems and solve each subproblem in isolation. This paradigm works for large and complex problems, furthermore, it allows parallel development of a program.
# 
# However, before applying any development paradigm you need to understand the problem. Critical reading is essential, making sketches to visualise the problem and the solution, explain the solution to somebody else, and finally write the code.
# 
# Another paradigm, as advocated by "Think Python" is to use incremental development.
# 
# The idea is not to try develop a complete program in one go, but to develop it step by step.
# 
# Along the way you can write small tests to see whether you program behaves correctly.
# 
# Developing a complete program is likely to fail and you will spend a lot of time on debugging.

# 
# As an example, suppose you want to calculate the volume of a hollow cylinder, so a cylinder with an inner cylinder removed. 
# 
# So, the problem we have to solve is subtracting the volume of the inner cylinder from the volume of the outer cylinder. The volume of a cylinder is can be calculated by $volume = h*\pi*R^2$.
# 
# So, can we now mathematical formulate the problem?
# 
# $volume = h (\pi R^2 - \pi r^2)$
# 
# 
# ```{image} assets/hollow-cylinder.png
# :alt: Cylinder
# :align: center
# ```
# 
# The first step is to consider how a function to calculate the volume of a hollow cylinder should look like in Python. 
# 
# In other words, what are the inputs (parameters) and what is the output (return value)?
# 
# A first try is to write a function with three numbers, which represent the radius of
# the two cylinders and their heights, the result is a floating-point value.

# In[5]:


def volume(outerRadius : int, innerRadius : int, height : int) -> float:
    """calculates the volume of a hollow cylinder based 
    on the radius of the outer and inner cylinder"""
    
    return 0.0

volume(3, 1, 3)


# This function is obviously not correct, it does not calculate the value of a hollow cylinder, it just returns `0.0`.
# 
# However, we have now a skeleton of the function.
# 
# So, in the next step we can start developing the body of the function.
# 
# We need first to calculate the volume of a single cylinder based on the radius and
# the height. 
# 
# We introduce two auxilary variables `surfaceC1` and `surfaceC2`.
# 
# Furthermore we add a `print` statement to see whether the values make sense.

# In[6]:


def volume(outerRadius : int, innerRadius : int, height : int) -> float:
    """calculates the volume of a hollow cylinder based 
    on the radius of the outer and inner cylinder"""
    
    surfaceC1 : float = math.pi * outerRadius**2
    surfaceC2 : float = math.pi * innerRadius**2
    print('surfaceC1 is', surfaceC1)
    print('surfaceC2 is', surfaceC2)
    
    return 0.0

volume(3, 1, 4)


# The next step is to calculate the difference of the surfaces.

# In[ ]:


def volume(outerRadius : int, innerRadius : int, height : int) -> float:
    """calculates the volume of a hollow cylinder based 
    on the radius of the outer and inner cylinder"""
    
    surfaceC1 : float = math.pi * outerRadius**2
    surfaceC2 : float = math.pi * innerRadius**2
    diffSurfaces = surfaceC1 - surfaceC2
    print('diffSurfaces is', diffSurfaces)
    
    return 0.0

volume(3, 1, 4)


# Then, we add a statement for multiplying the obtained difference with the height.

# In[ ]:


def volume(outerRadius : int, innerRadius : int, height : int) -> float:
    """calculates the volume of a hollow cylinder based 
    on the radius of the outer and inner cylinder"""
    
    surfaceC1 : float = math.pi * outerRadius**2
    surfaceC2 : float = math.pi * innerRadius**2
    diffSurfaces : float = surfaceC1 - surfaceC2
    print('diffSurfaces is', diffSurfaces)
        
    return height * diffSurfaces

volume(3, 1, 4)


# The last step is to make sure that if the outer radius is smaller than the inner radius. Thus, we return `0` instead of a negative volume and print an error message.

# In[ ]:


def volume(outerRadius : int, innerRadius : int, height : int) -> float:
    """calculates the volume of a hollow cylinder based 
    on the radius of the outer and inner cylinder, using
    outerRadius >= innerRadius"""
    
    if outerRadius >= innerRadius:
        surfaceC1 : float = math.pi * outerRadius**2
        surfaceC2 : float = math.pi * innerRadius**2
        diffSurfaces : float = surfaceC1 - surfaceC2
        
        volumeCylinder : float = height * diffSurfaces
    else:
        print("The outer cylinder should be larger than the inner cylinder")
        
        volumeCylinder : float = 0
        
    return volumeCylinder

volume(3, 1, 4)


# The final version of the function does not display anything when it runs; it only returns
# a value, or prints an error message.
# 
# The `print` statements we wrote are useful for debugging, but once you get the
# function working, you should remove them. 
# 
# Code like that is called **scaffolding** or **refactor** because it
# is helpful for building the program but is not part of the final product.
# 
# When you get more experienced, you will add more statements in one 'run' and use less debug statements.
# 
# The key points of the incremental approach are:
# 
# 1. Start with a working program and make small incremental changes. At any point, if
# there is an error, you should have a good idea where it is.
# 2. Use variables to hold intermediate values so you can display and check them.
# 3. Once the program is working, you might want to remove some of the scaffolding or
# consolidate multiple statements into compound expressions, but only if it does not
# make the program difficult to read.
