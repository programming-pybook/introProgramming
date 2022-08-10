#!/usr/bin/env python
# coding: utf-8

# # Files [^intro]
# 
# [^intro]: This Jupyter Notebook is based on Chapter 7 of {cite}`Beecher` and Chapter 14 of {cite}`Erwig`.

# This chapter introduces how we can store data in a *persistent* way, this can be done via files and databases.
# We have already seen how we can open a file and read the content of a file, but storing data to process it later is indispensible. This functionality enables us to store data at some point in time and retrieve it at a later point in time.

# ## Persistence
# 
# The programs we have seen and that you have written, process data (input values) and print the results.
# The produced data evaporates, however, in real life this is not what we want. 
# Banks, webshops, etc. do not want to lose their data about customers, their shopping history, etc. Actually from a data science point of view this data is extremely important, because via this data trends, etc. can be predicted.
# 
# Programs that store their data are **persistent**. 

# Some programs are launched and they start with reading in (stored) data and continue with this data. Before terminating the new data is stored again.
# Other programs run "forever" and store their data in a persistent way (on disk) in order to ensure that no data is lost.

# One of the simplest ways for programs to maintain their data is by reading and writing (text) **files**. 
# Another way is to store data in a **database**, we will see a simple database and a module `pickle` to store data in an easy way.

# ## Opening Files
# 
# When we aim at opening a file, what we are really doing is asking the operating system (OS) to find a file by name and verify that it exists.
# We use the built-in function `open()` in Python to achieve this task.

# In[1]:


file_out = open('datasets/output.txt')


# If the function `open` is successful, the operating system returns a **file handle**.
# The file handle is not the real data, but instead, it is an intermediary that we can use to read from or write to the file.

# ## Text Files and Lines
# 
# A text file can be seen as a **sequence of lines**.
# 
# Python considers a special character to break the text into lines. This special character is known as the **newline** character, which represents the end of the line.
# 
# The newline character is represented as `\n`. If you include this character in a string, the content after the newline character will be displayed in a new line.

# In[ ]:


print('Data\nScience')


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
#     Can you print the text:
#     "I am
#     a Data Science student"
#     while using the newline character?
# ```

# In[ ]:


# Remove this line and add your code here


# ## Reading Files
# 
# To read a file we rely on the `open()` function.
# This function does not read the **entire content** of the file once it is called. This happens mainly because the file might be **too large** to keep it in main memory.
# Thus, the `open()` function takes the same amount of time to execute regardless of the size of the file.

# Once we call the `open()` function, we get a file handle that can be used within a `for` loop to read each line of the file.
# In this case, Python is in charge of splitting the content of the file into **separate lines**.
# With the `for` loop we can efficiently read a file of any size, because each line is read, counted, and then discarded.
# 
# The following code creates a **file handle** (`file_logs`) and counts the number of lines in the file.

# In[ ]:


file_logs = open('datasets/logs.txt')
count : int = 0

for line in file_logs:
    count += 1
    
print(count)


# If you know that the size of the file is **small** with reference to the size of your main memory, you can use the `read()` method on the file handle.
# This method reads the whole content of the file as a **big string** including all line and newline characters.
# 
# It is a good idea to store the output of the `read()` method in a variable, given that it **exhausts resources** (once resources are read, no more content can be obtained in a future invocation).

# In[ ]:


file_logs = open('datasets/logs.txt')
first_call : str = file_logs.read()
second_call : str = file_logs.read()

print('First call:\n' + first_call)
print('Second call:\n' + second_call)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
#  Read the *logs.txt* file and print its lines one by one.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Searching in a File
# 
# It is quite common to search for specific or interesting lines in a file, and skip the ones that do not meet a given condition. 
# For instance, we can use the `startswith()` string method to print the lines that start by "INFO".

# In[ ]:


file_logs = open('datasets/logs.txt')

for line in file_logs:
    if line.startswith('INFO'):
        print(line)


# We have filtered the information. 
# But, why are we seeing the extra blank line between lines?

# This is related to the invisible newline character present in all lines. Thus, the `print()` function prints all lines with this newline character and it also adds an **additional newline character**, resulting in double spacing.
# 
# To improve the asthetics of our output we can use the `rstrip()` method, which strips whitespaces from the end of a string.

# In[ ]:


file_logs = open('datasets/logs.txt')

for line in file_logs:
    if line.startswith('INFO'):
        print(line.rstrip())


# As your programs get more complex, you would like to use the `continue` statement to filter out uninteresting lines.
# 
# Please reflect on the difference between the `continue` and `break` statement.

# In[ ]:


file_logs = open('datasets/logs.txt')

for line in file_logs:
    if not line.startswith('INFO'): 
        continue
    print(line.rstrip())


# In the previous code, we use the contracted version of the `if` statement. That is why we place the `continue` statement in the same line.

# We can also use the `find()` string method to look for a string in a given line of the file. 
# This method returns the **position** of the string or `-1` if the string is not found.
# 
# Let us print now all lines that contain the text 'from:bob@mail.nl'.

# In[ ]:


file_logs = open('datasets/logs.txt')

for line in file_logs:
    if line.find('from:bob@mail.nl') == -1: 
        continue
    print(line.rstrip())


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Read the *logs.txt* file and count the ERROR lines.
# ```

# In[ ]:


# Remove this line and add your code here


# ## File Names and Paths
# 
# Files are organized into **directories** (also called “folders”). 
# Every running program has a **current directory**, which is the default directory for most operations. 
# For example, when you open a file for reading, Python looks for it in the current directory.
# 
# The `os` module provides functions for working with files and directories (“os” stands for
# “operating system”). 
# 
# `os.getcwd` returns the name of the current directory

# In[ ]:


import os

cwd : str = os.getcwd()
print(cwd)


# A string like '/Users/mvdbrand/Documents/GitLab/course-material-jbi010/202122/Lectures/week3' that identifies a file or directory is called a **path**. 
# 
# **[EXTRA]** Every operating system may have a different way of representing paths.

# A simple filename, like `words.txt` is also considered a path, 
# but it is a **relative path** because it relates to the current directory. 
# 
# For instance, if the current directory is `/Users/mvdbrand/Documents/GitLab/course-material-jbi010/202122/lectures/week3`, the filename
# `output.txt` would refer to `/Users/mvdbrand/Documents/GitLab/course-material-jbi010/202122/lectures/week3/output.txt`.
# 
# A path that begins with `/` does not depend on the current directory; it is called an **absolute
# path**. To find the absolute path to a file, you can use `os.path.abspath`.

# In[ ]:


os.path.abspath('datasets/output.txt')


# `os.path` provides other functions for working with filenames and paths. 
# 
# `os.path.exists` checks whether a file or directory **exists**.

# In[ ]:


os.path.exists('datasets/output.txt')


# If it exists, you can use `os.path.isdir` to check whether it **is a directory**.
# 
# **[NOTE]** I use an absolute path in the next cells, please change accordingly if you want to run the cells.

# In[ ]:


os.path.isdir('datasets/output.txt')


# In[ ]:


os.path.isdir('/Users/mvdbrand/Documents/GitLab/course-material-jbi010/202122/lectures/week3')


# `os.listdir` returns a **list of the files** (and other directories) in the given directory.

# In[ ]:


os.listdir(cwd)


# The application of these `os` functions are demonstrated in the following function, which iterates over a directory and prints all files and (sub)directories.
# 
# `os.path.join` takes a directory and a file name and joins them into a **complete path**.

# In[ ]:


def content(dir_name : str) -> None:
    """prints all files in subdirectories starting from dir_name"""
    current_directories : str = os.listdir(dir_name)
    
    for name in current_directories:
        path : str = os.path.join(dir_name, name)
        
        if os.path.isfile(path):
            print("File is:", path)
        else:
            print("Path is:", path)
            
content('/Users/mvdbrand/Documents/GitLab/course-material-jbi010/202021/lectures')


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Call the `content()` function in one of the folders of your file system.
# ```

# In[ ]:


# Remove this line and add your code here


# The `os` module provides a function called `walk` that walks over all subdirectories.
# 

# In[ ]:


for path in os.walk('/Users/mvdbrand/Documents/GitLab/course-material-jbi010/202122/lectures'):
    print(path)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Use the `walk()` method to check the content of a folder in your file system.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Let the User Choose the File
# 
# Sometimes we would like to let the user **choose the file** he or she wants to open. In this way, we do not need to modify our code every time we require a different file.
# 
# To do so, we can use the `input` function as follows.

# In[ ]:


file = input('Enter the file name:')
file_handle : str = open(file)

print(file)


# But what can go wrong with this code?

# ## Catching Exceptions
# 
# It might happen that our users or ourselves input a wrong path to our file, which will result in an **exception**.
# 
# In general, the reading and writing of files is error-prone. 
# The file may not exist, it may be read or write protected, etc.
# If you try to open a file that does not exist, you get a `FileNotFoundError`.

# In[ ]:


fbad = open('bad.txt')


# If you are not allowed to open a file, you get an error message as well.

# In[ ]:


file_out = open('/etc/passwd', 'w')


# If you try to open a directory, you get another error message.

# In[ ]:


file_in = open('/users')


# You could use functions like `os.path.exists` and `os.path.isfile` to prevent these type of errors.
# 
# However, a lot of (subtle) errors may happen when doing file-io and thus a lot of code
# may be involved to make it full proof.
# 
# If “`Errno 21`” is any indication, there are at least 21 things that can go wrong.
# It is better to go ahead and try—and deal with problems if they happen—which is exactly
# what the `try` statement does. 

# In[ ]:


try:
    fbad : str = open('bad_file')
except:
    print('Something went wrong.')


# Python starts by executing the `try` clause. 
# If all goes well, it skips the `except` clause and proceeds. 
# If an exception occurs, it jumps out of the `try` clause and executes the `except` clause.
# 
# Remember that tangling an exception with a try statement is called **catching an exception**. 
# In this example, the except clause prints an error message that is not very helpful. 
# In general, catching an exception gives you a chance to fix the problem, or try again, or at least end the program gracefully.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Handle the exception in the following code.
# ```

# In[ ]:


# Modify the following code
file = input('Enter the file name:')
file_handle = open(file)

print(file)


# ## Writing Files
# 
# To write a file you should open it with mode `w` (from *write*) as second parameter.

# In[ ]:


file_out = open('datasets/output.txt', 'w')


# If the file already exists, opening it in write mode removes the current content from the file, *so be careful!* 
# If the file does not exist, a new one is created.
# 
# `open` returns a file object that provides methods (`write` and `close`) for working with the file. 
# The `write` method puts data into the file.

# In[ ]:


line1 : str = "There are bright Data Scientists\n"
file_out.write(line1)


# The output number indicates how many characters are written to the file.
# 
# You need to explicitly add newline characters when using the `write()` method. Contrary to the `print()` function, the `write()` method does not automatically add newlines at the end of strings.
# 
# The file object keeps track of the position the next data is to be written.
# If you write more data to the file, it will be **appended**.

# In[ ]:


line2 : str = "But there are also bright Computer Scientists\n"
file_out.write(line2)


# When you are done writing, you must `close` the file. 
# As long as you do not close the file, no information is actually written to/stored in the file.
# If you do not close the file, it is closed for you when your program is terminated.
# However, similar to type hints and comments, make it common practice to **close files explicitly**, because different Python environments may have different behaviour in this respect.

# In[ ]:


file_out.close()


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Copy the content of *logs.txt* in the *output.txt* file.
# ```

# In[ ]:


# Remove this line and add your code here

