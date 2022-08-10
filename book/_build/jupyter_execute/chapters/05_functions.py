#!/usr/bin/env python
# coding: utf-8

# # Functions [^intro]
# 
# [^intro]: This Jupyter Notebook is based on Chapter 4 of {cite}`Severance2016` and Chapters 3 and 6 of {cite}`thinkPython`.

# So far we have seen expressions, variables, simple and advanced statements. 
# 
# These language constructs allows us to write already quite complex programs and to perform advanced calculations. In fact, the first programming languages did not offer many more language constructs. However, there is more to learn and to improve the quality of the programs you will write in the future. An important concept in programming is *abstraction*.

# **Functions** play an important role when structuring instructions. **Functions** allows us to call a group
# of instructions over and over again, without copying-and-pasting these instructions. 
# 
# Furthermore, **functions** introduce *abstraction*, grouping of functionality by means of group instructions and giving a simple but meanful name to it, for instance, `print`. 
# 
# First we will show how **functions** can be called, later we show how to define our own functions.

# ## Function Calls
# 
# We have already seen examples of **function calls**, for instance:

# In[1]:


type(42)


# The name of this function is `type`. 
# 
# The expression in parentheses is called the **argument** of the function. 
# The result, for this function, is the type of the argument.
# 
# It is common to say that a function “takes” an argument and “returns” a result. The result
# is called the **return value**.

# ## Built-in Functions
# 
# Python has some built-in functions that we can use for free. 
# 
# For instance, it provides some functions to convert values from one type to another. 
# 
# The `int` function takes any value and converts it to an integer, if it can, or it will give an error message otherwise:

# In[2]:


int('32')


# In[3]:


int('Integer')


# `int` can convert floating-point values to integers, but it does not round off; it chops off the
# fraction part:

# In[3]:


int(3.9999)


# `float` converts strings and integers into floats.

# In[ ]:


float(32)


# In[ ]:


float('3.14159')


# `str` converts its argument into a string:

# In[ ]:


str(3.14159)


# There are other functions to compute the largest and smallest element in a list or string: `max` and `min`.

# In[4]:


max('I am a data scientist')


# In[5]:


min('I am a data scientist')


# Another common function is `len`, which returns the length of a list or a string.

# In[6]:


len('I am a data scientist')


# You should treat built-in functions as reserved words: don't use use their names to name variables.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Compute the length of the string "Twist and shout".
# ```

# In[ ]:


# Remove this line and add your code here


# ## Math Functions
# 
# The functions presented in the previous section are built-in functions. Every Python implementation will provide these functions. 
# 

# ````{margin}
# ```{admonition} EXTRA
# A **module** is yet another mechanism to structure your software, frequently used functions, such as Math functions, can be group together in a **module**.
# ```
# ````

# 
# Another way of providing predefined functions is via **modules**.
# 
# Python has a *math module* that provides most of the familiar mathematical functions. A
# **module** is a file that contains a collection of related functions.

# Before we can use the functions in a module, we have to import it with an import statement:

# In[7]:


import math


# This statement creates a **module object** named math. If you display the module object, you
# get some information about it:

# In[8]:


math


# If you want to learn more about the functions and constants defined in the Math module, see 
# https://docs.python.org/3/library/math.html. 
# 
# To execute one of the functions, you have to specify the name of the module and the name of the
# function, separated by a dot (also known as a period). This format is called **dot notation**.

# In[9]:


signal_power : int = 25
noise_power : int  = 5
ratio : float = signal_power / noise_power
decibels : float = 10 * math.log10(ratio)
print(decibels)


# The first example uses `math.log10` to compute a signal-to-noise ratio in decibels.

# The expression `math.pi` gets the variable `pi` from the math module. 
# 
# Its value is a floating point approximation of π in 15 digits.

# In[10]:


print(math.pi)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Use the <i>math</i> module to compute the square root of 361.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Random Numbers
# 
# Python provides the module `random` to generate pseudorandom numbers.
# 
# Pseudorandom numbers are not completely random because they are generated after a deterministic computation.
# 
# A computation is said to be **deterministic** if it always generates the same outputs for the same inputs.

# The `random` module provides the `random` function to generate a pseudorandom float bwteen 0.0 and 1.0 (including 0.0 but not 1.0).
# 
# The following function generates 5 pseudorandom numbers by using the `random` function. Run it multiple times to check its output:

# In[12]:


import random

i : int = 0
while i < 5:
    x = random.random()
    print(x)
    i+=1
    


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Use the `randint` function to generate 10 random integers between 20 and 80.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Composition
# 
# The program:

# In[ ]:


signal_power : int = 25
noise_power : int = 5
ratio : float = signal_power / noise_power
decibels : float = 10 * math.log10(ratio)
print(decibels)


# shown in the previous section, contains program elements in isolation.
# Every line introduces a new variable and the right hand side of the
# assignment is a rather trivial operation.
# 
# Programming languages offers facilities to compose operations and create
# more complicated expression.  

# For example, the argument of a function can be any
# kind of expression, including arithmetic operators:

# In[ ]:


degrees : float = 45.0
x : float = math.sin(degrees / 360.0 * 2 * math.pi)
print(x)


# And even function calls:

# In[ ]:


x : float = math.exp(math.log(x+1))
print(x)


# Almost anywhere you can put a value, you can put an arbitrary expression, with one exception:
# the left side of an assignment statement has to be a variable name. Any other
# expression on the left side is a syntax error (we will see exceptions to this rule later).

# In[13]:


hours : int = 2
minutes : int = hours * 60 # correct

minutes


# In[14]:


hours * 60 = minutes # wrong


# Furthermore, it is important to realise the order of execution. The arguments of
# functions are evaluated before the function is called. 
# 
# The arguments are evaluated
# from left to right. 
# 
# If in the arguments arithmetic operators, they are evaluated taking
# the priorities (PEDMAS) into consideration.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Re-write the program presented in the first cell of this section. Use functions composition to this aim.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Adding New Functions
# 
# So far, we have only been using existing Python functions, but it is also possible
# to define your own functions. 
# 
# This allows you to capture computations in functions in order to reuse them later.
# Functions are the mechanism to facilitate reuse. 
# 
# A lot of programmers are lazy and use the principle of *copy-and-paste*. 
# If they see a few lines of code that does the job, they copy and paste it, instead
# of creating a proper function. This behavior leads to *code clones* and code clones
# hamper maintenance in the long run. If it is one up to four statements it is fine, but
# if you copy and paste five or more statements please create a function.
# 
# A **function definition** specifies the name of a new function and the
# sequence of statements that run when the function is called.

# In[15]:


def print_hello():
    print("Hello")
    
print_hello()


# `def` is the keyword that indicates that you defined a new function.
# 
# The name of the new function, in this case, is `print_hello`.

# ````{margin}
# ```{admonition} EXTRA
# The rules for function names are the same as for variable names: letters, numbers and underscore are legal, but the first character cannot be a number. 
# ```
# ````

# You cannot use a keyword as the name of a function, and you should avoid having a variable and a function
# with the same name.

# The empty parentheses after the name indicate that this function does not take any arguments.
# 
# The first line of the function definition is called the **header**; the rest is called the **body**. 
# 
# The header has to end with a colon and the body has to be indented. 
# 
# By convention, indentation is always four spaces. 
# 
# The body can contain any number of statements.

# Defining a function creates a **function object**, which has type function:

# In[16]:


print(print_hello)


# In[17]:


type(print_hello)


# In[18]:


print_hello()


# You can define another function `print_name`

# In[19]:


def print_data_scientists():
    print("Data Scientists")
    
print_data_scientists()


# You can define a new function `print_greeting` that calls the other 2 functions.

# In[20]:


def print_greeting():
    print_hello()
    print_data_scientists()


# In[21]:


print_greeting()


# 
# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Define the function `compute_area()` that computes the area of a circle. It takes an integer representing the radio of a circle as argument. The return value is the area of the circle.
# ```

# In[ ]:


# Remove this line and add your code here


# ## docstring
# 
# A **docstring** is a string at the beginning of a function that explains the interface (“doc” is
# short for “documentation”).

# In[23]:


def print_squares():
    """ prints the squares of 1 up to 5
        and it does not return a value.
    """
    print("1, 4, 9, 16, 25")
    
print_squares()


# By convention, all docstrings are triple-quoted strings, also known as multiline strings
# because the triple quotes allow the string to span more than one line.
# 
# It is concise, but it contains the essential information someone would need to use this function.
# 
# It explains concisely what the function does (without getting into the details of how
# it does it). 
# 
# It explains what effect each parameter has on the behavior of the function and
# what type each parameter should be (if it is not obvious).
# 
# Writing this kind of documentation is an important part of interface design. 
# 
# A well designed interface should be simple to explain; if you have a hard time explaining one
# of your functions, maybe the interface could be improved.

# In[25]:


def print_squares():
    """ prints the squares of 1 up to 5.
    """
    i : int = 1
        
    while i < 6:
        print(i**2)
        i += 1
        
print_squares()


# ## Definitions and Uses
# 
# Pulling together the code fragments from the previous section, you get the following program.

# In[ ]:


def print_data_scientists():
    print("Data Scientists")
    
def print_hello():
    print("Hello")
    
def print_greeting():
    print_hello()
    print_data_scientists()
    
print_greeting()


# This program contains three function definitions: `print_hello`, `print_data_scientists` and `print_greeting`.
# 
# Function definitions get executed just like other statements, but the effect is that function objects are created. 
# 
# The statements inside the function do not run until the function is called, and the
# function definition generates no output.
# 
# You need to define a function before you can run it.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
#  Define a new function `print_bye()` that prints the word "Bye". Then define another function `print_all()` that uses twice the `print_hello()` function, once the `print_data_scientists()` function, and twice the `print_bye` function in that order.
# ```

# In[ ]:


# Remove this line and add your code here


# ````{margin}
# ```{admonition} EXTRA
# This is also the case in the Jupyter notebooks. If you forget to execute a *cell* than variables and functions defined in that cell are not available in later cells.
# ```
# ````

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

# ## Parameters and Arguments
# 
# Some of the functions require arguments. For instance, `math.sin` requires a number as argument.
# 
# Some functions take more than one argument. For instance, `math.pow` takes the base and exponent as arguments.
# 
# Inside the function, the arguments are assigned to variables called **parameters**.

# ````{margin}
# ```{admonition} EXTRA
# Python is a *dynamically typed language*, this means that the Python interpreter computes the types of variables and arguments.
# ```
# ````

# Python does not require to add types to the function arguments.
# 
# In this course, you are **required** to provide the types of the arguments of a function explicitly by means of *type hints* when they are known in advance! 

# In[26]:


def print_text_twice(text_arg : str):
    print(text_arg)
    print(text_arg)


# Currently Python does not use the type hints, but who knows...
# 
# In the next cell we do not know the type of the arguments, so we  provide the type `any`.

# In[27]:


def print_twice(text_arg : any):
    print(text_arg)
    print(text_arg)


# The function `print_twice` assigns the argument to a parameter named `text_arg`. 
# 
# When the function is called, it prints the value of the parameter (whatever it is) twice.
# 
# This function works with any value that can be printed.

# In[28]:


print_twice(42)


# In[29]:


print_twice(math.pi)


# In[30]:


print_twice('Data Science ' * 6)


# The argument is always evaluated before the function is called, so in the example, the expression `'Data Science ' * 6` is only evaluated once.
# 
# It is also possible to pass a variable as argument to a function parameter.
# 
# The name of the variable is independent of the name of the argument.

# In[31]:


cs_str : str = 'Computer Science'

print_twice(cs_str)


# ## Variables and Parameters
# 
# It is possible to create a local variable inside a function, which means that it only exists inside the function.

# In[32]:


def concat(part1 : str, part2 : str):
    cc_result : str = part1 + part2
    print_twice(cc_result)
    
concat('Data ', 'Science')


# You cannot use the local variables outside the function.

# In[33]:


print(cc_result)


# Local variables and parameters are invisible outside the function.

# In[35]:


print(part1)


# 
# Which value will the following code print?
# 

# In[36]:


greeting : str = "Hello!"

def print_greeting():
    greeting : str = "Hoi!"
    
print(greeting)


# ## Fruitful Functions and Void Functions
# 
# In "normal" programming language parlance a **fruitful function** is a **function** and a
# **void function** is a **procedure**. 
# 
# In Python both **function** and **procedure** are called **function**. 
# 
# A **fruitful function** is a function that returns a result. From now on, we will add the return type to the function definition via `-> type`.
# 
# A **void function** is a function that returns nothing.

# In[37]:


import math
math.sqrt(5)


# In order to "capture" the value you have to assign the result of the function to a variable.

# In[38]:


result : float = math.sqrt(5)
print(result)


# Void functions might display something on the screen or have some other effect, but they
# do not have a return value. 
# 
# So, it makes no sense to call a void function in the right hand side of an assignment statement.
# 
# If you assign the result to a variable, you get a special value
# called `None`.

# In[39]:


ai : str = print_twice('Artifial Intelligence')


# In[40]:


print(ai)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Identify the fruitful and the void function.
# ```

# In[ ]:


def sum(x: int, y: int) -> int:
    return x + y

print(sum(1, 2))


# In[ ]:


def sum(x: int, y: int) -> None:
    print(x + y)

sum(1, 2)


# ## Boolean Functions
# 
# So far, we have seen **fruitful functions** returning integer and floating-point values.
# 
# Functions can also return booleans.

# In[41]:


def is_divisible(x : int, y : int) -> bool:
    """calculates whether x is divisible by y"""
    
    print(x % y)
    if x % y == 0:
        return True
    else:
        return False
    
is_divisible(6, 3)


# The result of the `==` operator is a boolean, so the `is_divisible` function can be more concise.

# In[42]:


def is_divisible(x : int, y : int) -> bool:
    """caculates whether x is divisible by y"""
    
    return x % y == 0

is_divisible(6, 3)


# Functions return boolean values can be used in conditional expressions.

# In[43]:


x : int = 10
y : int = 5
if is_divisible(x, y):
    print('x is divisible by y')


# It is not neccesary to have to write the conditional expression as `is_divisible(x, y) == True`.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Create a function that checks if a number is greater than another number. Use it in an if statement. If the number is greater print the message "*num1* is greater than *num2*", otherwise print "*num1* is equal or less than *num2*".
# ```

# In[ ]:


# Remove this line and add your code here


# ## Return Values
# 
# Many functions in Python, such as the math functions, produce return values.
# 
# The functions that do not return a value, and are so-called `void` functions.
# 
# If we want to use the result of a function call in an expression, the function has to return a value.
# 
# The first example is the function `area`, which returns the area of a circle with the given radius:

# In[44]:


import math

def area(radius : int) -> float:
    """calculates the size of a circle given its radius
    """
    
    sz : float = math.pi * radius**2
    return sz

size : float = area(5)
print(size)


# We have seen the `return` statement before, but in a fruitful function the return statement
# includes an expression. 
# 
# This statement means: “Return immediately from this function
# and use the following expression as a return value.” 
# 
# The expression can be arbitrarily
# complicated, so we could have written this function more concisely:

# In[45]:


def area(radius : int) -> float:
    """calculates the size of a circle given its radius
    """
    return math.pi * radius**2

print(area(5))


# ````{margin}
# ```{admonition} EXTRA
# **Temporary variables** makes debugging a function more easy. You can print intermediate results.
# ```
# ````

# 
# Sometimes it is useful to have multiple return statements, one in each branch of a conditional.
# 
# Some programmers, and I am one of them, have a different opinion, they claim that for understandability it is better to have just one `return` statement in a function.

# In[46]:


def absolute_value(x : int) -> int:
    """transforms a negative value into a positive value
    """
    
    if x < 0:
        return -x
    else:
        return x
    

y = absolute_value(-10)
print(y)


# Since these `return` statements are in different branches of the condition, only one branch is executed.
# 
# As soon as a `return` statement is executed, the function terminates without executing any following statements. 
# 
# Statements that appear after a return statement, or any other place the flow
# of execution cannot reach, is called **dead code**.
# 
# In a fruitful function, it is a good idea to ensure that every possible path through the program hits a `return` statement

# In[49]:


def absolute_value(x : int) -> int:
    """transforms a negative value into a positive value
    """
    if x < 0:
        return -x
    if x > 0:
        return x
    
x = absolute_value(-10)
print(x+x)


# This function is incorrect because if `x` happens to be `0`, neither condition is `True`, and the
# function ends without reaching a `return` statement.
# 
# If the flow of execution gets to the end of a function, the return value is `None`, which is not the absolute value of 0.

# In[ ]:


val : int = absolute_value(0)
print(val)


# ## Function Composition
# 
# Let's see an example of function composition.
# 
# Suppose you want to develop a function that calculates the area of a circle based on the center
# of the circle and a point on the perimeter.
# 
# Suppose the center point of the circle is `(xc, yc)` and the point on the perimeter is `(xp, yp)`.
# 
# The first step is to calculate the radius of the circle.
# 
# We have created the two relevant functions `distance` and `circle_area`.

# In[50]:


def distance(x1 : int, y1 : int, x2 : int, y2 : int) -> float:
    """calculates the distance between 2 2-dimensional point
    """
    
    dx : int = x2 - x1
    dy : int = y2 - y1
    dsquared : int = dx**2 + dy**2
    result : float = math.sqrt(dsquared)
    
    return result

def circle_area(xc : int, yc : int, xp : int, yp : int) -> float:
    """calculates the area of a circle based on the center and
    a point on the circle"""
    radius : float = distance(xc, yc, xp, yp)
    result : float = area(radius)
    return result

circle_area(1, 3, 4, 6)


# The `circle_area` function can be refactor in order to get rid of the local variables.

# In[ ]:


def circle_area(xc : int, yc : int, xp : int, yp : int) -> float:
    """calculates the area of a circle based on the center and
    a point on the circle"""
    
    return area(distance(xc, yc, xp, yp))

circle_area(1, 3, 4, 6)


# ## Encapsulation
# 
# If you want to re-use statements, you have to capture them in a function.

# In[51]:


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

# In[53]:


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

# In[55]:


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

# In[ ]:


print_important_message(freq=7, discipline1='Computer science', discipline2='Statistics')


# ## Checking Arguments
# 
# When calling a function we have to ensure that the arguments that we pass to the function are 'correct'.
# 
# Therefore, it is necessary to write auxilary code to perform some checking on the arguments,
# to ensure that the given argument does not lead to unwanted behaviour.

# In[56]:


def countdown(nr : int) -> None:
    """print numbers in a decreasing order"""
    while (nr != 0):
        print(nr)
        nr -= 1
    print("Done!")


# In[57]:


countdown(15)


# In[ ]:


countdown(-15)


# In[ ]:


countdown(1.5)


# It looks like an infinite computation. How can that be? The function has a condition—when 
# `n != 0`. But if `n` is not an integer or negative, the condition will never be met.
# 
# From there, it gets smaller (more negative), but it will never be 0.
# 
# We can solve this problem by checking the type of the argument of `countdown` function. 

# In[58]:


def countdown(nr : int) -> None:
    """print numbers in a decreasing order"""
    
    if not isinstance(nr, int):
        print('countdown is only defined for integers.')
    elif nr < 0:
        print('countdown is not defined for negative integers.')
    else:
        while (nr != 0):
            print(nr)
            nr -= 1
    print("Done!")


# In[59]:


countdown(-1.5)


# The first condition handles non-integers; the second handles negative integers. In both
# conditions, the program prints an error message to indicate that something
# went wrong.
# 
# This program demonstrates the guardin pattern. The first two conditionals
# act as guardians, protecting the code that follows from values that might cause an
# error. 
# 
# The guardians make it possible to prove the correctness of the code.

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

# In[ ]:


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

# In[ ]:


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
