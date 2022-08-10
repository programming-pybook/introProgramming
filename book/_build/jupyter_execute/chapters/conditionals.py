#!/usr/bin/env python
# coding: utf-8

# # Conditionals [^intro]
# 
# [^intro]: This Jupyter Notebook is based on Chapter 3 and 5 of {cite}`Severance2016`; and Chapter 5 and 7 of {cite}`thinkPython`.

# ## Boolean Expressions
# 
# A **boolean expression** is an expression that yields either `True` or `False`.
# 
# The following examples use the operator `==` to compare the values of two expressions.
# 
# The result is `True` if the values are the same, otherwise the result is `False`.

# In[1]:


5 == 5


# In[2]:


5 == 6


# `True` and `False` are special values of the type `bool`.

# In[3]:


True and False


# Beside the relational operator `==` we have
# 
# | **Operator** | **Purpose** |
# |:----------|:---------|
# | `==` | x is  equal to y |
# | `!=` | x is not equal to y |
# | `x > y` | x is greater than y |
# | `x < y` | x is less than y |
# | `x >= y` | x is greater than or equal to y | 
# 
# Although these operations are probably familiar to you, the Python symbols are different from the mathematical symbols. 
# 
# A common error is to use a single equal sign (`=`) instead of
# a double equal sign (`==`). 
# 
# Remember that `=` is an assignment operator and `==` is a relational
# operator.

# ## Logical Operators
# 
# There are three logical operators: `and`, `or`, and `not`. 
# 
# The semantics (meaning) of these operators is similar to their meaning in English. 
# 
# For example, `x > 0 and x < 10` is `True`
# only if `x` is greater than `0` *and* less than `10`.

# In[4]:


x = 9
x > 0 and x < 10


# `n % 2 == 0 or n % 3 == 0` is `True` if *either one or both* of the conditions are `True`, that is, if the number
# is divisible by `2` *or* `3`.

# In[5]:


n = 27
n % 2 == 0 or n % 3 == 0


# Finally, the `not` operator negates a boolean expression, so `not (x > y)` is `True` if `x > y` is
# `False`, that is, if `x` is less than or equal to `y`.

# In[6]:


x = 10
y = 15
not (x > y)


# Strictly speaking, the operands of the logical operators should be boolean expressions, but Python is not very strict. 
# 
# Any nonzero number is interpreted as `True`.
# 
# This flexibility can be useful, but there are some subtleties to it that might be confusing.
# 
# You might want to avoid it (unless you know what you are doing).

# If you use the boolean operators in the same expression you have to beware of the order of the boolean operators.
# 
# The order is as follows: `not` > `or` > `and`, again if in doubt *use brackets!*

# In[7]:


not False and True


# In[8]:


True or False and True


# ## Conditional Execution
# 
# In order to write useful programs, we almost always need the ability to check conditions
# and change the behavior of the program accordingly. Conditions allow us to change the execution flow in a program. 
# 
# **Conditional statements** provide us this functionality. 
# 
# The simplest form is the **if statement**.

# In[9]:


x = 10
if x > 0:
    print('x is positive')
print('x is an integer value')


# The boolean expression after the `if` is called the **condition**. 
# 
# If it is true, the indented statement is being executed.
# 
# If statements have the same structure as function definitions: a header followed by an indented body. 
# 
# Statements like this are called **compound statements**.

# What is printed when executing the following cells?

# In[10]:


x = 1
if x < 0:
    print('x is negative')
print('Hello Data Scientists')


# In[11]:


x = 1
if x < 0:
print('x is negative')
print('Hello Data Scientists')


# Where "normal" programming languages use brackets, for instance `{` and `}` in C or Java, Python uses **indentation** to group lists of instruction *blocks*.

# In[ ]:


x = -1
if x < 0:
    print('x is negative')
    print('Hello Data Scientists')


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Ask the age of a user with the <i>input</i> function. If the user is an adult (older than or equal to 18) print the message "Hi adult!".
# ```

# In[ ]:


# Remove this line and add your code here


# ## Alternative Execution
# 
# There is yet another if statement, namely to represent **alternative execution**.
# 
# There are 2 alternatives to execute and the evaluation of the expression determines which alternative
# needs to be executed.

# In[ ]:


x = 23

if  x % 2 == 0:
    print('x is even')
else:
    print('x is odd')


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Ask the age of a user with the <i>input</i> function. If the user is an adult (older than or equal to 18) print the message "Hi adult!", otherwise print the message "Hi kid!".
# ```

# In[ ]:


# Remove this line and add your code here


# ## Chained Conditionals
# 
# Sometimes there are more than 2 alternatives. 
# 
# In that case you can use a **chained conditional**. 

# In[ ]:


x = 4
y = 2

if  x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')


# `elif` is an abbreviation of `else if`.
# 
# Every condition is checked from top to bottom and as soon as one succeeds the corresponding branch is
# executed and the conditional terminates.
# 
# If more than one condition evaluates to `True` only the first branch for which the condition succeeds is executed.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Ask the age of a user with the <i>input</i> function. If the user is a kid (younger than 18) print the message "Hi kid!"; if the user is between 18 and 69 print the message "Hi adult!"; otherwise, print the message "Hi old pal!".
# ```

# In[ ]:


# Remove this line and add your code here


# ## Nested Conditionals
# 
# One conditional can also be nested within another.

# In[ ]:


x = 2
y = 2

if  x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')


# The outer conditional contains two branches. 
# 
# The first branch contains a simple statement.
# 
# The second branch contains another `if` statement, which has two branches of its own.
# 

# 
# ````{margin}
# ```{admonition} EXTRA
# Although the indentation of the statements makes the structure apparent, **nested conditionals**
# become difficult to read very quickly. 
# ```
# ````
# 

# 
# It is a good idea to avoid them whenever you can.
# 
# Logical operators often provide a way to simplify nested conditional statements.

# In[ ]:


x = 2

if  0 < x :
    if x < 10:
        print('x is a positive single-digit number')


# We can **refactor** this nested conditional by introducing the `and` operator in the logical expression.

# In[ ]:


x = 2

if  0 < x and x < 10:
    print('x is a positive single-digit number')


# We can **refactor** this nested conditional by merging the two conditions into `0 < x < 10`.

# In[ ]:


x = 3

if  0 < x < 10:
    print('x is a positive single-digit number')


# In[ ]:



print('Do something!')


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Can you refactor the following program so we avoid having nested conditionals?
# ```

# In[ ]:


# Modify this code
day = 2

if day < 3:
    print('The week just started')
else:
    if day <= 5:
        print('We are just in the middle of the week')
    else:
        if day < 7:
            print('The week is ending')
        else:
            print('It is a fact, the week ends today')


# ## Catching Exceptions
# 
# The following program request you to enter your age. Then, it parses the input as an integer. But what does it happen if you introduce a string instead of a number?

# In[ ]:


age = input('What is your age? ')
int(age)


# Indeed, you get an error or exception. 
# 
# Python can help you handle these cases to end the program gracefully, or continue trhough an alternative path. The construct that handles errors is called **try/except**.
# 
# We use the try/except when we know that a sequence of instructions might introduce an error (placed in the **try** section) and you want to execute other sequence in case the problem rises (placed in the **except** section). If no error appears, the except section is ignored. 
# 
# **Catching** is the action of handling an exception.
# 
# Now, let's rewrite our previous example with the try/except construct.

# In[ ]:


age = input('What is your age? ')

try: 
     print(int(age))
except:
    print('You should introduce a number!')


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Ask the user for two numbers (two calls of the <i>input</i> function can be used) so you can compute the addition of both of them. Then, print the message "<i>num_1</i> + <i>num_2</i> = <i>sum</i>". If the user inputs a value that cannot be converted to a number print the message "Please, enter a valid number."
# ```

# In[ ]:


# Remove this line and add your code here


# ## Short-circuit Evaluation of Logical Expressions
# 
# When Python processes a logical expression, it does it from left to right. 
# 
# So, for the expression `x > 0 and x < 10` it will first process `x > 0` and then `x <10`.
# 
# However, if it happens that `x = -1`, the first expression `x > 0` will be equal to `False` and tthen there is no point to evaluate the second expression. By definition, if one of the expression of an `and` is `False`, the whole expression is also `False`.
# 
# Python avoids processing extra expressions when the result is already known. This is know as **short-circuiting** the evaluation.

# Short-circuiting the evaluation lead to a useful technique known as the **guard pattern**. Let's see why it is needed with the following example.

# In[ ]:


x = 10
y = 5

x > 0 and x / y == 2


# Everything works fine until now. But what does it happen if we change the value of `y` to `0`?

# In[ ]:


x = 10
y = 0

x > 0 and x / y == 2


# Yes. We get an error because you cannot have `0` as a denominator in a division. We can use the guard pattern to place a **guard** expression that let us check if `y != 0`. Let's see what happens now.

# In[ ]:


x = 10
y = 0

x > 0 and y != 0 and x / y == 2


# No errors now because Python stops evaluating expressions when it notices that `y != 0 == False`. And this is the beauty of using the guard pattern.
