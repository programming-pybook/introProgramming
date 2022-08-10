#!/usr/bin/env python
# coding: utf-8

# # Regular Expressions [^intro]
# 
# [^intro]: This Jupyter Notebook is based on Chapter 11 of {cite}`Severance2016`.

# To extract information from strings, we have been using string methods such as `split()` and `find()`, and lists and string slicing.
# However, the task of extracting data is so common that Python provides a library dedicated to handle these tasks in a more elegant manner.
# The library is called `re` (regular expressions) and it should be imported before you can start using it.
# 
# **Regular expressions** are like a little programming language created for searching and parsing strings.
# 
# There are general libraries, not Python specific, that offer this functionality as well (e.g. `grep`).
# 
# One of the simplest uses of the `re` library is the `search()` function, which verifies if a string is part of another string. 
# Let us see an example.

# In[1]:


file = open('datasets/mbox-short.txt')

for line in file:
    line: str = line.rstrip()
    print(line)


# In[2]:


import re

file = open('datasets/mbox-short.txt')

for line in file:
    line: str = line.rstrip()
    if re.search('Author:', line):
        print(line)


# The previous program prints all the lines that have the word `'Author'`.
# 
# As you might have noticed, we could implement this same program with the use of the `find()` method.
# 
# The power of the regular expressions comes when we add special characters to
# the search string, which allows us to more precisely control which lines match the
# string.

# In[ ]:


file = open('datasets/mbox-short.txt')

for line in file:
    line: str = line.rstrip()
    
    if re.search('^Author:', line):
        print(line)


# We modified our previous program, so it only prints the lines that start with the `'Author'` string. 
# This is done thanks to the use of the caret character (`^`), which is used in regular expressions to match the beginning of a line.
# 
# Still, this example can also work with the use of the `startswith()` method, but along this chapter we will try to convince you that in some cases using regular expressions eases our lives.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Add all lines that start by 'Details:' to a list. Use the <i>search</i> function.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Character Matching
# 
# There are other characters that help us build powerful regular expressions.
# For instance, the **period** or **full stop** character matches any character within a string.
# 
# The regular expression `s..r` can match any 4-letter word that starts with `s` and ends with `r`, like `scar`, `sear`, `slur`, and `soar`.
# 
# Let us now print all lines that start by `X-` followed by four characters and ending with `M`.

# In[ ]:


file = open('datasets/mbox-short.txt')

for line in file:
    line: str = line.rstrip()
    
    if re.search('^X-....M', line):
        print(line)


# This can be simplified by indicating that a character can be repeated multiple times.
# To do so, we use the `*` and the `+` **wildcard characters**.
# 
# The **asterisk** means that we need to match zero-or-more characters; while the **plus** sign states that we need to match one-or-more characters. The `*` or `+` applies to the single character placed immediately to their left.
# 
# The use of `*` and `+` results into a **greedy** match.
# A greedy match indicates that we match the longest possible string.
# 
# Let's now print all lines that start with `X-`, that are followed by one-or-more characters and that then have the `Result` word.

# In[ ]:


file = open('datasets/mbox-short.txt')

for line in file:
    line: str = line.rstrip()
    
    if re.search('^X-.+Result', line):
        print(line)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Print all lines that start by 'Received:', followed by zero-or-more charcaters, and that have the word 'nakamura'.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Extracting Data
# 
# We can also extract data from a string if we use the `findall()` method.
# This method will extract all substrings that match a given regular expression.
# 
# For instance, the `findall()` method is quite handy if we want to get all email addresses on the file, regardless of the format of the line where they are found.
# In this way, we do not need to write code for each type of line.
# 
# Let us see a small example before we create the whole program.

# In[ ]:


line: str = 'Einstein einstein@uni.edu sent an email to Ada ada@otheruni.edu about life @10'
emails: list = re.findall('\S+@\S+', line)
print(emails)


# The `findall()` method returns a list of strings with all the words that match the regular expression `\S+@\S+`.
# `\S` matches a non-whitespace character.
# 
# Thus, the `\S+@\S+` expression can be read as: one-or-more non-whitespace characters, followed by an `@` character (at), followed by one-or-more non-whitespace characters.
# 
# Now, we are ready to create a program to gather all emails within the `mbox-short.txt` file.

# In[ ]:


file = open('datasets/mbox-short.txt')
emails: list = list()

for line in file:
    line: str = line.rstrip()
    line_emails = re.findall('\S+@\S+', line)
    emails.extend(line_emails)
    
emails


# As you have noticed, some of the emails have additional characters that we would like to exclude (e.g. `<`, `>`, `;`).
# We only want to extract the email. 
# 
# To do so, we need to be more explicit when defining our regular expression. 
# Thus, we will use **square brackets** to define the set of characters that we want to match at the beginning and end of the email.
# 
# The new regular expression looks like this: `[a-zA-Z0-9]\S*@\S*[a-zA-Z]`
# 
# - The `[a-zA-Z0-9]` indicates that we are expecting one alphanumeric value (a letter between a-z or A-Z or a number between 0-9). We do not care if it is a capital or lower-case letter, that is why we add both `a-z` (for lower-case letters) and `A-Z` (for capital letters).
# - The `[a-zA-Z]` indicates that we will only match a lower-case or capital letter at the end of the string.
# - We switch to `\S*` because we already consider the need to match at least one character with the inclusion of both `[a-zA-Z0-9]` and `[a-zA-Z]`.

# In[8]:


file = open('datasets/mbox-short.txt')
emails: list = list()

for line in file:
    line: str = line.rstrip()
    line_emails: list = re.findall('[a-zA-Z0-9]\S*@[a-zA-Z.]+', line)
    emails.extend(line_emails)
    
emails


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Use regular expressions to count all the times that the email 'cwen@iupui.edu' appears on the file regardles of the line where it is placed.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Combining Searching and Extracting
# 
# Let us imagine that now we want to extract all the numbers that follow an `X-Something:` header, such as:
# 
# ```
# X-DSPAM-Confidence: 0.8475
# X-DSPAM-Probability: 0.0000
# ```
# 
# To do so, we can define the following regular expression:
# 
# `^X-.*: [0-9.]+`
# 
# `^X-` indicates that the line should start with 'X-'. Then, it must be followed by zero-or-more characters (`.*`), followed then by a colon and a space (`: `). Finally, the string should be followed by a one-or-more numbers `0-9` that can have points `.` (`[0-9.]+`). Notice that when we use the `.` inside square brackets, it does not match any character but instead it matches **literally** the point character.
# 
# Before extracting the numbers, let us just print the lines that match our regular expression.

# In[ ]:


file = open('datasets/mbox-short.txt')

for line in file:
    line: str = line.rstrip()
    
    if re.search('^X-.*: [0-9.]+', line):
        print(line)
    
emails


# We should use `split()` to actually get the decimal number out of our target lines.
# However, we will use regular expressions to achieve the same goal.
# 
# We introduce now the use of parentheses `()`.
# When you use parentheses in regular expressions, they are just completely ignored. 
# You usually use them to group terms in your expression.
# 
# Nevertheless, if you use `()` in a regular expression inside the `findall()` method, they serve a different purpose: 
# they indicate that you are interested in extracting only a portion of the string that matches the expression.
# 
# So, we modify our expression as follows:
# 
# `^X-.*: ([0-9.]+)`

# In[ ]:


file = open('datasets/mbox-short.txt')

for line in file:
    line: str = line.rstrip()
    match: list = re.findall('^X-.*: ([0-9.]+)', line)
    
    if len(match) > 0:
        print(match)


# Let us explore another example.
# The `mbox-short.txt` file also has the following type of lines:
# 
# `Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39771`
# 
# We would like to extract the revision number placed at the end of the string after `rev=`.
# In this example the revision number is `39771`.
# 
# We will now extract these numbers all along the file.

# In[ ]:


file = open('datasets/mbox-short.txt')

for line in file:
    line: str = line.rstrip()
    revision: list = re.findall('^Details:.*rev=([0-9.]+)', line)
    
    if len(revision) > 0:
        print(revision)


# We used the regular expression `^Details:.*rev=([0-9.]+)`.
# 
# `^Details:` indicates that the line should start by the word `Details:`; it will be then followed by zero-or-more characters (`.*`); and then it will find the `rev=` string.
# After the latter, we want to only extract the number that follows, which is composed by one-or-more numbers and points `([0-9.]+)`.
# 
# Remember that the `[0-9]+` is *greedy* and it tries to make as large a string of
# digits as possible before extracting those digits. Because of this behaviour, we
# get all five digits for each number.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
#     Use regular expressions to extract the IP numbers of lines with the following format (the IP number is the number that you find between the square brackets at the end of the string, e.g. 141.211.14.46):
#     
#     Received: from murder (mail.umich.edu [141.211.14.46])
# ```

# In[ ]:


# Remove this line and add your code here


# ## Escape Character
# 
# We need a way to use special characters within regular expressions in a normal or **literal** way.
# For instance, there might be cases where we want to match the caret `^` character, and not just use it to denote the start of a line.
# To do so, we use the escape character `\` before we type the character we want to match (e.g. `\^`).

# In[ ]:


msg: str = 'This is how you write 2 to the power of 2 in Java: 2^2'
matches: list = re.findall('[0-9]+\^[0-9]+', msg)
matches


# Remember that if you write special characters inside square brackets, characters are taken as literals.
# If we write `[0-9.^]` it literally means that we want to match digits (`0-9`) or the dot (`.`) or the caret character (`^`).

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Match all prices with the <i>receipt</i> string and return the sum of them all.
# ```

# In[ ]:


receipt: str = "Chocolate $2.0, Soap $10.0, Bread $1.4, Milk $2.4"

# Remove this line and add your code here


# ## Regular Expressions Cheat Sheet
# 
# In this section, we introduce some of the characters you can use when creating your regular expressions.

# ### Special Characters
# 
# | Character | Description |
# |:---------:|:------------|
# | `^` | Matches the start of a string |
# | `$` | Matches the end of a string |
# | `.` | Matches any character except new line characters (e.g. `\n`)|
# | `\` | Escapes special characters |
# | `A\|B` | Matches expression A or B |
# | `+` | Greedy match of one-or-more characters |
# | `*` | Greedy match of zero-or-more characters |
# | `?` | Greedy match of zero-or-one character. If added after a qualifier (i.e. `+`, `*`, `?`) performs non-greedy (or lazy) matches |
# | `{n}` | Matches an expression `n` times |
# | `{n, m}` | Matches an expression from `n` to `m` times |

# ### Character Classes
# 
# | Character | Description |
# |:---------:|:------------|
# | `\w` | Matches alphanumeric characters (i.e. a-z, A-Z, 0-9 and \_) |
# | `\d` | Matches digits (i.e. 0-9) |
# | `\D` | Matches non-digits | 
# | `\s` | Matches whitespace characters (e.g. \t, \n, \r) |
# | `\S` | Matches non-whitespace characters |
# | `\b` | Matches the empty string, but only at the start or end of a word |
# | `\B` | Matches the empty string, but not at the start or end of a word |
# 

# ### Sets
# 
# | Character | Description |
# |:---------:|:------------|
# | `[ ]` | Contains characters to match |
# | `[ab]` | Matches character `a` or `b`, not `ab` |
# | `[a-z]` | Matches a lower-case letter from `a` to `z` |
# | `[A-Z]` | Matches a capital letter from `A` to `Z` |
# | `[0-9]` | Matches a digit from `0` to `9` |
# | `[a-zA-Z0-9]` | Matches alphanumeric characters |
# | `[+*().]` | Matches special characters as literals |
# | `[^ab]` | Matches any character except `a` and `b` |

# ### Common `re` Methods
# 
# 
# | Method | Description |
# |:-------|:------------|
# |`re.findall(exp, string)` | Matches substrings in `string` that match expression `exp`, and returns them on a list. |
# | `re.search(exp, string)` | Matches the first substring in `string` that matches expression `exp`, and returns it as a match object. |
# | `re.split(exp, string)` | Splits `string` into a list by means of using expression `exp` as delimiter. |
# | `re.sub(exp1, exp2, string)` | Replaces all matches of expression `exp1` with `exp2` in the `string`. |

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Write a program to look for lines of the form: 'New Revision: 39772'. Then, extract all numers and add them up.
# ```

# In[ ]:


# Remove this line and add your code here

