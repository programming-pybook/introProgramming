#!/usr/bin/env python
# coding: utf-8

# # Sorting [^intro]
# 
# This Jupyter Notebook is based on external content related to algorithms (e.g. searching and sorting).

# _(c) 2021, Mark van den Brand, Eindhoven University of Technology_

# ## Table of Contents
# <div class="toc" style="margin-top: 1em;">
#     <ul class="toc-item">
#         <li>
#             <span><a href="#4.-Sorting" data-toc-modified-id="4.-Sorting">4. Sorting</a></span>
#         </li>
#     </ul>
# </div>

# ## 4. Sorting
# 
# Sorting is an operation that you need to perform frequently. There are multiple sorting algorithms, such as bubble sort, insertion sort, merge sort, quick sort, etc. Each algorithm has a different time complexity, this means the amount of time need to sort an array. 
# 
# Of course, Python offers built-in functions for sorting, e.g. `list.sort()`.
# 
# But it is good to understand the basic principles of various sorting algorithms.

# ### Bubble Sort
# 
# The first algorithm that will be discussed is *bubble sort*.
# 
# The basic idea of *bubble sort* is to move the largest element to the end of a list, array, etc. 
# 
# We will use a list of elements for which the comparison operator `>` is defined.
# 
# Suppose we have to sort the list `[4, 3, 5, 2, 1]`.
# 
# In the first step the element `5` bubbles to the end of the list, giving `[4, 3, 2, 1, 5]`.
# 
# In the second step the element `4` bubbles to the end of the list, but will not pass the element `5`, giving `[3, 2, 1, 4, 5]`.
# 
# In the third step the element `3` bubbles to the end of the list, but will not pass the element `4`, giving `[2, 1, 3, 4, 5]`.
# 
# In the fourth step the element `2` bubbles to the end of the list, but will not pass the element `3`, giving `[1, 2, 3, 4, 5]`.
# 
# The first version of *bubble sort* is a recursive version.

# In[1]:


from typing import List

def bubble_to_end(lst : List[any]) -> List[any]:
    """ moves the largest element to the end of the list"""
    
    if len(lst) <= 1:   # Stop condition for moving
        return lst
    else:
        if lst[0] > lst[1]:
            # Swap the first and second elements in the row
            lst[0], lst[1] = lst[1], lst[0] 
        first : any = lst[0]
        return [first] + bubble_to_end(lst[1:])
    
def bubble_sort_r(unsorted : List[any]) -> List[any]:
    """ sorts a list in a recursive way
    >>> bubble_sort([3, 4, 7, -1, 2, 5])
    [-1, 2, 3, 4, 5, 7]
    >>> bubble_sort([])
    []
    >>> bubble_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    """
    
    if len(unsorted) <= 1:  # Stop condition for sorting
        return unsorted
    else:
        unsorted = bubble_to_end(unsorted)    #move (bubble) largest element to the end
        print(unsorted)
        last : any = unsorted.pop()               #remove last element and remember it
        sortedList = bubble_sort_r(unsorted)
        print(sortedList)
        return sortedList + [last]  #sort the rest and concatenate last element
    
print(bubble_sort_r([4,3,5,2,1]))


# In[2]:


import doctest

doctest.testmod(verbose=True)  # with details


# The time complexity of the *bubble sort* algorithm is $n^2$ worst case.
# 
# The next cell shows the iterative version of *bubble sort*, it has the same time complexity.

# In[3]:


from typing import List

def bubble_sort(unsorted : List[any]) -> List[any]:
    """sorts a list in a non-recursive way
    >>> bubble_sort([3, 4, 7, -1, 2, 9, 5])
    [-1, 2, 3, 4, 5, 7, 9]
    >>> bubble_sort([])
    []
    >>> bubble_sort([6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6]
    """
    
    offset : int = 1
    swapped : bool = True
    while swapped:  #Non-terminating loop
        swapped = False
        #move the biggest element to the end of the list
        for i in range(len(unsorted)-offset): 
            if unsorted[i] > unsorted[i+1]:
                unsorted[i], unsorted[i+1] = unsorted[i+1], unsorted[i] #swap
                swapped = True
                
        # you can ignore the last element(s) because they are sorted       
        offset += 1
        #print(unsorted)
        #print(offset)
        
    return unsorted
        
print(bubble_sort([4,3,5,2,1]))


# In[4]:


doctest.testmod(verbose=True)  # with details


# In[5]:


import random
from typing import List

i : int = 0
rdlst : List[int] = []
    
while i < 10000:
    rdnr : int = random.randint(0,1000000)
    if rdnr not in rdlst:
        rdlst = rdlst + [rdnr]
    i += 1
    
#print(rdlst)


# Again some timing measurements.

# In[6]:


import time

org_lst = rdlst.copy()

t1 = time.perf_counter()
lst2 : List[int] = bubble_sort(rdlst)
t2 = time.perf_counter()
print("The binary search code took {:.2f}ms".format((t2 - t1) * 1000))


# ### Insertion Sort
# 
# The second algorithm that will be discussed is *insertion sort*.
# 
# The basic idea of *insertion sort* is to move the smaller elements in front of bigger elements.  
# 
# We will use a list of elements for which the comparison operator `>` is defined.
# 
# Suppose we have to sort the list `[4, 3, 5, 2, 1]`.
# 
# In the first step the element `3` will be inserted before the `4` in the list, giving `[3, 4, 5, 2, 1]`. This is done by storing the value `3` and copying the `4` to the place of the `3`, the intermediate result is: `[4, 4, 5, 2, 1]`. Now the original `4` is replaced by `3`, giving `[3, 4, 5, 2, 1]`.
# 
# In the second step the first 3 elements `3, 4, 5` are sorted and next element `2` must be inserted before the `3`. This is done by storing the value `2` and copying the first 3 elements one position to the right, the intermediate result is: `[3, 3, 4, 5, 1]`.Now the original `3` is replaced by `3`, giving `[2, 3, 4, 5, 1]`.
# 
# In the third and final step the first 4 elements `2, 3, 4, 5` are sorted and next element `1` must be inserted before the `2`. This is done by storing the value `1` and copying the first 4 elements one position to the right, the intermediate result is: `[2, 2, 3, 4, 5]`.Now the original `2` is replaced by `1`, giving `[1, 2, 3, 4, 5]`.
# 
# 
# The next cell shows a version of *insertion sort*.

# In[7]:


from typing import List

def insertion_sort(unsorted: List[any]) -> List[any]:
    """sorts the list by inserting the at the right position in the list
    
    >>> insertion_sort([3, 4, 7, -1, 2, 9, 5])
    [-1, 2, 3, 4, 5, 7, 9]
    >>> insertion_sort([])
    []
    >>> insertion_sort([6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6]
    """
   
    for index in range(1, len(unsorted)):
        currentvalue : any = unsorted[index]
        position : int = index

        # print(unsorted)
        # shift elements that are greater than the "current value" to the right and
        # create an "open" slot in the list to insert the "current value".
        while position > 0 and unsorted[position-1] > currentvalue:
            unsorted[position] = unsorted[position-1]
            position -= 1
        #print(unsorted)
        unsorted[position] = currentvalue
    
    return unsorted

alist = [54,26,93,17,77,31,44,55,20]
sortedList = insertion_sort(alist)
print(sortedList)


# In[8]:


import doctest

doctest.testmod(verbose=True)  # with details


# In[9]:


import time

rdlst = org_lst.copy()

t1 = time.perf_counter()
lst1 : List[int] = bubble_sort(rdlst)
t2 = time.perf_counter()
print("The binary search code took {:.2f}ms".format((t2 - t1) * 1000))

rdlst = org_lst.copy()

t1 = time.perf_counter()
lst2 : List[int] = insertion_sort(rdlst)
t2 = time.perf_counter()
print("The insertion search code took {:.2f}ms".format((t2 - t1) * 1000))

if lst1 == lst2:
    print("lst1 == lst2")


# ### Merge Sort
# 
# The third algorithm that will be discussed is *merge sort*. This algorithm and the next are based on the same idea as the *binary_search* algorithm. Splitting the list recursively in 2 parts and sort each part and then merge.
# 
# The basic idea of *merge sort* is to split the list in two halves and sort each halves
# and merge the both into one list again.
# 
# We will use again a list of elements for which the comparison operator `>` is defined.
# 
# Suppose we have to sort the list `[4, 3, 5, 2, 1]`.
# 
# In the first step the list is splitted into `[4, 3]` and `[5, 2, 1]`
# 
# In the second step the list `[4, 3]` is splitted into `[4]` and `[3]`, and
# the resulting two 'sorted lists' are merged into `[3, 4]`.
# 
# In the third step the list `[5, 2, 1]` is splitted into `[5]` and `[2, 1]`.
# 
# In the fourth step the list `[2, 1]` is splitted into `[2]` and `[1]`, and
# the resulting two 'sorted lists' are merged into `[1, 2]`. 
# 
# The list `[1, 2]` can now be merged with the sorted list `[5]`, resulting in `[1, 2, 5]`.
# 
# The list `[1, 2, 5]` can now be merged with the sorted list `[3, 4]`, resulting in the sorted list `[1, 2, 3, 4, 5]`.
# 
# The  version of *merge sort* is a recursive version.

# In[10]:


from typing import List

def merging(leftSorted : List[any], rightSorted : List[any]) -> List[any]:
    """both lists into a merged list
    """
    
    sortedList : List[any] = []
    i : int = 0
    j : int = 0
    while i < len(leftSorted) and j < len(rightSorted):
        if leftSorted[i] < rightSorted[j]:
            sortedList.append(leftSorted[i])
            i += 1
        else:
            sortedList.append(rightSorted[j])
            j += 1

    if i < len(leftSorted):
        sortedList += leftSorted[i:]

    if j < len(rightSorted):
        sortedList += rightSorted[j:]

#    print("Merging ", sortedList)
    return sortedList

def merge_sort(unsorted : List[any]) -> List[any]:
    """sorts a list by means of divide and conquer
    
    >>> merge_sort([3, 4, 7, -1, 2, 9, 5])
    [-1, 2, 3, 4, 5, 7, 9]
    >>> merge_sort([])
    []
    >>> merge_sort([6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6]
    """
    
    if len(unsorted) > 1:
        middle = len(unsorted) // 2
        leftUnsorted = unsorted[:middle]
        rightUnsorted = unsorted[middle:]

        leftSorted = merge_sort(leftUnsorted)
        rightSorted = merge_sort(rightUnsorted)

        return merging(leftSorted, rightSorted)
    else:
        return unsorted
    

alist = [54,26,93,17,77,31,44,55,20]
#alist = [4, 3, 5, 2, 1]
print(alist)
sList = merge_sort(alist)
print(sList)


# In[11]:


import doctest

doctest.testmod(verbose=True)  # with details


# *merge sort* is more efficient than *bubble sort* because of the *divide-and-conquer* strategy, however the creation of intermediate lists may be problematic.
# 
# 

# In[12]:


import time

rdlst = org_lst.copy()

t1 = time.perf_counter()
lst1 : List[int] = bubble_sort(rdlst)
t2 = time.perf_counter()
print("The bubble sort took {:.2f}ms".format((t2 - t1) * 1000))

rdlst = org_lst.copy()

t1 = time.perf_counter()
lst2 : List[int] = insertion_sort(rdlst)
t2 = time.perf_counter()
print("The insertion sort took {:.2f}ms".format((t2 - t1) * 1000))

rdlst = org_lst.copy()

t1 = time.perf_counter()
lst3 : List[int] = merge_sort(rdlst)
t2 = time.perf_counter()
print("The merge sort took {:.2f}ms".format((t2 - t1) * 1000))

if lst1 == lst2:
    print("lst1 == lst2")

if lst1 == lst3:
    print("lst1 == lst3")


# ### Quicksort
# 
# Quicksort is an algorithm presented by Tony Hoare in 1962.
# It is like merge sort a recursive algorithm, where the list 
# to be sorted is recursively "split" into 2 parts, sorted and 
# combined again. In contrast to merge sort,
# where the split is done based on the length of the list, 
# each half is sorted and the results are merged. In case of quicksort
# the splitting results two parts that can be concatenated.
# This is possible because a *pivot* is chosen and the elements 
# of the list are reshuffled in relation to the pivot. Elements
# smaller than the pivot are moved to left of the pivot, elements greater
# than the pivot are moved to the right of the pivot.
# 
# The challenge is to find the right pivot. The better the pivot the faster the algorithm, because the sublist (left and right of the pivot) will be more or less of the same length.

# In[13]:


def partition(arr : List[any], low : int, high : int) -> int: 
    """ Reshuffles the elements of the list according to a pivot.
    The arbitrary chosen pivot is the last element of the list.
    The pivot is moved to the "middle" of the list.
    
    >>> L = [1]
    >>> partition(L, 0, 0)
    0
    >>> L = [5, 4, 2, 1, 3]
    >>> partition(L, 0, 4)
    2
    >>> L = [5, 4, 3, 2, 1]
    >>> partition(L, 0, 4)
    0
    """
    
    i : int  = low-1             # index of smaller element 
    pivot : any = arr[high]     # choose a pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or equal to pivot 
        if arr[j] <= pivot: 
            # increment index of smaller element and swap elements
            i += 1 
            arr[i],arr[j] = arr[j],arr[i] 
            
    # move the pivot to the right position
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    
    return i+1 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quick_sort(arr : List[any], low : int, high : int) -> None: 
    """ the list is sorted by partition the list in two parts,
    a part with elements smaller than a pivot and elements greater
    than the pivot.
    The partitioned parts are recursively sorted.
    
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> quick_sort(L, 0, 5)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi : int = partition(arr, low, high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quick_sort(arr, low, pi-1) 
        quick_sort(arr, pi+1, high) 
        
alist = [54,26,93,17,77,31,44,55,20]
#alist = [4, 3, 5, 2, 1]
print(alist)
quick_sort(alist, 0, len(alist)-1)
print(alist)


# In[14]:


import doctest

doctest.testmod(verbose=True)  # with details


# In[15]:


import time

rdlst = org_lst.copy()

t1 = time.perf_counter()
lst1 : List[int] = bubble_sort(rdlst)
t2 = time.perf_counter()
print("The bubble sort took {:.2f}ms".format((t2 - t1) * 1000))

rdlst = org_lst.copy()

t1 = time.perf_counter()
lst2 : List[int] = insertion_sort(rdlst)
t2 = time.perf_counter()
print("The insertion sort took {:.2f}ms".format((t2 - t1) * 1000))

rdlst = org_lst.copy()

t1 = time.perf_counter()
lst3 : List[int] = merge_sort(rdlst)
t2 = time.perf_counter()
print("The merge sort took {:.2f}ms".format((t2 - t1) * 1000))

rdlst1 = org_lst.copy()

t1 = time.perf_counter()
quick_sort(rdlst1, 0, len(rdlst1)-1)
t2 = time.perf_counter()
print("The quick sort took {:.2f}ms".format((t2 - t1) * 1000))

rdlst2 = org_lst.copy()

t1 = time.perf_counter()
rdlst2.sort()
t2 = time.perf_counter()
print("The python sort took {:.2f}ms".format((t2 - t1) * 1000))

if lst1 == lst2:
    print("lst1 == lst2")

if lst1 == lst3:
    print("lst1 == lst3")

if lst1 == rdlst1:
    print("lst1 == rdlst1")

if lst1 == rdlst2:
    print("lst1 == rdlst2")


# <div class="alert alert-success">
#     <b>Do It Yourself!</b><br>
#     Use the four functions to sort an array of integers and profile each one of them. Create a copy of the list otherwise you will end up sorting the same list. What is the difference among each algorithm?
# </div>

# In[16]:


lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Remove this line and add your code here


# **Advice:** when writing code always make sure that the code is correct (via testing for instance) before starting optimizing.
