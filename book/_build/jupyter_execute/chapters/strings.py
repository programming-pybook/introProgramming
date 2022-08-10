#!/usr/bin/env python
# coding: utf-8

# # Strings [^intro]
# 
# [^intro]: This Jupyter Notebook is based on Chapter 6 of {cite}`Severance2016` and Chapter 8 of {cite}`thinkPython`.

# ## What is a String?
# 
# We have seen and used most of the language constructs Python offers.
# 
# The next step in programming is how to represent data. 
# 
# We have seen so far a number of basic data types: integers, floats, and booleans.
# 
# However, we will need more powerful data types to describe and manipulate data. For instance,
# if we want to calculate the average of a list of integers, the basic data types are not sufficient.
# 
# We will start with *strings*, which is a (non-basic) data type (`str`) in Python. 
# 
# A string represents a **sequence** of characters.
# 
# You can consider a *sequence* as a list of elements, we will see *lists* later on.
# 
# One of the operations that we can perform on strings is selecting one of the characters, via *indexing*.

# In[1]:


bike : str = 'gazelle'
letter = bike[1]
letter


# The second statement selects character number 1 from `bike` and assigns it to `letter`.
# 
# The expression in square brackets is called an **index**. 
# 
# The index indicates which character in the sequence you want (hence the name).
# 
# The index `1` does not yield the first letter of `gazelle`, but the second.
# 
# The first letter of a string is obtained by index `0`.

# In[2]:


letter = bike[0]
letter


# So `g` is the 0th letter of `'gazelle'`, `a` is the 1st letter, `z` is the 2th
# letter, and so on. 
# 
# The following table presents the index of each letter in the string `'gazelle'`.
# 
# | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
# |---|---|---|---|---|---|---|
# | g | a | z | e | l | l | e |

# As an index you can use an expression that contains variables and operators:

# In[3]:


i : int = 0
letter = bike[i]
print(letter)
i += 1
letter = bike[i]
print(letter)
i += 1
letter = bike[i]
print(letter)


# The value of the index **must** be an integer.

# In[4]:


letter = bike[1.5]


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Assign the value 'Maurits Cornelis Escher' to the variable <i>artist</i>. Then, print the first letter of the first, middle and last name of the artist.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Length of a String
# 
# There are more operations that we can apply on a sequence, such as calculating the length of a sequence (or string).
# 
# `len` is a built-in function to obtain the length of a sequence, and thus of a string.

# In[ ]:


len(bike)


# In[ ]:


len('gazelle')


# Given the fact that the first letter is accessed via the index `0`, the last letter is accessed via `len - 1` instead, as you may have expected.

# In[ ]:


length : int = len(bike)
bike[length]


# In[ ]:


bike[length - 1]


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Make sure you have declared the variable `artist`and you have assigned it the value 'Maurits Cornelis Escher'. Then, print the penultimate (second last) and antepenultimate (third last) letters of the artist name.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Traversal with a `for` Loop
# 
# Programs often involve processing a string by reading its characters one by one.
# 
# Often they start at the beginning, select each character, do something to the selected character, and continue until the end of the string. 
# 
# This pattern of processing is called a **traversal** of a sequence (or string). 
# 
# One way to write a traversal is with a `while` loop. Note that we need an explicit *iterator* in order to access all elements of the sequence (or characters of the string).
# 
# The next cell contains a correct implementation for iterating over a string with a `while` loop.

# In[ ]:


index : int = 0
while index < len(bike):
    letter = bike[index]
    print(letter)
    index += 1


# However, using an explicit iterator often introduces serious mistakes in programs. For example, programmers start at the wrong index (`1` instead of `0`) and terminate to early or to late.
# 
# So-called **out-of-bound** errors, or **off-by-one** errors are the root cause for serious security threats.
# 
# Below you find code that contains multiple **out-of-bound** errors.

# In[ ]:


index : int = 1
while index <= len(bike):
    letter = bike[index]
    print(letter)
    index += 1


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Make sure you have declared the variable `artist` and you have assigned it the value 'Maurits Cornelis Escher'. Then, only print the characters located in an even position. Use a `while` loop.
# ```

# In[ ]:


# Remove this line and add your code here


# Another way (and more secure) way of writing a traversal is using a `for` loop.
# 
# A `for` loop has an implicit iterator, in the cell below represented by the variable `letter`.

# In[ ]:


for letter in "sparta":
    print(letter)


# Each time the loop is executed, the next character in the string is assigned to the *iterator* (variable) `letter`. 
# 
# The loop continues until no characters are left.
# 
# The following example shows how to use concatenation (string addition) and a `for` loop
# to generate a list of names in alphabetical order. 

# In[ ]:


prefixes : str = 'JKLMNOPQ'
suffix : str = 'ack'

for letter in prefixes:
    print(letter + suffix)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# There is a hidden text in the following cell. To find the hidden message you should print all characters in the variable `code` except for those that are equal to 'x', 'y', or 'z'. Use a `for` loop to solve this problem.
# ```

# In[ ]:


code = 'Esxzcxxhyezrzy wyzyaxsz zyxbxoxrxxn yinz zyLxexxeuzwaryxdexyzn'

# Remove this line and add your code here


# ## String Slices
# 
# We are now able to select individual characters of a string and to iterate over all characters of a string, but sometimes we want just a part (segment) of a string.
# 
# A segment of a string is called a **slice**.
# 
# A slice is obtained by giving a range of indices.
# 
# In the next cell, we show how we can obtain the segments `Data` and `Science` from the giving string.

# In[ ]:


ds_str : str = 'Data Science'

ln : int = len(ds_str)
print(ln)
data : str = ds_str[0:4]
science : str = ds_str[5:ln]

print(data)
print(len(data))
print(science)
print(len(science))


# The operator [n:m] returns the part of the string from the “n-eth” character to the “m-eth”
# character, including the first but excluding the last. 
# 
# If you omit the first index (before the colon), the slice starts at the beginning of the string.
# If you omit the second index, the slice goes to the end of the string.
# 
# Beware, take care of the *start* and *end* indices of the string. This is a frequent source of errors.

# In[ ]:


ds_str : str = 'Data Science'

data : str = ds_str[:4]
science : str = ds_str[5:]

print(data)
print(science)


# If the first index is greater than or equal to the second the result is an empty string, represented
# by two quotation marks:

# In[ ]:


ds : str = 'Data Science'

data : str = ds[4:4]

data


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Assign the string 'skateboard' to the variable *word*. Now, print the first and second half in independent lines by just slicing the string and using the `len` function. 
# ```

# In[ ]:


# Remove this line and add your code here


# ## Strings are Immutable
# 
# What is meant by *immutable*?

# It is not possible to use the `[]` operator on the left hand side of an assignment.
# 
# It is not possible to change an existing string, strings are **immutable**.

# In[ ]:


greeting : str = 'Hello Data Scientist'
greeting[0] = 'h'


# If you want to change a string you *must* create a new string.
# 
# In the cell below, we create a new string `new_greeting` by concatenating the letter `h` with the slice consisting of all characters of the original string except the first character.
# 
# The original string is not *changed*.

# In[ ]:


print(greeting)
new_greeting : str = 'h' + greeting[1:]
print(new_greeting)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Assign the string 'break' to a varible. Replace the first letter by 'g' and the last one by 't'.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Searching
# 
# Finding a specific element in a long list can be boring, in principle you have to inspect all elements until you find the element you are looking for. 
# 
# The next cell shows a few lines of code that mimicks this searching for an element by means of looking for a specific letter in a word.

# In[ ]:


def find(word : str, letter : str) -> int:
    """looks at which position the letter appears first, 
    if the letter does not appear in the string -1 is returned"""
    index : int = 0
    
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
        
    return -1

find('data science', 'a')


# The function `find` is in fact the inverse of the `[]` operator. 
# 
# Instead of taking an index and extracting
# the corresponding character, it takes a character and finds the index where that character
# appears. 
# 
# If the character is not found, the function returns `-1`.
# 

# 
# ````{margin}
# ```{admonition} EXTRA
# This is the first example we have seen of a return statement inside a loop. 
# ```
# ````
# 

# 
# If `word[index] == letter`, the function breaks out of the loop and returns immediately.
# 
# If the character does not appear in the string, the program exits the loop normally and returns
# `-1`.
# 
# This pattern of computation —traversing a sequence and returning when we find what we
# are looking for— is called a **search**.
# 
# Is it possible to write this function using a `for` loop more compact?

# In[ ]:


def find(word : str, letter : str) -> int:
    """looks at which position the letter appears first, 
    if the letter does not appear in the string -1 is returned"""
    index : int = 0
    
    for char in word:
        if char == letter:
            break
        index += 1
        
    if index >= len(word):
        return -1
    else:
        return index

find('data science', 'z')


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# In the following cell there is information about the ticket of a concert. You want to extract the number of the ticket. Use the search pattern and previous string functions and operators to return the ticket reference.
# ```

# In[ ]:


info = 'Ticket reference: 9090873982'

# Remove this line and add your code here


# ## Looping and Counting
# 
# The following program counts the number of times the letter `e` appears in a string.

# In[ ]:


word : str = 'gazelle'
count : int = 0

for letter in word:
    if letter == 'e':
        count += 1
        
print(count)


# This program demonstrates another pattern of computation called a **counter**. 
# 
# The variable count is initialized to `0` and then incremented each time the letter is encountered. 
# 
# When the loop exits, count contains the result —the total number of `e`’s in the word `gazelle`.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Count the number of vowels in the word 'supercalifragilisticexpialidocious'.
# ```

# In[ ]:


# Remove this line and add your code here


# ## The `in` Operator
# 
# The word `in` is a boolean operator that takes two strings and returns `True` if the first appears
# as a substring in the second.

# In[ ]:


'zel' in 'gazelle'


# In[ ]:


'par' in 'gazelle'


# For example, the following function prints all the letters from `word1` that also appear in `word2`.

# In[ ]:


def in_both(word1 : str, word2 : str):
    """prints letters that appear in both words"""
    for letter in word1:
        if letter in word2:
            print(letter)

in_both('trek', 'gazelle')


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Count the number of vowels in the word 'supercalifragilisticexpialidocious' but this time use the <i>in</i> operator.
# ```

# In[ ]:


# Remove this line and add your code here


# ## String Comparison
# 
# An important operation on strings is checking whether strings are equal or not.
# If you have to search for a certain word in a text or dictionary you will need
# such an operation. 
# 
# Python offers a number of relational operators that work on strings, 
# for instance to check whether two strings are equal.

# In[ ]:


word : str = input('> ')
if word == 'apple':
    print('Hmmm, an apple!')


# Other relational operations are useful for putting words in alphabetical order.

# In[ ]:


word : str = input('> ')
if word < 'apple':
    print('Your word, ' + word + ', comes before apple!')
elif word > 'apple':
    print('Your word, ' + word + ', comes after apple!')
else:
    print('Hmmm, an apple!')


# Python does not treat uppercase and lowercase letters the same as people do. 
# 
# All the uppercase letters come before all the lowercase letters, so:
# 
# `Your word, Pineapple, comes before apple.`
# 
# A common way to address this problem is to convert strings to a standard format, such as
# all lowercase, before doing string comparison. 

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# In the following cell you will find three words. Can you print them in alphabetical order? Use the comparison operator for that purpose.
# ```

# In[ ]:


word1 : str = 'purple'
word2 : str = 'green'
word3 : str = 'red'

# Remove this line and add your code here


# ## String Methods
# 
# Strings are an example of a Python object.
# 
# For now, an object is equivalente to a value.
# 
# However, it has more information than a normal valuel. An object contains *data* and a set of *methods*.
# 
# Methods are functions that are built into the object. 
# 
# Contrary to normal function, methods have a slightly different syntax.
# 
# The Python function `dir` lists all the methods available for an object. Let's see the methods that an object of type string has.

# In[ ]:


text : str = 'Data Science'
dir(text)


# As you can see, Python provides a whole collection of useful methods on strings.
# 
# Calling a method is similar to calling a function, the only difference is that you will first place the name of the variable and then the name of the method separated by a dot. Something like `var.method()`.
# 
# For instance, instead of the function syntax `upper(word)`, we use the method syntax `word.upper()`.

# In[ ]:


word : str = 'gazelle'
new_word : str = word.upper()
new_word


# This form of dot notation specifies the name of the method, `upper`, and the name of the
# string to apply the method to, `word`. 
# 
# The empty parentheses indicate that this method takes no arguments.
# 
# A method call is called an **invocation**; in this case, we would say that we are invoking the method
# `upper` on `word`.
# 
# As it turns out, there is a string method named `find` that is remarkably similar to the
# function we wrote.

# In[ ]:


word : str = 'gazelle'
index : int = word.find('z')
index


# Actually, the find method is more general than our function; it can find substrings, not just
# characters.
# 
# Furthermore, the method can also be directly invoked on a string **object**.

# In[ ]:


index : int = 'sparta'.find('par')
index


# The `find` method can take 1 or 2 **optional arguments**.
# 
# The first optional argument is the index where the search in the string object should start.
# 
# The second optional argument is the index where the search in the string object should stop.

# In[ ]:


name : str = 'bob'
name.find('b', 1, 2)


# This search fails because `b` does not appear in the index range from `1` to `2`, not including `2`.
# 
# Searching up to, but not including, the second index makes `find` consistent with the slice operator.

# In[ ]:


name[1:2].find('b')


# ## Format Operator
# 
# With the format operator `%` we can build a string by replacing parts of it with data stored in variables.
# 
# Remember that when `%` is used with integers it is know as the modulus operator. When playing around with strings we call it the format operator.
# 
# The first operand should always be a string containing *format sequences*. The second argument is one or more variables. If you have more than one variable they should be stores in a tuple (we will talk about this data type later).
# 
# A format sequence are markers such as `'%d'` to format an integer, `'%g'` to format floats, and `'%s'` to format strings.

# In[ ]:


days : int = 365
'A year has %d' % days


# In[ ]:


who : str = 'Tom'
budget : float = 1.99
days : int = 365

'%s says that he is allowed to spend %g euros every single day of the %d days of the year.' % (who, budget, days)


# You can get an error if your don't write all needed elements to format the string.

# In[ ]:


day : str = 'Monday'
hour : int = 5
place : str = 'the park'

'Se you on %s at %d in %s' % (day, hour)


# Or when you use a wrong format sequence.

# In[ ]:


day : str = 'Monday'
hour : int = 5
place : str = 'the park'

'Se you on %d at %d in %s' % (day, hour, place)


# For more information on the format operator, 
# see https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting. 
# 
# A more powerful alternative is
# the string format method, which you can read about at 
# https://docs.python.org/3/library/stdtypes.html#str.format.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Create three variables: the first one will contain your name, the second one your age, and the third one your passion. Print a string that says 'My name is `name`. I am `age` years old. And my passion is `passion`.' Use the format operator to create this string.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Reading Word Lists
# 
# In one of the next lectures, file manipulation will be discussed, however we need to have a list of words.
# 
# This file is in plain text, so you can open it with a text editor, but you can also read it from Python. 
# 
# The built-in function `open` takes the name of the file as a parameter and returns a
# file **object** you can use to read the content of the file.

# In[ ]:


words = open('words.txt')


# The `file` object provides several methods for reading, including **readline**, which reads characters from the `file` until it gets to a newline and returns the result as a string.

# In[ ]:


words.readline()


# The character `\n` represents whitespace character `newline`, that separate this word from the next.
# 
# The `file` object keeps track of where it is in the file, so if you call `readline` again, you get the next word.

# In[ ]:


words.readline()


# The next word is “aah”.
# 
# The fact that every word that we read via `readline` is terminated by a whitespace is
# annoying and inconvenient. 
# 
# We can get rid of these whitespace characters with the string method `strip`.

# In[ ]:


line : str = words.readline()
word : str = line.strip()
word


# You can also use a file object as part of a `for` loop. 
# 
# The following program reads `words.txt` and prints each word, one per line.

# In[ ]:


words = open('words.txt')
for word in words:
    s_word : str = word.strip()
    print(s_word)


# ## Simple Examples
# 
# There are a number of exercises/examples in the book. 
# 
# The first is to print all words with a length greater than 20.
# 
# A straightforward solution is to use a `for` loop to iterate over the list of words, of course we first need to read the file with words.
# 
# In the body of the `for` loop there is a test on the length of the words, after stripping the whitespace.

# In[ ]:


words = open('words.txt')

for word in words:
    stripped_word : str = word.strip()
    if len(stripped_word) > 20:
        print(stripped_word)


# The second example is on counting the number of words without an `'e'` character.
# 
# Again we use a `for` loop, but now we need to keep a counter for counting the number of words without an `'e'` letter.

# In[ ]:


words = open('words.txt')

no_e_count : int = 0

for word in words:
    
    if not('e' in word):
        no_e_count += 1

print(no_e_count)


# The third example is variation on the second one, we do not only count the number of words without an `'e'` character, but also *all* words in the file.
# 
# For course, we could introduce a separate loop for counting the total number of words, but because we have to iterate anyway one `for` loop will be sufficient.
# 
# We need to keep a counter for counting the number of words with an `'e'` letter and a counter for counting all words.

# In[ ]:


words = open('words.txt')

count : int = 0
no_e_count : int = 0

for word in words:

    count += 1
    if not('e' in word):
        no_e_count += 1

print(count)
print(no_e_count)

print("Percentage is:", int((no_e_count/count)*100))


# The fourth example is how via a simple check on can determine whether forbidden letters are used in a word.

# In[ ]:


def avoids(word : str, forbidden : str) -> bool:
    """check whether the forbidden letters do not appear the word"""
    for letter in forbidden:
        if letter in word:
            return False
    return True

avoids("foo", "abcf")


# In[ ]:


forbidden_letters = input('> ')

words = open('words.txt')

count = 0
for word in words:
    if avoids(word, forbidden_letters):
        count += 1

print(count)


# In[ ]:


def uses_only(word : str, only : str) -> bool:
    """check whether the all letters in word appear in only"""
    for letter in word:
        if not letter in only:
            return False
    return True

uses_only("foo", "fol")


# ## Frequent string related errors
# 
# One of the most frequently occurring and most expensive errors are the **off-by-one** errors.
# 
# When traversing a sequence (string) it turns out to be very hard to get the indices right.
# 
# Consider the following function that tests whether one word is the reverse of the other.
# 
# So, `stop` and `pots` are possible candidates.
# 
# We are going to use a loop in combination with indices, note that a recursive solution is more *robust*.

# In[ ]:


def is_reverse(word1 : str, word2 :str) -> bool:
    """check whether the first argument is a reverse 
    of the second argument
    """
    if len(word1) != len(word2):
        return False
    
    i : int = 0
    j : int = len(word2)
    
    while (j > 0):
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1
        
    return True


# First we check both words have the same length, if not, then the words cannot be the reverse of each other.
# 
# Next we iterate over the both words, `word1` from the first character to  the end and `word2` starting for the end of the word to the beginning. 
# 
# We check per character whether they appear in both words.

# In[ ]:


is_reverse('pots', 'stop')


# Adding a print statement when we enter the loop to see the values of `i` and `j` gives insight in what we did wrong. 

# In[ ]:


def is_reverse(word1 : str, word2 :str) -> bool:
    """check whether the first argument is a reverse of the second argument
    """
    if len(word1) != len(word2):
        return False
    
    i = 0
    j = len(word2)
    
    while (j > 0):
        print(i, j)
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1
        
    return True

is_reverse('stop', 'pots')


# We did not initialized the variable `j` in a correct way. 

# In[ ]:


def is_reverse(word1 : str, word2 :str) -> bool:
    """check whether the first argument is a reverse of the second argument
    """
    if len(word1) != len(word2):
        return False
    
    i = 0
    j = len(word2) - 1
    
    while (j >= 0):
        print(i, j)
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1
        
    return True

is_reverse('stop', 'pots')


# In[ ]:


is_reverse('stop', 'lots')


# Is the `is_reverse` function now correct?
# 
# What is the result of the following call and why?
