#!/usr/bin/env python
# coding: utf-8

# # Conditionals and Iteration [^intro]
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

# ## The `while` Statement
# 
# Computers are good in repeating boring tasks, they do this faster and more accurate than people.
# 
# Repetition of instructions is called **iteration** in programming.
# 
# Suppose you want to countdown and print a value, we need to *loop*.

# In[ ]:


# Countdown program

n = 10  # integer
print('initial n value =', n)
i = 0   # integer

while n > 0:
    print(n)
    n = n - 1
    
    i = i + 10
print('Ready, and value of i =', i)


# The flow of execution for a `while` statement is as follows:
# 
# 1. Determine whether the condition is `True` or `False`.
# 2. If `False`, exit the `while` statement and continue with the next statement.
# 3. If the condition is `True`, run the body and go back to step 1.
# 
# This type of flow is called a loop because the third step loops back around to the top.
# 
# The body should change the value of some variables that are used in the condition in order to ensure termination
# of a loop.

# In[ ]:


while True:
    print('Hello')


# The `while` loop above will never terminate, this is a so-called `infinite` loop.
# 
# When writing programs it is important to convince yourself that the program terminates.
# 
# In the case of `countdown`, we can prove that the loop terminates: if `n` is zero or negative, the
# loop never runs. Otherwise, `n` gets smaller each time through the loop, so eventually we
# have to get to 0.
# 
# Reasoning that loops terminate is not always trivial, consider for instance.

# In[ ]:


# sequence
n = 5   # integer
while n != 1:
    print(n)
    
    if n % 2 == 0: # n is even
        n = n / 2
    else: # n is odd
        n = n * 3 + 1


# The condition for this loop is `n != 1`, so the loop will continue until `n` is 1, which makes
# the condition `False`.
# 
# Since `n` sometimes increases and sometimes decreases, there is no obvious proof that `n` will
# ever reach 1, or that the program terminates. 
# 
# For some particular values of `n`, we can prove termination. 
# 
# For example, if the starting value is a power of two, `n` will be even every
# time through the loop until it reaches 1. 
# 
# The previous example ends with such a sequence,
# starting with 16.

# ## `break`
# 
# It is possible to enforce the termination of a loop via the `break` statement.
# 
# Suppose you are processing input and as soon as you get the string value `done` you want to terminate.

# In[1]:


count_words = 0

while True:
    line = input("> ")
    
    if line == 'done':
        break
        
    count_words = count_words + 1; print("Hello")
    
print(count_words)


# This way of terminating `while` loops is common practice, because you can check very easily whether some condition
# holds.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Try to rewrite the <i>while</i> loop without the <i>break</i> statement.
# ```

# In[ ]:


# Remove this line and add your code here


# ## `continue` 
# 
# Sometimes you don't want to finish the execution of the loop body for certain iterations.
# 
# In that case, you want to stop the current iteration and continue with the next one.
# 
# To do so, you can use the `continue` keyword.
# 
# Let's see how to use it with the following example. 

# In[ ]:


while True:
    instruction = input('What to do next? ')
    
    if instruction == 'quit':
        break
    
    if instruction == 'skip':
        continue
        print('Skip this line')
        
    print('Your instruction is ' + instruction)


# In this program we ask for input to the user and we print a message saying "Your instruction is `instruction`". However, if the input is equal to "quit", the program will end. Otherwise, if the input is equal to "skip", the current iteration will stop just before printing the message and will continue with the next iteration.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Try to rewrite the <i>while</i> loop without the <i>break</i> and <i>continue</i> statements.
# ```

# In[ ]:


# Remove this line and add your code here


# ## While Loops in Detail
# 
# Let's consider the following cell to understand the flow of control of a `while` loop.
# 
# * A `while` loop should always have a boolean expression (condition). In the cell  `x < 10` (see line `#2`), but `True` is also fine.
# * A `while` loop should have at least one statement in the body (see lines `#3` and `#4`). Beware only the indented statements are part of the body, line `#5` is not part of the body.
# * As long as the evaluation of the condition yields the boolean value `True` (see line `#2`), the statements
# in the body are executed (see lines `#3` and `#4`). After the execution of the body, the condition is re-evaluated. 
# If the evaluation of the condition yields the value `False`, the statement after the body is executed (see line `#5`).
# * Removing the indentation on line `#4` leads to a non-terminating loop. **Why?**

# In[ ]:


x = 0               #1
while x < 10:       #2
    print(x)        #3
    x = x + 1       #4
print("Done!")      #5


# The program above can be visualised as follows:
# 
# ```{image} assets/flowchart.png
# :alt: Flowchart of first while loop program
# :width: 250px
# :align: center
# ```
# 
# <div style="text-align:center">
#     <span style="font-size:0.9em; font-weight: bold;">Flowchart of the first while-loop program.</span>
# </div>
# <br>
# 
# Do you also want to see the `while` loop in action?

# ```{image} assets/while-animation.gif
# :alt: Animated while loop program
# :align: center
# ```
# 
# <div style="text-align:center">
#     <span style="font-size:0.9em; font-weight: bold;">Animmated while-loop program.</span>
# </div>
# <br>
# <br>

# 

# In[ ]:


x = 0               #1
while x < 10:       #2
    print(x)        #3
x = x + 1           #4
print("Done!")      #5


# The program above can be visualised as follows:
# 
# ```{image} assets/flowchart2.png
# :alt: Flowchart of second while loop program
# :width: 250px
# :align: center
# ```
# 
# <div style="text-align:center">
#     <span style="font-size:0.9em; font-weight: bold;">Flowchart of the second while-loop program.</span>
# </div>
# 

# * The execution of the loop can *always* be terminated via a `break` statement. See line `#6` in the cell below.
# * Often the `break` statement is used in combination with a conditional. See lines `#5` and `#6`.
# * This conditional should be part of the loop body, so intended.

# In[ ]:


x = 0               #1
while True:         #2
    print(x)        #3
    x = x + 1       #4
    if x >= 10:     #5
        break       #6
print("Done!")      #5


# The program above can be visualised as follows:
# 
# ```{image} assets/flowchart3.png
# :alt: Flowchart of third while loop program
# :width: 300px
# :align: center
# ```
# 
# <div style="text-align:center">
#     <span style="font-size:0.9em; font-weight: bold;">Flowchart of the third while-loop program.</span>
# </div>

# ## Square Roots
# 
# Loops are often used in programs that compute numerical results by starting with an approximate
# answer and iteratively improving it.
# 
# For example, one way of computing square roots is Newton’s method.
# 
# Suppose that you want to know the square root of $a$. 
# 
# If you start with almost any estimate, $x$, you can compute
# a better estimate with the following formula:
# 
# $y = \frac{x + a/x}{2}$
# 
# For example, if $a$ is 4 and $x$ is 3, we get:

# In[ ]:


a = 4
x = 3
y = (x + a / x) / 2
y


# The result is closer to the correct answer ($\sqrt{4} = 2$). If we repeat the process with the new
# estimate, it gets even closer

# In[ ]:


x = y
y = (x + a / x) / 2
y


# After a few more iterations the results gets more precise.

# In[ ]:


x = y
y = (x + a / x) / 2
y


# In[ ]:


x = y
y = (x + a / x) / 2
y


# After a couple more iterations the value of $y$ is equal to $x$ and thus we can stop.

# In[ ]:


x = 1
a = 4

while (True):
    print(x)
    y = (x + a / x) / 2
    
    if y == x:
        break
    
    x = y


# For most values of a this works fine, but in general it is dangerous to test equality on floating point numbers.
# 
# Floating-point values are only approximately right: most rational numbers, like 1/3, and
# irrational numbers, like $\sqrt{2}$ cannot be represented exactly with a float.
# 
# Rather than checking whether `x` and `y` are exactly equal, it is safer to use the built-in function
# abs to compute the absolute value, or magnitude, of the difference between them:

# In[ ]:


x = 3
a = 4
epsilon = 0.00000000000001

while (True):
    print(x)
    y = (x + a / x) / 2
    
    if abs(y - x) < epsilon:
        break
        
    x = y


# Where `epsilon` has a value like `0.00000000000001` that determines how close is close enough.

# ````{margin}
# ```{admonition} EXTRA
# See what happens if you play with the value of `epsilon`.
# ```
# ````

# Suppose we want to add all numbers to a number provided via input.

# In[ ]:


x = 1+2+3+4+5+6+7+8+9+10
print(x)


# In[ ]:


sx = input()

x = int(sx)

s = 0
while (x > 0):
    s = s + x
    print(s)
    x = x - 1
    print(x)

print(s)


# In[ ]:


inp = input("Give a number > 0:")
nr = int(inp)
print(nr)

cnt = 0
tot = 0
while (cnt <= nr):
    print(cnt)
    if (cnt % 2 == 0):
        tot += cnt
    cnt += 1
print(tot)
    

