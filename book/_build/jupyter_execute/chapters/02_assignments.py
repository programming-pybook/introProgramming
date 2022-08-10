#!/usr/bin/env python
# coding: utf-8

# # Variables, expressions and assignments [^intro]
# 
# [^intro]: This Jupyter Notebook is based on Chapter 2 of the books Python for Everybody {cite}`Severance2016` and Think Python (Sections 5.1, 7.1, 7.2, and 5.12) {cite}`thinkPython`.

# ## Values and Types
# 
# A **value** is the basic unit used in a program. It may be, for instance, a number respresenting temperature. It may be a string representing a word.
# 
# Some values are 42, 42.0, and 'Hello, Data Scientists!'.
# 
# Each value has its own **type**: 42 is an integer (`int` in Python), 42.0 is a floating-point number (`float` in Python), and 'Hello, Data Scientists!' is a string (`str` in Python).
# 
# The interpreter can tell you the type of a value.
# 
# The function `type` takes a value as argument and returns its corresponding type.

# In[1]:


type(42)


# In[2]:


type(42.0)


# In[3]:


type('Hello Data Scientists!')


# Observe the difference between `type(42)` and `type('42')`!

# In[4]:


type('42')


# ## Assignment Statements
# 
# We have already seen that Python allows to evaluate expressions, for instance `40 + 2`. 
# 
# It is very convenient if we are able to store the calculated value in some variable
# for future use. 
# 
# An **assignment statement** creates a new variable and gives it a name.
# 
# 

# In[5]:


magicnumber = 40 + 2    
pi = 3.141592653589793  
message = 'Data is eating the world'  


# In[6]:


print(magicnumber)


# The example in the previous box contains three assignments. The first assign the value of the expression `40+2` to a new variable called `magicnumber`, the second assigns the value of π to the variable `pi`, and the last assignment assigns a string to the variable `message`.

# ````{margin}
# ```{admonition} EXTRA
# The type of the new variable is automatically derived from the expression in the left hand side. In contrast to other languages, Python does not offer a way of declaring the type of a variable explicitly. It may be good practice to add the types explicitly as comments.
# ```
# ````

# Programmers generally choose names for their variables that are meaningful—they document
# what the variable is used for.

# In[7]:


magicnumber = 40 + 2   # An integer
pi = 3.141592653589793 # A float
message = 'Data is eating the world' # A string


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Let's compute the volume of a cube if side $s = 5$. Remember that the volume of a cube is defined as $v = s^3$. Assign the value to a variable called `volume`.
# ```

# In[8]:


# Remove this line and add your code here


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Well done! Now, why don't you print the result in a message? It can say something like "The volume of the cube of side 5 is $volume$".
# ```

# In[9]:


# Remove this line and add your code here


# Beware that there is no checking of types (*type checking*) in Python, so a variable to which you have assigned an integer may be re-used as float.

# In[10]:


magicnumber = 40 + 2 # An integer 
print(type(magicnumber))

magicnumber = 3.141592653589793 # A float
print(type(magicnumber))

magicnumber = "Hello"
print(type(magicnumber))


# ## Variable Names and Keywords
# 
# Variable names can be as long as you like. They can contain both letters and numbers, but
# they cannot begin with a number.
# 
# The underscore character, `_`, can appear in a variable name. 
# It is often used in names with multiple words, such as `your_name` or `data_science_student`.
# 
# Some programmers prefer `doSomething`, others use `do_something`, and yet another group
# may use `dosomething`. It is important to be consistent in your naming convention, do not mix conventions, use the same naming convention for *variables* and *function names* (to be discuss later).
# 
# If you use illegal variable names you will get a syntax error.

# ````{margin}
# ```{admonition} EXTRA
# If you are developing software in a team, which will be very likely in the future, it makes sense to agree upon a number of basic principles. One of them is the **naming convention** principle.
# ```
# ````

# 
# These basic development principles are sometimes called **architectural rules**. 
# By defining and agreeing upon architectural rules you make it easier for you and your fellow developers to understand and modify your code.
# 
# If you want to read more on this, please have a look at **Code complete** a book by **Steven McConnell** {cite}`McConnell`.

# In[11]:


99ballons = 'Nena'


# In[9]:


largenr$ = 1000000


# You are not allowed to use Python **keywords** as variable names. 
# Every programming language has a collection of reserved **keywords**. They are used
# in predefined language constructs, such as *loops* and *conditionals*.
# These language concepts and their usage will be explained later.
# 
# The interpreter uses keywords to recognize these language constructs in a program.
# 
# Python 3 has the following keywords:
# 
# `False` `class` `finally` `is` `return` 
# 
# `None` `continue` `for` `lambda` `try` 
# 
# `True` `def` `from` `nonlocal` `while` 
# 
# `and` `del` `global` `not` `with` 
# 
# `as` `elif` `if` `or` `yield` 
# 
# `assert` `else` `import` `pass` `break`  
# 
# `except` `in` `raise`
# 

# In[11]:


while_nr = 'loop'


# ## Expressions and Statements
# 
# An **expression** is a combination of values, variables, and operators. 
# 
# A value all by itself is considered an expression, and so is a variable.

# In[12]:


42


# In[13]:


n = 17
n


# In[14]:


m = 27
m + 25


# In[15]:


k = 9
k * 37


# When you type an expression at the prompt, the interpreter **evaluates** it, which means that
# it calculates the value of the expression and displays it. 
# 
# In boxes above, `m` has the value `27` and `n + 25` has the
# value `52`.

# A **statement** is an instruction that has an effect, like creating a variable or displaying a value. 

# In[16]:


n = 17


# In[17]:


print(n)


# The first statement initialize the variable `n` with the value `17`, this is a so-called assignment statement. 
# 
# The second statement is a print statement and prints the value of the variable `n`.
# 
# The effect is not always visible. Assigning a value to a variable is not visible, but printing the value of a variable is.
# 
# Statements do not have values, but effects.

# ## Script Mode
# 
# So far we have run Python in **interactive mode** in these Jupyter notebook, which means that you interact directly with the interpreter in the **code cells**.
# 
# The interactive mode is a good way to get started, but if you are working
# with more than a few lines of code, it can be clumsy.
# 
# The alternative is to save code in a file called a script and then run the interpreter in 
# **script mode** to execute the script. 
# 
# By convention, Python scripts have names that end with `.py`.
# 
# Use the **Spyder** icon in **Anaconda Navigator** to create and execute stand-alone Python scripts.
# 
# Later in the course, you will have to work with Python projects for the assignments in order to get acquainted with another integrated development environment (PyCharm) for Python. 

# ## Order of Operations
# 
# Expressions may contain multiple operators. 
# 
# The order of evaluation depends on the **priorities of the operators** also known as **rules of precedence**.
# 
# For mathematical operators, Python follows mathematical
# convention. The acronym [PEMDAS](https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-arithmetic-operations/cc-6th-order-of-operations/a/order-of-operations-review) is a useful way to remember the rules:
# 
# + **Parentheses** have the highest precedence and can be used to force an expression to evaluate in the order you want. Since expressions in parentheses are evaluated first, `2 * (3 - 1)` is `4`, and `(1 + 1)**(5 - 2)` is `8`. You can also use parentheses to make an expression easier to read, even if it does not change the result.
# + **Exponentiation** has the next highest precedence, so `1 + 2**3` is `9`, not `27`, and `2 * 3**2` is `18`, not `36`.
# + **Multiplication** and **Division** have higher precedence than **Addition** and **Subtraction**. So `2 * 3 - 1` is `5`, not `4`, and `6 + 4 / 2` is `8`, not `5`.
# + Operators with the same precedence are evaluated from left to right (except exponentiation). So in the expression `degrees / 2 * pi`, the division happens first and the result is multiplied by `pi`. To divide by 2π, you can use parentheses or write: `degrees / 2 / pi`.

# ```{tip}
# :class: margin
# In case of doubt, *use parentheses!*
# ```
# 

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Let's see what happens when we evaluate the previous expressions. Just run the cell to check the resulting value.
# ```

# In[18]:


# Parentheses 1
2 * (3 - 1) 


# In[19]:


# Parentheses 2
(1 + 1)**(5 - 2)


# In[20]:


# Exponentiation 1
1 + 2**3


# In[ ]:


# Exponentiation 2
2 * 3**2


# In[ ]:


# MDAS 1
2 * 3 - 1


# In[ ]:


# MDAS 2
6 + 4 / 2


# In[ ]:


# Same precedence 1
degrees = 180
pi = 3.141592653589793
degrees / 2 * pi


# In[ ]:


# Same precedence 2
degrees / 2 / pi


# ## Floor Division and Modulus Operator
# 
# The floor division operator `//` divides two numbers and rounds down to an integer.
# 
# For example, suppose that driving to the south of France takes 555 minutes.
# 
# You might want to know how long that is in hours.
# 
# Conventional division returns a floating-point number.

# In[21]:


minutes = 555
minutes / 60


# Hours are normally not represented with decimal points. 
# 
# Floor division returns the integer number of hours, dropping the fraction part.

# In[22]:


minutes = 555
hours = minutes // 60
hours


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# You spoend around 225 minutes every week on programming activities. You want to know around how many hours you invest to this activity during a month. Use the $//$ operator to give the answer.
# ```

# In[ ]:


# Remove this line and add your code here


# The modulus operator `%` works on integer values. It computes the remainder when dividing the first integer by the second one. 

# In[23]:


remainder = minutes % 60
remainder


# The modulus operator is more useful than it seems. 
# 
# For example, you can check whether one number is divisible by another—if `x % y` is zero, then `x` is divisible by `y`.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# A child asks you the time. You check your digital clock and it says 17. The child does not understand what it means. Can you tell him what hour it is by using a number between 1 and 12? Use the % operator to solve this problem.
# ```

# In[ ]:


# Remove this line and add your code here


# ## String Operations
# 
# In general, you cannot perform mathematical operations on strings, even if the strings look like numbers, so the following operations are illegal: `'2'-'1'` `'eggs'/'easy'` `'third'*'a charm'`

# In[24]:


'2' - '1'


# But there are two exceptions, `+` and `*`.
# 
# The `+` operator performs string concatenation, which means it joins the strings by linking them end-to-end.

# In[27]:


first = 'data'
second = ' '
third = 'science'
first + ((second) + third)


# The `*` operator also works on strings; it performs repetition. 

# In[29]:


('Data' + ' ') * 3


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Speedy Gonzales is a cartoon known to be the <i>fastest mouse in all Mexico</i>. He is also famous for saying "Arriba Arriba Andale Arriba Arriba Yepa". Can you use the following variables, namely <i>arriba</i>, <i>andale</i> and <i>yepa</i> to print the mentioned expression? Don't forget to use the string operators.
# ```

# In[ ]:


arriba = "Arriba"
andale = "Andale"
yepa = "Yepa"

# Remove this line and add your code here


# ## Asking the User for Input
# 
# The programs we have written so far accept no input from the user. 
# 
# To get data from the user through the Python prompt, we can use the built-in function `input`.
# 
# When `input` is called your whole program stops and waits for the user to enter the required data. Once the user types the value and presses `Return` or `Enter`, the function returns the input value as a string and the program continues with its execution.
# 
# Try it out!

# In[30]:


inp = input()
inp * 3


# You can also print a message to clarify the purpose of the required input as follows.  

# ````{margin}
# ```{admonition} EXTRA
# The sequence `\n` at the end of the prompt represents a newline, which is a special character that causes a line break. That’s why the user’s input appears below the prompt.
# ```
# ````

# In[31]:


food = input('What is your favourite food? \n')
print('I love ' + food)


# The resulting string can be later translate as a different type, like an integer or a float. To do so, you use the functions `int()` and `float()`, respectively. But be careful, the user might introduce a value that cannot be converted to the type you required.

# In[32]:


age = input('What is your age? ')
print(int(age))
print(float(age))


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# We want to know the name of a user so we can display a welcome message in our program. The message should say something like "Hello $name$, welcome to our hello world program!".
# ```

# In[ ]:


# Remove this line and add your code here


# ## Comments
# 
# A program is more than just a list of instructions to be executed.
# 
# It is also a means of documenting your ideas and a means of communication to fellow software developers.
# So, it is very important to always add comments to your programs, how trivial they may seem. What is trivial today is complex tomorrow.
# 
# It is, therefore, a good idea to add notes to your programs to explain in natural language
# what the program is doing.
# 
# One challenge is not to write trivial comments, such as "the value 1 is assigned to the variable x".
# Such a comment is useless.
# 
# Another challenge is to keep comments up to date, so if you change a program make sure the comments are still valid. It is a nightmare to maintain software with outdated comments.
# 
# A Python comment starts with `#`, and extends to the end of the line.
# It is ignored during execution.

# In[ ]:


# This is a Python comment.


# In[ ]:


# compute the percentage of the hour that has elapsed
minute = 10
percentage = (minute * 100) / 60
print(percentage)


# In[ ]:


percentage = (minute * 100) / 60 # percentage of an hour


# By choosing the right variables names you make the code self-documenting, what is better the variable `v` or `velocity`?

# In[ ]:


velocity = 5 # in meters/second.


# ## Reassignments
# 
# It is allowed to assign multiple times a value to a variable, a so-called **reassignment**. 
# 
# As soon as you assign a value to a variable, the old value is lost.

# In[33]:


x = 42
print(x)

x = 43
print(x)


# The assignment operator `=` has a different semantics than equality operator `==`.
# 
# The assignment operator does not imply that two variables have refer to the same value.
# 
# The assignment of a variable to another variable, for instance `b = a` does not imply that
# if `a` is reassigned then `b` changes as well.

# In[34]:


a = 42
b = a # a and b have now the same value

print('a =', a)
print('b =', b)

a = 43 # a and b are no longer equal

print(a)
print(b)


# ````{margin}
# ```{admonition} EXTRA
# Reassigning variables is useful but one should take care. It may hinder understandability of the software.
# ```
# ````
# 

# ````{margin}
# ```{admonition} EXTRA
# As pointed out earlier, the type of the reassigned value does not need to have the same type of the original value.
# ```
# ````

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# You have a variable <i>salary</i> that shows the weekly salary of an employee. However, you want to compute the monthly salary. Can you reassign the value to the <i>salary</i> variable according to the instruction?
# ```

# In[ ]:


# Remove this line and add your code here


# ## Updating Variables
# 
# A frequently used reassignment is the **update**, the value of a variable depends on the previous value of the variable.

# In[35]:


print(x)
x = x + 1

print(x)


# This statement expresses "get the current value of `x`, add one, and then update `x` with the new value.”
# 
# Beware, that variable should be initialized first.

# In[36]:


y = y + 1
print(y)


# Before you can update a variable, you have to initialize it, usually with a simple assignment.

# ````{margin}
# ```{admonition} EXTRA
# It is a good practice whenever you *declare* a variable to initialize it and to add *comment* with the type of the variable.
# ```
# ````

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Do you remeber the salary excercise of the previous section (cf. 13. Reassignments)? Well, if you have not done it yet, update the <i>salary</i> variable by using its previous value.
# ```

# In[ ]:


# Remove this line and add your code here


# In[ ]:


y = 0   # integer
y = y + 1
print(y)


# Updating a variable by adding `1` is called an **increment**; subtracting `1` is called a **decrement**.

# In[38]:


z = 0    # integer
z += 100
print(z)


# In[39]:


z -= 1
print(z)

