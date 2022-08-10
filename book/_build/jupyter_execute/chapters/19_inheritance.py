#!/usr/bin/env python
# coding: utf-8

# # Inheritance [^intro]
# 
# [^intro]: This Jupyter Notebook is based on Chapter 18 of {cite}`thinkPython`.

# **Inheritance** is another important concept in the object oriented programming paradigm.
# 
# Inheritance refers to defining a new class with little or no modification to an existing class. 
# 
# Inheritance is the ability to define a new class that is a modified version of an existing
# class without copy-and-pasting.
# 
# This Jupyter Notebook contains **much more** material than Chapter 18 of the book *Think Python*.

# ## Dish Objects
# 
# Healthy food is a hype. People pay a lot of attention to what they eat. It should be low on calories but nevertheless tasty.
# 
# We are going to develop a number of classes to represent dishes and meals in order to see whether our calorie intake is just right (not too much, not too little).
# 
# The types of meals we distinguish are `breakfast`, `lunch`, `dinner`, and `all`.
# 
# The types of food we distinguish are `vegetarian` and `non-vegetarian`.
# 
# If we want to define a new object to represent a dish, it is obvious what the attributes should be: `meal_type` and `food_type`. 
# 
# A "better" way is to use integers to **encode** the `meal_type` and `food_type`. 
# 
# In this context, “encode” means that we are going to define a mapping between numbers and meal_types and food_types.
# 
# This kind of encoding is not meant to be a secret (that would be “encryption”).
# 
# For example, this table shows the meals and the corresponding integer codes:
# 
# * all $\rightarrow$ 0
# * breakfast $\rightarrow$ 1
# * lunch $\rightarrow$ 2
# * dinner $\rightarrow$ 3
# 
# The next table shows the type of food and the corresponding integer codes:
# 
# * vegetarian $\rightarrow$ 0
# * non-vegetarian $\rightarrow$ 1
# 
# Although the latter mapping is a kind of overkill, it allows the introduction of more specific food types, like meat, fish, etc.
# 
# The $\rightarrow$ symbol is used to make it clear that these mappings are not part of the Python program. 
# 
# They are part of the program design, but they do not appear explicitly in the code.

# In[1]:


class Dish:
    """Represents a dish."""

    food_type_names : list = ['vegetarian', 'non-vegetarian']
    meal_names : list = ['all', 'breakfast', 'lunch', 'dinner']
    
    def __init__(self, name : str, calories : int, food_type : int = 1, meal : int = 0) -> None:
        """ creates a new Meal object and initializes it
        """
        self.name : str = name
        self.calories : int = calories
        self.food_type : int = food_type
        self.meal : int = meal


# As usual, the `init` method takes an optional parameter for each attribute. 
# 
# The default meal is `0` (`all`) and the food type is `1` (`non-vegetarian`).
# 
# To create a `Dish`, you call `Dish` with the food type and meal type of the dish you want.

# In[2]:


fries : Dish = Dish('fries', 400, 0, 3)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Let's improve the <i>Dog</i> type we defined in previous chapters. This time we want to have the following attributes: `name`, `breed`, `age`, and `weight`. Define the `init` function and the `breeds` class attribute.
# ```

# In[3]:


# Remove this line and add your code here


# ## Class Attributes
# 
# In order to print `Dish` objects in a way that people can easily read, we need a mapping
# from the integer codes to the corresponding meal and food types. 
# 
# A natural way to do that is with lists of strings. We assign these lists to **class attribute**.

# In[4]:


class Dish:
    """Represents a dish."""
    
    food_type_names : list = ['vegetarian', 'non-vegetarian']
    meal_names : list = ['all', 'breakfast', 'lunch', 'dinner']

    def __init__(self, name: str, calories : int, food_type : int = 1, meal : int = 0) -> None:
        """ creates a new Meal object and initializes it
        """
        self.name : str = name
        self.calories : int = calories
        self.food_type : int = food_type
        self.meal : int = meal
        
    def __str__(self) -> str:
        """ returns the string represetation of a Dish object
        """
        return '{} dish {} has {:d} calories and is used {} meal'.format(Dish.food_type_names[self.food_type], self.name, self.calories, Dish.meal_names[self.meal])


# Variables like `food_type_names` and `meal_names`, which are defined inside a class but outside
# of any method, are called class attributes because they are associated with the class object `Dish`.
# 
# This term distinguishes them from variables like `food_type` and `meal`, which are called **instance attributes** because they are associated with a particular instance (object).
# 
# Both kinds of attribute are accessed using dot notation. For example, in `__str__`, `self`
# is a `Dish` object, and `self.meal` is its meal. 
# 
# `Dish` is a class object, and
# `Dish.meal_names` is a list of strings associated with the class.
# 
# Every dish has its own `food_type` and `meal`, but there is only one copy of `food_type_names` and
# `meal_names`.
# 
# Putting it all together, the expression `Dish.meal_names[self.meal]` 
# means “use the attribute `meal` from the object `self` as an index into the list `meal_names` 
# from the class `Dish`, and select the appropriate string."
# 
# With the methods we have so far, we can create and print dishes.

# In[5]:


dish : Dish = Dish('fries', 400, 0, 2)
print(dish)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Let's add a new class attribute <i>breeds</i> with the accepted dog breeds to the <i>Dog</i> type. It must be a list with the following options: "labrador", "chihuahua", "samoyed", "shar-pei". The <i>breed</i> instance attribute should now be an integer.
# ```

# In[6]:


# Remove this line and add your code here


# ## Comparing Dishes
# 
# For built-in types, there are relational operators (`<`, `>`, `==`, etc.) that compare 
# values and determine when one is greater than, less than, or equal to another. 
# 
# For programmer-defined types, we can override the behavior of the built-in operators by providing a method named `__lt__`, which stands for “less than”. 
# 
# This is similar to the `__str__` method that overrides the `print` method.
# 
# `__lt__` takes two parameters, `self` and `other`, and returns `True` if `self` is strictly less than other.
# 
# The correct ordering for dishes may be not obvious. 
# 
# What criteria do we use, is a vegetarian dish healthier than a non-vegetarian dish? Or
# do we only look at the amount of calories? Or do we take the meal into consideration as well?
# 
# For this moment we take the calories into consideration when comparing dishes.

# In[7]:


class Dish:
    """Represents a dish."""
    
    food_type_names : list = ['vegetarian', 'non-vegetarian']
    meal_names : list = ['all', 'breakfast', 'lunch', 'dinner']

    def __init__(self, name: str, calories : int, food_type : int = 1, meal : int = 0) -> None:
        """ creates a new Meal object and initializes it
        """
        self.name : str = name
        self.calories : int = calories
        self.food_type : int = food_type
        self.meal : int = meal
        
    def __str__(self) -> str:
        """ returns the string represetation of a Dish object
        """
        return '{} dish {} has {:d} calories and is used {} meal'.format(Dish.food_type_names[self.food_type], self.name, self.calories, Dish.meal_names[self.meal])
    
    def __lt__(self, other) -> bool:
        """ compares 2 dishes based on calories
        """
        # check the calories
        return self.calories < other.calories


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Override the <i>__str__</i> method of the <i>Dog</i> types o it says: "<i>name</i> is a <i>breed</i>". Use the <i>breeds</i> class attribute to get the name of the breed.
# ```

# In[8]:


# Remove this line and add your code here


# ## Meals
# 
# Now that we have dishes we can start composing meals.

# In[9]:


class Meal:
    """Represents a collection of dishes."""
    
    def __init__(self) -> None:
        """ creates a new Meal object and initializes it
        """
        self.dishes : list = []


# The following `__init__` method is more robust.

# In[10]:


class Meal:
    """Represents a collection of dishes."""
    
    def __init__(self, dishes=[]) -> None:
        """ creates a new Meal object and initializes it
        """
        self.dishes : list = dishes


# We need to be able to compose a meal given a list of dishes.

# In[11]:


class Meal:
    """Represents a collection of dishes."""
    
    def __init__(self, dishes=[]) -> None:
        """ creates a new Meal object and initializes it
        """
        self.dishes : list = dishes
        
    def compose(self, dishes : list) -> None:
        """ composes a meal
        """
        self.dishes : list = dishes


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Now, the <i>DogOwner</i> type can have more than one dog. Remember that a dog owner has a <i>name</i>, <i>last name</i>, and <i>age</i>. Create the <i>init</i> function so it reflects this new requirement. Afterwards, create the method <i>get_dog</i>, which adds one new dog to the list of dogs of the owner.
# ```

# In[12]:


# Remove this line and add your code here


# ## Printing a Meal
# 
# The next cell extends the class with a `__str__` method for printing a `Meal`.

# In[13]:


class Meal:
    """Represents a collection of dishes."""
    
    def __init__(self, dishes=[]) -> None:
        """ creates a new Meal object and initializes it
        """
        self.dishes : list = dishes
        
    def __str__(self):
        dlst : list = []
        for dish in self.dishes:
            dlst.append(dish.name)
        return '\n'.join(dlst)
        
    def compose(self, dishes : list) -> None:
        """ composes a meal
        """
        self.dishes : list = dishes


# Since we invoke `join` on a newline character, the dishes are separated by newlines. 
# 
# Even though the result appears on multiple lines, it is one long string that contains newlines.
# 
# Here is what the result looks like.

# In[14]:


cereals : Dish = Dish('cereals', 200, 0, 1)
eggs : Dish = Dish('eggs', 100, 0, 1)
meal : Meal = Meal()
meal.compose([cereals, eggs])
print(meal)


# The following code is better.

# In[15]:


cereals : Dish = Dish('cereals', 200, 0, 1)
eggs : Dish = Dish('eggs', 100, 0, 1)
meal : Meal = Meal([cereals, eggs])
print(meal)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Define the <i>__str__</i> method of the <i>DogOwner</i> type. You should print the message "<i>name</i> <i>last_name</i> is <i>age</i> years old and has the following dogs:". Then, use the <i>join</i> method to append the result of invoking the <i>str</i> method on each dog.
# ```

# In[16]:


# Remove this line and add your code here


# ## Add, Remove, Unique, and Surprise Me
# 
# Sometimes you want to remove a dish from a meal.
# 
# The list method `remove` provides a convenient way to do that, but you need to pass the name
# of the dish.

# In[17]:


class Meal:
    """Represents a collection of dishes."""
    
    def __init__(self, dishes=[]) -> None:
        """ creates a new Meal object and initializes it
        """
        self.dishes : list = dishes
        
    def __str__(self):
        dlst : list = []
        for dish in self.dishes:
            dlst.append(dish.name)
        return '\n'.join(slst)
        
    def compose(self, dishes : list) -> None:
        """ composes a meal
        """
        self.dishes : list = dishes
        
    def remove_dish(self, dish_name : str) -> None:
        """ removes a dish from a meal
        """
        for i in range(len(self.dishes)):
            if self.dishes[i].name == dish_name:
                del self.dishes[i]
                break


# Since `remove` removes a dish from the list, if you want to remove a specific dish, you need to pass its name as argument.
# 
# To add a dish, we can use the list method `append`.

# In[18]:


class Meal:
    """Represents a collection of dishes."""
    
    def __init__(self, dishes=[]) -> None:
        """ creates a new Meal object and initializes it
        """
        self.dishes : list = dishes
        
    def __str__(self):
        dlst = []
        for dish in self.dishes:
            dlst.append(dish.name)
        return '\n'.join(dlst)
        
    def compose(self, dishes : list) -> None:
        """ composes a meal
        """
        self.dishes : list = dishes
        
    def remove_dish(self, dish_name : str) -> None:
        """ removes a dish from a meal
        """
        for i in range(len(self.dishes)):
            if self.dishes[i].name == dish_name:
                del self.dishes[i]
                break
    
    def add_dish(self, dish : Dish) -> None:
        """ add a dish to a meal
        """
        self.dishes.append(dish)


# Maybe you do not want to have the same dish twice in your meal. 
# 
# For that, we introduce a method to check whether a dish is already in the meal.

# In[19]:


class Meal:
    """Represents a collection of dishes."""
    
    def __init__(self, dishes=[]) -> None:
        """ creates a new Meal object and initializes it
        """
        self.dishes : list = dishes
        
    def __str__(self):
        dlst = []
        for dish in self.dishes:
            dlst.append(dish.name)
        return '\n'.join(dlst)
        
    def compose(self, dishes : list) -> None:
        """ composes a meal
        """
        self.dishes : list = dishes
        
    def remove_dish(self, dish_name : str) -> None:
        """ removes a dish from a meal
        """
        for i in range(len(self.dishes)):
            if self.dishes[i].name == dish_name:
                del self.dishes[i]
                break
    
    def add_dish(self, dish : Dish) -> None:
        """ adds a dish to a meal
        """
        self.dishes.append(dish)
        
    def contains_dish(self, dish : Dish) -> bool:
        """ checks whether the dish is already in the meal
        """
        return dish in self.dishes


# In[20]:


cereals : Dish = Dish('cereals', 200, 0, 1)
eggs : Dish = Dish('eggs', 100, 0, 1)
bread : Dish = Dish('bread', 50, 0, 0)
meal : Meal = Meal([cereals, eggs])
print(meal)
meal.remove_dish('eggs')
meal.add_dish(bread)
print(meal.contains_dish(bread))
print(meal.contains_dish(eggs))

print(meal)


# There exists an extensive list of food data, see https://catalog.data.gov/dataset/mypyramid-food-raw-data-f9ed6.
# 
# This list has been the basis for creating a CSV file with about 85 different types of food, including information on
# calories, portion size, (non-)vegetarian and type of meal.
# 
# Suppose you want to select arbitrary of dishes from this list.
# 
# Before we start implementing the function to read the CSV file, we first write a function to convert an entry of the CSV file into a dish.
# 
# The information in the CSV file is:
# 
# `Display_Name; Portion_Amount; Portion_Display_Name; Meats;Calories; Vegetarian; Meal`. 
# 
# We use this information to develop the conversion function `convert_to_dish`.

# In[21]:


def convert_to_dish(entry) -> Dish:
    name : str = entry['Display_Name']
    calories : int = entry['Calories']
    if entry['Meal'] == 'B':
        meal_type = 1
    elif entry['Meal'] == 'L':
        meal_type = 2
    elif entry['Meal'] == 'D':
        meal_type = 3
    else: # entry['Meal'] == 'A'
        meal_type = 0
        
    if entry['Vegetarian'] == 'yes':
        dish : Dish = Dish(name, calories, 0, meal_type)
    else:
        dish : Dish = Dish(name, calories, 1, meal_type)
    return dish


# For that we introduce the method `surprise_me`, it takes the number of dishes to be added to
# the meal, and it uses a random function to "select" the dishes.

# Before we can implement this `surprise_me` method, we first have to define a function to
# process food data (given as a CSV file) via a function `process_food_data`.
# 
# See https://docs.python.org/3/library/csv.html for more information on CSV files.
# 
# We need to import the `csv` module.

# In[22]:


import csv

def process_food_data():    
    """ reads a CSV and converts it into a dictionary where the key is plain integer value
        and the value is a Dish
    """
    csv_file = open('datasets/FoodTable.csv')
    food_table : dict = dict()
    reader = csv.DictReader(csv_file, delimiter=';')
    
    i : int = 0
    for entry in reader:
        food_table[i] = convert_to_dish(entry)
        i += 1    
        
    csv_file.close()
    return food_table


# The next step is writing a function that converts an entry in the food data into a dish.
# 
# Note, that the function `randint` is used to generate an arbitrary ranking.

# The next step is to write the `surprise_me` method, that given an integer value as argument, selects that number
# of dishes (arbitrary from the list of dishes).

# In[23]:


import random

class Meal:
    """Represents a collection of dishes."""
    
    def __init__(self, dishes=[]) -> None:
        """ creates a new Meal object and initializes it
        """
        self.dishes : list = dishes
        
    def __str__(self) -> str:
        dlst = []
        for dish in self.dishes:
            dlst.append(dish.name)
        return '\n'.join(dlst)
        
    def compose(self, dishes : list) -> None:
        """ composes a meal
        """
        self.dishes  : list= dishes
        
    def remove_dish(self, dish_name : str) -> None:
        """ removes a dish from a meal
        """
        for i in range(len(self.dishes)):
            if self.dishes[i].name == dish_name:
                del self.dishes[i]
                break
    
    def add_dish(self, dish : Dish) -> None:
        """ adds a dish to a meal
        """
        self.dishes.append(dish)
        
    def contains_dish(self, dish : Dish) -> bool:
        """ checks whether the dish is already in the meal
        """
        return dish in self.dishes
            
    def surprise_me(self, nr : int) -> None:
        """ add arbitrary dishes upto 'nr_of_dishes'
        """
        for i in range(nr):
            dish : Dish = food_table[random.randint(0,len(food_table))]
            while self.contains_dish(dish):
                dish = food_table[random.randint(0,len(food_table))]
            self.add_dish(dish)
    
food_table = process_food_data()
meal = Meal()
meal.surprise_me(5)
print(meal)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Define the <i>remove_dog</i> and <i>has_dog</i> methods on the <i>DogOwner</i> class. The former removes a dog given its name from the list of dogs. The latter verifies if a dog is part of the list of dogs given its name.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Inheritance
# 
# Inheritance is the ability to define a new class that is a modified version of an existing class.
# 
# As an example, suppose we want to distinguish between the general concept of a meal and a specific meal, such as
# breakfast, lunch and dinner.
# 
# To define a new class that inherits from an existing class, you put the name of the existing
# class in parentheses.

# The new class is called **derived (or child) class** and the one from which it *inherits* is called the **base (or parent) class**.
# 
# A derived class inherits features from the base class where new features can be added to it. This results in re-usability of code.
# 
# The syntax for inheritance:
# 
# `class BaseClass:
#     Body of base class
# class DerivedClass(BaseClass):
#     Body of derived class`

# In[ ]:


class Breakfast(Meal):
    """ represents a breakfast as a meal 
    """


# This definition indicates that `Breakfast` inherits from `Meal`; that means we can use methods like
# `add_dish` and `remove_dish` for `Breakfast` as well as `Meal`.
# 
# When a new class inherits from an existing one, the existing one is called the **parent** and
# the new class is called the **child**.
# 
# In this example, `Breakfast` inherits `__init__` from `Meal`, but it does not really do what we want:
# instead we want to start healthy with a glass of orange juice, the `__init__` method for `Breakfast` should initialize dishes with an orange juice. Thus, we **override** it.

# In[19]:


class Breakfast(Meal):
    """ represents a breakfast as a meal
    """
    
    def __init__(self):
        orange_juice : Dish = Dish('Orange juice (100% juice)', 105, 0, 0)
        Meal.__init__(self,[orange_juice])


# When you create a `Breakfast`, Python invokes this `__init__` method, not the one in `Meal`.

# In[20]:


breakfast : Breakfast = Breakfast()
print(breakfast)


# The other methods are inherited from `Meal`, so we can use `add_dish` and `remove_dish`.

# In[21]:


breakfast : Breakfast = Breakfast()
yoghurt : Dish = Dish('Fruit yogurt, whole milk', 202, 0, 0)
breakfast.add_dish(yoghurt)
print(breakfast)


# The method `surprise_me` of the class `Meal` selects all possible types of food from the food data.
# When composing a breakfast you only want to have breakfast dishes.

# In[25]:


class Breakfast(Meal):
    """ represents a breakfast as a meal
    """
    
    def __init__(self):
        orange_juice = Dish('Orange juice (100% juice)', 105, 0, 0)
        Meal.__init__(self,[orange_juice])
        
    def surprise_me(self, nr : int) -> None:
        """ add arbitrary dishes upto 'nr_of_dishes'
        """
        for i in range(nr):
            dish : Dish = food_table[random.randint(0,len(food_table))]
            while dish.meal == 2 or dish.meal == 3 or self.contains_dish(dish):
                dish = food_table[random.randint(0,len(food_table))]
            self.add_dish(dish)


# In[30]:


breakfast : Breakfast = Breakfast()

breakfast.surprise_me(1)
print(breakfast)


# Inheritance is a useful feature.
# 
# Some programs that would be repetitive without inheritance can be written more elegantly with it.
# 
# Inheritance can facilitate code reuse, since you can customize the behavior of parent classes without having to modify them.
# 
# In some cases, the inheritance structure reflects the natural structure of the problem, which makes the design easier to understand.
# 
# On the other hand, inheritance can make programs difficult to read.
# 
# When a method is invoked, it is sometimes not clear where to find its definition.
# 
# The relevant code may be spread across several modules.
# 
# Also, many of the things that can be done using inheritance can be done as well or better without it.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# A dog owner can now have other types of pets. Define the <i>Pet</i> class and create the <i>Dog</i> and <i>Cat</i> classes, which inherits from them. A Pet instance has the following attributes: <i>name</i>, <i>breed</i>, <i>age</i>, and <i>weight</i>. Now, we will define new <i>breeds</i> lists on the Dog and Cat classes. Possible cat breeds are "siamese", "sphynx", "persian", and "angora".
# ```

# In[ ]:


# Remove this line and add your code here


# ## A Second Example of Inheritance
# 
# A polygon is a closed figure with 3 or more sides. A class called `Polygon` can be defined as follows.

# In[31]:


class Polygon:
    def __init__(self, no_of_sides : int):
        self.n : int = no_of_sides
        sides : list = []
        for i in range(no_of_sides):
            sides.append(0)
        self.sides : list = sides

    def input_sides(self) -> None:
        self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n)]

    def display_sides(self) -> None:
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])


# This class has data attributes to store the number of sides `n` and magnitude of each side as a list called `sides`.
# 
# The `input_sides()` method takes in the magnitude of each side and `display_sides()` displays these side lengths.
# 
# A triangle is a polygon with 3 sides. So, we can create a class called `Triangle` which inherits from `Polygon`. This makes all the attributes of `Polygon` class available to the `Triangle` class.
# 
# We do not need to define them again (code reusability). 
# 
# `Triangle` can be defined as follows.

# In[32]:


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def calculate_area(self) -> None:
        a, b, c = self.sides
        # calculate the semi-perimeter
        s : int = (a + b + c) / 2
        area : float = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)


# `class Triangle` has a new method `find_area()` to find and print the area of the triangle.

# In[34]:


t = Triangle()

t.input_sides()

t.calculate_area()


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Copy the <i>Pet</i> class and define the method <i>compute_human_age()</i>, which only returns the age of the pet. Now, copy the <i>Dog</i> and <i>Cat</i> classes, and redefine the new method. In the case of a dog, the human age is equal to the age of the dog times 7; and the human age of a cat is equal to its age times 5. Create one <i>Cat</i> and one <i>Dog</i> object, then test your methods.
# ```

# In[ ]:


# Remove this line and add your code here


# ## A Third Example of Inheritance
# 
# Below is another simple example of inheritance in Python.

# In[36]:


class Person(): 
    """ Representing a person 
    """
    
    # Constructor 
    def __init__(self, name : str): 
        self.name : str = name 
   
    # To get name 
    def get_name(self) -> str: 
        return self.name 
   
    # To check if this person is an employee 
    def is_employee(self) -> bool: 
        return False
   
   
# Inherited or Subclass/Child class
class Employee(Person): 
   
    # Here we return true 
    def is_employee(self) -> bool: 
        return True


emp : Person = Person("Mark")  # An Object of Person 
print(emp.get_name(), emp.is_employee()) 
   
emp : Employee = Employee("Lina") # An Object of Employee 
print(emp.get_name(), emp.is_employee()) 


# Let us work a bit more on this example.

# In[37]:


class Person():     
    """ Representing a person 
    """
    
    # Constructor
    def __init__(self, name : str, idnumber : int):    
        self.name : str = name 
        self.idnumber : int = idnumber 
        
    # getters have to be added!
    
    # To get name     
    def display(self) -> None: 
        print(self.name) 
        print(self.idnumber) 

# Child class
class Employee(Person): 
    """ Representing an employee
    """
    
    def __init__(self, name : str, idnumber : int, salary : int, function : str): 
        self.salary : int = salary 
        self.function : str = function 
  
        # invoking the __init__ of the parent class  
        Person.__init__(self, name, idnumber)  
  
                  
# creation of an object variable or an instance 
a : Employee = Employee('Mark', 886012, 100000, "Professor")     
    
# calling a function of the class Person using its instance 
a.display()


# The variables defined within `__init__()` are called as the **instance variables** or **attributes**. Hence, `name` and `idnumber` are the attributes of the class `Person`. 
# 
# Similarly, `salary` and `function` are the attributes of the class `Employee`. Since the class `Employee` inherits from class `Person`, `name` and `idnumber` are also the attributes of class `Employee`.
# 
# If you forget to invoke the `__init__()` of the parent class then its instance variables would not be available to the child class.

# In[ ]:


class Person():     
    """ Representing a person 
    """
    
    # Constructor
    def __init__(self, name : str, idnumber : int):    
        self.name : str = name 
        self.idnumber : int = idnumber 
        
    # To get name     
    def display(self) -> None: 
        print(self.name) 
        print(self.idnumber) 

# Child class
class Employee(Person): 
    """ Representing an employee
    """
    
    def __init__(self, name : str, idnumber : int, salary : int, function : str): 
        self.salary : int = salary 
        self.function : str = function 
  
        # invoking the __init__ of the parent class  
        super().__init__(name, idnumber)  
  
                  
# creation of an object variable or an instance 
a : Employee = Employee('Mark', 886012, 100000, "Professor")     
    
# calling a function of the class Person using its instance 
a.display()


# When calling a method or the parent class you can use `super()`, which returns a temprary object of the parent class.
# With this object you can invoke all methods defined within the super class.
# Notice that we do not pass the argument `self` anymore.

# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Copy the <i>Pet</i> and <i>Dog</i> classes. Now, you will add the attribute <i>bark_volume</i> to the dog, which is an integer between 1 and 10 being 1 the lowest possible value and 10 the highest. Modify the <i>Dog</i> constructor to add this new instance variable.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Different Forms of Inheritance
# 
# * **Single inheritance**: When a child class inherits from only one parent class, it is called single inheritance. We saw an example above.
#     
# * **Multiple inheritance**: When a child class inherits from multiple parent classes, it is called multiple inheritance. Unlike Java and like C++, Python supports multiple inheritance. We specify all parent classes as a comma-separated list in the bracket. 

# In[38]:


class Person():     
    """ Representing a person 
    """
    
    # Constructor
    def __init__(self, name : str, idnumber : int):    
        self.pname : str = name 
        self.idnumber : int = idnumber 
        
    # To get name     
    def display(self): 
        print(self.pname) 
        print(self.idnumber) 
        
class Organisation():
    """ Representing an organisation
    """
    # Constructor
    def __init__(self, name : str, tp_of_organ : str):
        self.orgname : str = name
        self.orgtype : str = tp_of_organ

# Child class
class Employee(Person, Organisation): 
    """ Representing an employee
    """
    # Constructor
    def __init__(self, idname : str, idnumber : int, salary : int, function : str, orgname : str, orgtype : str): 
        self.salary : int = salary 
        self.function : str = function 
  
        # invoking the __init__ of the parent class  
        Person.__init__(self, idname, idnumber) 
        Organisation.__init__(self, orgname, orgtype)
  
                  
# creation of an object variable or an instance 
a = Employee('Mark', 886012, 100000, 'Professor', 'TU/e', 'university')     
  
# calling a function of the class Person using its instance 
a.display()


# * **Multilevel inheritance**: When we have a child and grandchild relationship.

# In[39]:


class Person():     
    """ Representing a person 
    """
    
    # Constructor
    def __init__(self, name : str, idnumber : int):    
        self.pname : str = name 
        self.idnumber : int = idnumber 
        
    # To get name     
    def display(self): 
        print(self.pname) 
        print(self.idnumber) 
        
class Organisation():
    """ Representing an organisation
    """
    # Constructor
    def __init__(self, name : str, tp_of_organ : str):
        self.orgname : str = name
        self.orgtype : str = tp_of_organ

# Child class
class Employee(Person, Organisation): 
    """ Representing an employee
    """
    # Constructor
    def __init__(self, idname : str, idnumber :int, salary : int, orgname : str, orgtype : str): 
        self.salary : int = salary 
  
        # invoking the __init__ of the parent class  
        Person.__init__(self, idname, idnumber) 
        Organisation.__init__(self, orgname, orgtype)
        
class Scientific(Employee):
    """ Representing a specific function
    """
    
    #Constructor
    def __init__(self, idname : str, idnumber : int, salary : int, level : str, orgname : str, orgtype : str):
        self.level = level
        
        # invoking the __init__ of the parent class
        Employee.__init__(self, idname, idnumber, salary, orgname, orgtype)
        
# creation of an object variable or an instance 
a = Scientific('Mark', 886012, 100000, 'professor', 'TU/e', 'university')     
  
# calling a function of the class Person using its instance 
a.display()


# * **Hierarchical inheritance**: When more than one derived classes are created from a single base this type of inheritance is called hierarchical inheritance. In this program, we have a parent (base) class and two child (derived) classes.

# In[40]:


class Person():     
    """ Representing a person 
    """
    
    # Constructor
    def __init__(self, name : str, idnumber : int):    
        self.pname : str = name 
        self.idnumber : int = idnumber 
        
    # To get name     
    def display(self): 
        print(self.pname) 
        print(self.idnumber) 
        
class Organisation():
    """ Representing an organisation
    """
    # Constructor
    def __init__(self, name : str, tp_of_organ : str):
        self.orgname : str = name
        self.orgtype : str = tp_of_organ

# Child class
class Employee(Person, Organisation): 
    """ Representing an employee
    """
    # Constructor
    def __init__(self, idname : str, idnumber : int, salary : int, orgname : str, orgtype : str): 
        self.salary : int = salary 
  
        # invoking the __init__ of the parent class  
        Person.__init__(self, idname, idnumber) 
        Organisation.__init__(self, orgname, orgtype)
        
class Scientific(Employee):
    """ Representing a specific scientific function
    """
    
    #Constructor
    def __init__(self, idname : str, idnumber : int , salary : int, level : str, orgname : str, orgtype : str):
        self.level  : str= level
        
        # invoking the __init__ of the parent class
        Employee.__init__(self, idname, idnumber, salary, orgname, orgtype)
        
class Support(Employee):
    """ Representing a specific support function
    """
    
    #Constructor
    def __init__(self, idname : str, idnumber : int, salary : int, suptype : str, orgname : str, orgtype : str):
        self.suptype = suptype
        
        # invoking the __init__ of the parent class
        Employee.__init__(self, idname, idnumber, salary, orgname, orgtype)
        
# creation of an object variable or an instance 
a = Scientific('Mark', 886012, 100000, 'full', 'TU/e', 'university')
b = Support('Erik', 685010, 50000, 'programmer', 'TU/e', 'university')     
  
# calling a function of the class Person using its instance 
a.display()
b.display()


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# What type of inheritance do we have in the <i>Pet</i>-<i>Dog</i>-<i>Cat</i> scenario? Why?
# ```

# ## Method Overriding
# 
# In the above example, notice that `__init__()` method was defined in both classes `Breakfast` as well `Meal`. 
# 
# When this happens, the method in the derived class *overrides* the one in the base class. This is to say, `__init__()` in `Breakfast` gets preference over the `__init__()` in `Meal`.
# 
# Generally, when overriding a base method, we tend to extend the definition rather than replace it. 
# 
# The same is being done by calling the method in base class from the one in derived class (calling `Meal.__init__()` from `__init__()` in `Breakfast`).

# ## Checking Inheritance
# 
# Two built-in functions `isinstance()` and `issubclass()` are used to check inheritances.
# 
# The function `isinstance()` returns `True` if the object is an instance of the class or other classes derived from it. 
# 
# Each and every class in Python inherits from the base class `object`.

# In[41]:


isinstance(breakfast,Breakfast)


# In[42]:


isinstance(breakfast,Meal)


# In[43]:


isinstance(breakfast,int)


# In[44]:


isinstance(breakfast,object)


# In the same way, `issubclass()` is used to check for class inheritance.

# In[45]:


issubclass(Meal,Breakfast)


# In[46]:


issubclass(Breakfast,Meal)


# In[47]:


issubclass(bool,int)


# ```{admonition} Do It Yourself!
# :class: seealso, dropdown
# Create one <i>Dog</i> and one <i>Cat</i> object. Use the <i>isinstance()</i> and <i>issubclass()</i> functions to verify the relationship between your <i>Pet</i> objects and the <i>Pet</i>, <i>Dog</i>, and <i>Cat</i> classes.
# ```

# In[ ]:


# Remove this line and add your code here


# ## Class Diagrams
# 
# A **class diagram** is an abstract representation of the structure of a program. 
# 
# It shows the classes and their relations.
# 
# Class diagrams are extremely popular and used, among others, in UML (Unified Modeling Language).
# 
# There are several kinds of relationship between classes:
# 
# * Objects in one class might contain references to objects in another class. For example,
#   each Rectangle contains a reference to a Point, and each Deck contains references to
#   many Cards. This kind of relationship is called **HAS-A**, as in, “a Rectangle has a
#   Point.”
# * One class might inherit from another. This relationship is called **IS-A**, as in, “Breakfast
#   is a kind of Meal.”
# * One class might depend on another in the sense that objects in one class take objects
#   in the second class as parameters, or use objects in the second class as part of a
#   computation. This kind of relationship is called a **dependency**.
#   
# A **class diagram** is a graphical representation of these relationships.

# In[ ]:


print(' +--------+        *   +--------+')
print(' |  Meal  |   ------>  |  Dish  |')
print(' +--------+            +--------+')
print('     /_\                         ')
print('      |                          ')
print('      |                          ')
print('      |                          ')
print('+-----------+                    ')
print('| Breakfast |                    ')
print('+-----------+                    ')


# The arrow with a hollow triangle head represents an IS-A relationship; in this case it indicates that Hand inherits from Deck.
# 
# The standard arrow head represents a HAS-A relationship; in this case a Meal object has references
# to Dish objects.
# 
# The star (\*) near the arrow head is a **multiplicity**; it indicates how many Dishes a Meal has.
# 
# A multiplicity can be a simple number, like 3, a range, like 5..7 or a star, which indicates that a Meal can have any number of Dishes.
# 
# There are no dependencies in this diagram. 
# 
# They would normally be shown with a dashed arrow. 
# 
# Or if there are a lot of dependencies, they are sometimes omitted.
# 
# A more detailed diagram might show that a Meal actually contains a list of Dishes, but
# built-in types like list and dict are usually not included in class diagrams.
# 
# See https://en.wikipedia.org/wiki/Class_diagram for more information on UML class diagrams.

# ## Data Encapsulation
# 
# The previous chapters demonstrate a development plan we might call “object-oriented
# design”. 
# We identified objects we needed -- like `Point`, `Rectangle` and `Time` -- and defined
# classes to represent them. 
# 
# In each case there is an obvious correspondence between the
# object and some entity in the real world (or at least a mathematical world).But sometimes it is less obvious what objects you need and how they should interact. 
# 
# In
# that case you need a different development plan. 
# 
# In the same way that we discovered
# function interfaces by encapsulation and generalization, we can discover class interfaces
# by **data encapsulation**.

# Introducing classes, attributes and methods, starting from *regular* Python code, is another example of refactoring.
# 
# This example suggests a development plan for designing objects and methods:
# 
# 1. Start by writing functions that read and write global variables (when necessary).
# 2. Once you get the program working, look for associations between global variables and the functions that use them.
# 3. Encapsulate related variables as attributes of an object.
# 4. Transform the associated functions into methods of the new class.
