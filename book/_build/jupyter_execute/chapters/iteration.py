#!/usr/bin/env python
# coding: utf-8

# # Iteration [^intro]
# 
# [^intro]: This Jupyter Notebook is based on Chapter 3 and 5 of {cite}`Severance2016`; and Chapter 5 and 7 of {cite}`thinkPython`.

# ## The `while` Statement
# 
# Computers are good in repeating boring tasks, they do this faster and more accurate than people.
# 
# Repetition of instructions is called **iteration** in programming.
# 
# Suppose you want to countdown and print a value, we need to *loop*.

# In[1]:


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

# In[2]:


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
    

