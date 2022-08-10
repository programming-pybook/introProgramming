#!/usr/bin/env python
# coding: utf-8

# # Data Preparation [^intro]
# 
# [^intro]: This Jupyter Notebook is based on Chapter 3 of {cite}`Pyle1999`. <br> **Relevant references:** <br> Kwak, S. K., & Kim, J. H. (2017). *Statistical Data Preparation: Management of Missing Values and Outliers*. Korean journal of anesthesiology, 70(4), 407–411. DOI: 10.4097/kjae.2017.70.4.407. Find it [here](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5548942/pdf/kjae-70-407.pdf). <br> Saluja, C. (2018). *Data Preparation — A Crucial Step in Data Mining*. Medium. Find it [here](https://medium.com/@chhavi.saluja1401/data-preparation-a-crucial-step-in-data-mining-dba35772f281).<br> Tachepun, C. and Thammaboosadee, S. (2020). *A Data Masking Guideline for Optimizing Insights and Privacy Under GDPR Compliance*. In the 11th International Conference on Advances in Information Technology. ACM, New York, Article 22, 1–9. DOI: 10.1145/3406601.3406627. Find it [here](https://dl.acm.org/doi/abs/10.1145/3406601.3406627).

# _(c) 2021, Lina Ochoa Venegas, Eindhoven University of Technology_

# In the Exploratory Data Analysis (EDA) chapter, we mentioned the two main stages considered in a data science project. In this notebook, we will extend this workflow by adding a new stage, namely the *data preparation* stage. **Data preparation** is a critical stage within the data analysis process given that data should be structure in such a way that it eases the extraction of information and does not alter the expected results. It is required because there might be missing values, missing variables<sup>1</sup> that must be computed based on existing features, discrepancies in the levels of categorical variables, wrong data formats, erroneous observations, to name but a few. Thus, when analyzing data, we consider the following stages:
# 
# 1. **Data preparation:** raw data is manipulated and transformed so further analysis can be performed atop of it to solve a domain problem.
# 2. **Exploratory data analysis:** assumptions are verified, methods are chosen, and quality hypotheses are formulated.
# 3. **Confirmatory data analysis:** (statistical hypothesis testing) previously defined hypotheses are tested and conclusions are drawn from the analysis.
# 
# Although we placed *data preparation* as the first stage of the data analysis process, it is common that after performing the EDA, data scientists go back to the underlying data and prepare it even further. This is natural after identifying irrelevant or erroneous observations, as well as errors in the formatting of the values.
# 
# <sup>1</sup> Remember that in the context of data science a *variable* models a feature of a case or observation. They are represented as columns in a rectangular dataset.

# <div class="alert alert-info">
#     <b>Data preparation</b><br>
#     <p>Data preparation is a stage in the data analysis process where raw data is manipulated and transformed to support further analysis targeting a domain problem.<p>
# </div>

# Data preparation comprises the following subprocess:
# 
# * **Data access:** accessing and discovering the dataset.
# * **Data cleanse:** cleaning the data by treating faulty and inconsistent data.
# * **Data integration:** merging or joining multiple data sources together.
# * **Data transformation:** normalizing, enriching, generalizing, or reducing the data.
# 
# The application of each subprocess in a dataset will depend on the nature of the data and the domain problem to solve.

# ## Data Access <a class="anchor" id="access"></a>
# 
# The data preparation stage begins with accessing and discovering the data. Evaluating if the data is correct and enough is part of the duties of a good data scientist. It must be clear:
# 
# * what was the *methodology* used to extract the data;
# * which *data structure* should be used to represent the data;
# * which *format* is used to store the data, and;
# * which *variables* are available. 
# 
# This information will be useful to assess and understand if the data at hand is enough to solve the domain problem, and if not, what additional data is needed. The result of this process will be finding a new dataset to replace or complement the existing one (c.f. [Data Integration](#integration)) or adding new variables to the existing dataset (c.f. [Data Transformation](#trannsformation)). 
# 
# For this course, we will only consider *rectangular data*, but there are many other data structures used in the wild. In particular, we will focus on the different file formats we can find and how to use Python to access these data sources.

# <div class="alert alert-info">
#     <b>Data access</b><br>
#     <p>Subprocess within the data analysis stage that focuses on accessing and discovering the data.<p>
# </div>

# ### File Formats
# 
# There are a plethora of formats used to store both structured and unstructured data. Some of the most popular formats are *plain text (txt)*, *Comma-Separated Values (CSV)*, *JavaScript Object Notation (JSON)*, and *Extensible Markup Language (XML)*. 
# 
# #### Plain Text
# In the Files chapter, you had the opportunity to interact with **plain text** files–with the `.txt` extension–, representing characters written using a specific encoding such as ASCII or Unicode. An **encoding** is a system that represents each character as a number for digital representation. (Have a look at the `logs.txt` file.)
# 
# You can use the `open()` function and `with` statement in Python to interact with these types of files. The `with` statement simplifies and encapsulates the use of try-except-finally patterns–that -s, you do not need to write them explicitly, the `with` statement does that for you! For more examples, check the Files chapter.

# In[1]:


# Read the first line of the log.txt file

with open('datasets/logs.txt') as file:
    print(file.readline()) 


# #### Comma-Separated Values (CSV)
# 
# The **Comma-Separated Values (CSV)** format–with the `.csv` extension–uses a comma, semicolon, or another character to separate values in a file. Each line in the file reports a case or record, and each value within the record is an observation for a given variable. Each record should have the same number of observations. CSV files usually store rectangular data in plain text and they look as follows. (Also have a look at the `logs.csv` file.)
# 
# ```
# variable_1, variable_2, ..., variable_n
# row_1_value_1, row_1_value_2, ..., row_1_value_n
# row_2_value_1, row_2_value_2, ..., row_2_value_n
# row_3_value_1, row_3_value_2, ..., row_3_value_n
# ```
# 
# In Pyhon, we can use the `csv` library to interact with CSV files. We can use the `reader()` function to create a reader object that will iterate over the rows in the CSV file. We can access each value using an index–based on the position of the variable in the file. Notice that the header of the rectangular data will also be printed if you do not exclude it explicitly.

# In[ ]:


import csv

with open('datasets/logs.csv') as file:
    reader = csv.reader(file, delimiter=',') # Default value of delimiter is ','
    
    for row in reader:
        typ = row[0]        # We write typ because type is a reserved word
        timestamp = row[1]
        from_email = row[2]
        to_email = row[3]
        message = row[4]
        
        print(f'{typ} {message} [{timestamp}] from:{from_email} to:{to_email}')


# However, indexing is error-prone. We can instead use the `DictReader()` function that will create a dictionary for each record in the file. You can access specific values with the name of the variable–declared in the first row of the file. In this case, you do not need to manage the header row, the `csv` library will do it for you.

# In[ ]:


import csv

with open('datasets/logs.csv') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        typ = row['type']            # We write typ because type is a reserved word
        timestamp = row['timestamp']
        from_email = row['from']
        to_email = row['to']
        message = row['message']
        
        print(f'{typ} {message} [{timestamp}] from:{from_email} to:{to_email}')


# #### JavaScript Object Notation (JSON)
# 
# The **JavaScript Object Notation (JSON)** is a file format–with the `.json` extension–used to store data objects represented as attribute-value pairs. We can think of it as an object that usually contains data in the form of lists and dictionaries. This format is specially popular when there is data transfer between web applications and servers. JSON files look as follows. (Also have a look at the `logs.json` file.)
# 
# ```
# {
#     "key_1" : {
#         "key_1_1" : "value_1",
#         "key_1_2" : "value_2",
#         "key_1_3" : [...],
#         ...
#     },
#     ...
# }
# ```
# 
# JSON supports the following formats:
# 
# * **Object:** unordered set of name-value pairs. An object starts with `{` and ends with `}` (similar to a dictionary in Python).
# * **Array:** sequence of values. An array begins with `[` and `]` (similar to a list in Python). 
# * **Value:** can be a string (in double quotes), a number, `true`, `false`, `null`, an object, or an array. 
# 
# In Python, we can use the `json` library to interact with JSON files. We can use the `load()` function which creates a Python object based on [this conversion table](https://docs.python.org/3/library/json.html#json-to-py-table). You can then interact with the data as you normaly do in Pthon.

# In[ ]:


import json

with open('datasets/logs.json') as file:
    data = json.load(file)  # We get a dictionary out from the JSON file
    
    for obj in data:                 # Iterate over all objects (dictionaries) in the array (list)
        typ = obj['type']            # We write typ because type is a reserved word
        timestamp = obj['timestamp']
        from_email = obj['from']
        to_email = obj['to']
        message = obj['message']
        
        print(f'{typ} {message} [{timestamp}] from:{from_email} to:{to_email}')


# #### Extensible Markup Language (XML)
# 
# The Extensible Markup Language (XML) is a markup language and data format used to represent and store arbitrary data structures. The XML language was formalized in the World Wide Web Consortium's XML 1.0 Specification of 1998. It consists of a set of structured *tags*, each one with zero or more *attributes*, and an *element* (characters in between the opening and ending tags). XML files look as follows. (Also have a look at the `logs.xml` file.)
# 
# ```
# <tag_1>
#     <tag_1_1 attr_1="value_1" attr_2="value_2" ...>
#         element_1_1
#     </<tag_1_1>
#     <tag_1_2>
#         element_1_2
#     </<tag_1_2>
#     ...
# </tag_1>
# ```
# 
# In Python, we can use the `xml.etree.ElementTree` library to interact with XML files. We use the `parse()` function to read and parse an XML file. The output of the function is a tree. Trees are out of the scope of this course, but you should know that these are frequent data structures used in computer science and data science. You can traverse the tree to get relevant information from each of its nodes. In the following cell, we show a very simple interaction with the tree structure.

# In[ ]:


import xml.etree.ElementTree as ET

tree = ET.parse('datasets/logs.xml')
root = tree.getroot()                # Get the root node of the tree

for message in root.iter('message'): # Get all tags of type 'message'
    print(message.text)              # and print their text.


# ## Data Cleanse <a class="anchor" id="cleanse"></a>
# 
# The **data cleanse** stage is one of the most important parts of the data preparation process, mainly because is at this moment where faulty data and inconsistencies should be treated. If done incorrectly, the subsequent analysis might result in biased or inaccurate results. Some of the main tasks that should be carried on during the data cleanse stage include:
# 
# * removing *erroneous data*;
# * dealing with *missing values*;
# * *formatting values*, and;
# * masking *sensitive data*.
# 
# How to deal with these and other data issues will depend on the data source you are dealing with. There is no rule of thumb to follow for all cases. However, you can always be conscious about the previously mentioned tasks, and evaluate how to align them with your data. Hereafter, we present the main points to consider when cleaning a dataset.

# <div class="alert alert-info">
#     <b>Data cleanse</b><br>
#     <p>Subprocess within the data analysis stage that focuses on cleaning the data by treating faulty and inconsistent data.<p>
# </div>

# ### Erroneous Data
# 
# When accessing your data, you might encounter noisy or wrong values, duplicated records, or even irrelevant observations.
# 
# * **Noisy or wrong values** can be detected by checking that all values of a given variable are contained within the accepted *domain* of that variable. If not, you need to isolate and analyze these cases. Which values do they have? Do you need to redefine the domain of the variable? Or on the contrary, do you need to remove the record because the data is erroneous? Can you still keep the record and replace the faulty value with a default value, so you do not lose information relevant to other variables? All these questions and many more must be considered when deciding how to deal with noisy or wrong values in your data. Additionally, some outliers might be placed in this category. But beware! Not all outliers are faulty data. You need to further analyze them to draw a valid conclusion.
# * **Duplicated records** (or data redundancy) are also a point of discussion during the data cleanse stage. Do you want to keep them or you must get rid of them? The answer–once again–will depend on the problem at hand. Sometimes keeping duplicated records is required because they show the frequency of an event that is relevant to solve the domain problem. However, oftentimes these duplicates have been wrongly included in the dataset and should be removed to avoid getting biased results.
# * **Irrelevant observations** might also be included in your data. It might happen that you are using a dataset that explores a universe that is not part of the problem you want to solve. For instance, you might have a dataset that reports observations of a given domain for all the continents, but it might be the case that your problem focuses on only one of them. Then, having these extra cases will steer your research in the wrong direction. To avoid these issues, you must get rid of these irrelevant observations.

# ### Missing Values
# 
# Information loss and dropouts or nonresponses are typical causes of missing values. The former usually happens as a consequence of varying accuracy and precision of the different data sources used to extract the dataset; the latter appears when conducting studies that involve surveys or interviews. It is not rare to face cases where certain values are missed in the process of measuring and formatting data. It is up to you as a data scientist to decide how to deal with these cases. The options are pretty similar to the ones you have when dealing with noisy or wrong values; you can decide to ignore these observations and remove them from the dataset or replace them with a default value. If you opt for the latter, you need to carefully decide which is the default value you will be using, is it the mean, the median, a prediction, or a flag (like `-1` or `NaN`) that indicates that the value is missing?

# ### Value Formats
# 
# It is not rare to face observations containing the right data but the wrong format. This is particularly frequent when dealing with dates or timestamps: the format might be different among different records. To properly process this data you will need to define a standard and modify all values accordingly. Each variable must have a specific format, and all values within that variable should comply with it. Be as meticulous as possible when dealing with these cases; even forgetting about capitalizing a word or adding an extra space that does not comply with your format will make you lose a lot of time and effort! 

# ### Sensitive Data
# 
# As a data scientist, you have a big responsibility when dealing with private data. During the last decades, we have witnessed the rise of international regulations–such as the General Data Protection Regulation ([GDPR](https://gdpr.eu/what-is-gdpr/))–that enforces certain security practices to protect the rights and privacy of people involved in data gathering studies. Therefore, sensitive data should be masked in your dataset. **Data masking** is the process of hiding data in the original dataset. It can be performed using **pseudonymization** or **anonymization** (Tachepun, 2020). In the former, data is kept private by transforming it into another form. Some of the techniques used to pseudonymize data are:
# 
# * **Encryption:** plain text data is encoded in ciphertext format. To do so a key and algorithm are used. 
# * **Tokenization:** data is transformed but keeps its uniqueness–that is, the same values will be mapped to the same alternative representation. For instance, every value `'Omar'` will be mapped to the same value (let us say) `'Rolt'`.
# * **Scrambling:** data obfuscation is permanent and there is no way to go back to the original value. 
# 
# In the case of anonymization, we can use the following techniques:
# 
# * **Suppression:** certain characters are replaced by a special symbol such as `*`. For instance, a credit card might be represented as `'**** **** **** 2789'`.
# * **Generalization:** values are discretized–that is, they are replaced by the range in which they are located. For instance, the age `23` can be replaced by `'20-25'`.
# 
# Although extremely important, masking sensitive data is out of the scope of this course.

# ## Data Integration <a class="anchor" id="integration"></a>
# 
# The **data integration** stage is required when dealing with multiple data sources. These independent data sources can be merged or joined together. The main issues faced during this stage involve dealing with:
# 
# * **Schema integration:** you should be able to merge the schemas of the different data sources into one schema. 
# * **Data conflicts:** conflicts can be related to *naming conflicts*, either by introducing synonyms (two variables with different names representing the same feature) or homonyms (two variables with the same name represent different features); *type conflicts*, where the same variable is modeled with a different data type in two sources, and; *domain conflicts*, where the same variable has a different domain in two sources, among others.
# * **Data redundancy:** merging multiple data sources might result in duplicated records or variables. In the former, the duplicated record might be expected if it is describing a different observation with the same attributes. However, the rationale behind keeping or removing a record must be clear. Having redundant information might negatively impact the readability and complexity of your data.

# <div class="alert alert-info">
#     <b>Data integration</b><br>
#     <p>Subprocess within the data analysis stage that focuses on merging or joining multiple data sources.<p>
# </div>

# ## Data Transformation <a class="anchor" id="transformation"></a>
# 
# The **data transformation** stage involves modifying the existing data to *normalize*, *enrich*, *generalize*, or *reduce* it.
# 
# * **Data normalization:** mapping values in the original range of a variable into an output range. Beware that depending on the chosen method distortion or bias might be introduced in the data.
# * **Data enrichment:** data from different variables and sources are added or related resulting in new variables in the dataset. One type of data enrichment is *data aggregation*, which results from the operation of aggregating or summarizing multiple values in one. 
# * **Data generalization:** values of a variable are replaced with high-level factors or ranges. This is useful to perform analysis based on categories.
# * **Data reduction:** data is reduced to ease its manipulation and analysis. Irrelevant variables might be removed. In addition, the number of observations can also be reduced utilizing different techniques such as random sampling.

# <div class="alert alert-info">
#     <b>Data transformation</b><br>
#     <p>Subprocess within the data analysis stage that normalizes, enriches, generalizes, or reduces the data at hand.<p>
# </div>

# ## The Airbnb Case <a class="anchor" id="airbnb"></a>
# 
# ```{image} assets/airbnb.jpeg
# :alt: Airbnb
# :width: 500px
# :align: center
# ```
# 
# <div style="text-align:center">
#     <span style="font-size:0.9em; font-weight: bold;">The Airbnb case.</span>
# </div>
# <br>
# 
# To apply the concepts we have learned in this notebook, we will use an adapted version of the *Airbnb Listings & Reviews* available [here](https://www.kaggle.com/mysarahmadbhat/airbnb-listings-reviews) under a CC0 1.0 Universal license. The dataset contains 279,712 listings of Airbnb in 10 major cities and more than 1 million reviews. The dataset comes in two different CSV files: the `listing.csv` and the `reviews.csv` files. The former contains the following variables.
# 
# | Variable   | Description |
# |------------|-------------|
# | `listing_id`           | ID of the listing in Airbnb |
# | `name`                 | Name of the listing |
# | `neighbourhood`        | Neighbourhood where the listing is located |
# | `district`             | District where the listing is located |
# | `city`                 | City where the listing is located |
# | `property_type`        | Type of the property (e.g. entire apartment, private room) |
# | `room_type`            | Type of (e.g. entire place, hotel room) |
# | `accommodates`         | Maximum number of guests |
# | `amenities`            | Amenities of the listing |
# | `price`                | Price of the listing in local currency |
# | `review_scores_rating` | Listing's overall rating (out of 100) | 
# 
# The latter contains the following features:
# 
# | Variable   | Description |
# |------------|-------------|
# | `listing_id` | ID of the listing in Airbnb |
# | `review_id`  | Id of the review |
# | `date`       | Date when the review was posted |
# 
# 
# ### Data Preparation
# In this opportunity, we are in charge of preparing the data for the coming data analysis stages. To do so, we have identified some requirements defined as follows.
# 
# | Requirement | Subprocess | Aspect | Requirement |
# |-------------|:-----------|:-------|:------------|
# | R1 | Data access | -      | Access the `listings.csv` file |
# | R2 | Data access | -      | Access the `reviews.csv` file  |
# | R3 | Data access | -      | Represent the listings dataset as a dictionary of dictionaries |
# | R4 | Data transformation  | Data enrichment | Count the number of reviews of a listing |
# | R5 | Data integration | - | Add the number of reviews variable to the listings dataset |
# | R6 | Data cleanse | Erroneous/Noisy data  | Remove non-reviewed listings |
# | R7 | Data cleanse | Missing values        | Replace empty rating values by -1 |
# | R8 | Data cleanse | Data format/type)     | Change the data types of the `accommodates`, `price`, and `review_scores_rating` to numeric |
# | R9 | Data transformation | Data reduction | Remove the `district` variable |
# | R10 | Data store  | -    | Store the prepared dataset | 
# 
# Hereafter, we will use Python to address each of these requirements.

# #### R1. Access the `listings.csv` file
# 
# We open the `listings.csv` file and we print its header and the first two rows to see its content.

# In[ ]:


with open('datasets/listings.csv') as file:
    for i in range(0,3):  # Print header and first two rows
        print(file.readline().rstrip()) 


# #### R2. Access the `reviews.csv` file
# 
# As we did before, we open now the `reviews.csv` file and we print its header and the first two rows to see its content.

# In[ ]:


with open('datasets/reviews.csv') as ratings_file:
    for i in range(0,3): # Print header and first two rows
        print(ratings_file.readline().rstrip())


# #### R3. Represent the listings dataset as a dictionary of dictionaries
# 
# After reading the CVS file we will transform it into a dictionary of dictionaries. The keys of the parent dictionary will be the listing IDs. Regarding the keys of the nested dictionaries, they will be named as the remaining variables of the dataset. The file has some strange characters that cannot be read properly, that is why we have added the `encoding='utf8', errors='ignore'` arguments to the `open()` function; all erroneous characters will be ignored.

# In[ ]:


import csv
from typing import Dict, List

def access_data(path_listings: str) -> Dict[str, Dict[str, any]]:
    """ Accesses and returns the listings dataset 
        as a dictionary of dictionaries. Keys are 
        listing_ids.
    """
    listings = dict()
    
    with open(path_listings, encoding='utf8', errors='ignore') as file: # Ignore erroneous characters
        reader = csv.DictReader(file)
        
        for row in reader:
            listing_key = row['listing_id']  # Get listing ID
            listing_val = dict()             # Create nested dictionary
            
            for key in row.keys():
                if key != 'listing_id':          # For all variables in the CSV file we will
                    listing_val[key] = row[key]  # create an item in the nested dictionary
                    
            listings[listing_key] = listing_val  # Add the nested dict to the parent dict
    
    return listings

data = access_data('datasets/listings.csv')
data['281420']


# #### R4. Count the number of reviews of a listing
# 
# We want to aggregate the data of the reviews–that is, we want to count the total number of reviews for each listing. For that, we create the function `agggregate_reviews()` with takes the `reviews.csv` path as a parameter and returns a dictionary where the key represents the listing ID and the value represents the number of reviews.

# In[ ]:


import csv
from typing import Dict, List

def agggregate_reviews(path: str) -> Dict['str', int]:
    """ Returns a dictionary where listing IDs are 
        mapped to the number of reviews in the given
        file.
    """
    reviews = dict()
    
    with open(path) as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            listing_id = row['listing_id']      # Get listing ID
            count = reviews.get(listing_id, 0)  # Get previous count or initialize it to 0
            reviews[listing_id] = count + 1     # Add one to the count
            
    return reviews


# #### R5. Add the number of reviews variable to the listings dataset
# 
# We will enrich the listings dataset with the aggregated reviews–that is, we will add a new key (a.k.a `reviews`) to the nested dictionaries. This new item will display the number of reviews associated with the listing.

# #### R6. Remove non-reviewed listings
# 
# We only care about listings with reviews. The other observations will be excluded in the data analysis stages. Thus, we need to remove all these cases from the data.
# 
# **Note:** to favor performance, we will comply with both requirements (R5 and R6) in the following code cell.

# In[ ]:


def access_data(path_listings: str, path_reviews: str) -> Dict[str, Dict[str, any]]:
    """ Accesses and returns the listings dataset 
        as a dictionary of dictionaries. Keys are 
        listing_ids.
    """
    listings = dict()
    
    with open(path_listings, encoding='utf8', errors='ignore') as file:
        reviews = agggregate_reviews(path_reviews)  # Get the reviews variable
        reader = csv.DictReader(file)
        
        for row in reader:
            listing_key = row['listing_id'] # Get listing ID
            listing_val = dict()            # Create nested dictionary
            
            for key in row.keys():
                if key != 'listing_id':          # For all variables in the CSV file we will 
                    listing_val[key] = row[key]  # create an item in the nested dictionary
            
            listing_val['reviews'] = reviews.get(listing_key, 0)  # Integrate data: add reviews variable
            listings[listing_key] = listing_val                   # Add the nested dict to the parent dict
    
    return listings

data = access_data('datasets/listings.csv', 'datasets/reviews.csv')
data['281420']


# #### R7. Replace empty rating values by -1
# 
# Given a nested listing dictionary, we aim at replacing all empty rating values with -1. For that purpose, we define the function `replace_empty_rating()`, which takes a nested listing dictionary and modifies it accordingly. This function will be used later.

# In[ ]:


def replace_empty_rating(listing: Dict[str, any]) -> Dict[str, any]:
    """ Replaces all empty rating values by -1.
    """
    rating = listing['review_scores_rating']   # Get rating value
        
    if rating == '':                           # If empty
        listing['review_scores_rating'] = '-1' # assign the '-1' value
        
        
    return listing


# #### R8. Change the data types of the `accommodates`, `price`, and `review_scores_rating` to numeric
# 
# Now, we would like to modify the types of the `accommodates`, `price`, and `review_scores_rating` to integer values. Thus, we define the function `change_data_types()`, which takes a nested listing dictionary and modifies it accordingly. This function will be used later.

# In[ ]:


def change_data_types(listing: Dict[str, any]) -> Dict[str, any]:
    """ Changes the types of the accommodates, price,
        and review_scores_rating to integer.
    """
    listing['accommodates'] = int(listing['accommodates'])
    listing['price'] = int(listing['price'])
    listing['review_scores_rating'] = int(listing['review_scores_rating'])
        
    return listing


# #### R9. Remove the district variable
# 
# Lastly, we have seen that the `district` variable is error-prone–it has many empty values. We do not consider that this variable is relevant for our analysis. Therefore, we will remove it from the nested dictionaries. We define then the `remove_district_var()`, which modifies a nested listing accordingly. The function will be used later.

# In[ ]:


def remove_district_var(listing: Dict[str, any]) -> Dict[str, any]:
    """ Removes the district item from the dictionary.
    """
    del listing['district'] # Remove the district key-value from the dict
    return listing


# #### Apply R7, R8, and R9
# 
# We will now use the functions defined previously to clean and transform our dataset.

# In[ ]:


def create_dataset(data: Dict[str, Dict[str, any]]) -> Dict[str, Dict[str, any]]:
    """ Creates, cleans and transforms the Airbnb dataset.
    """
    clean_data = dict()
    
    for listing_id in data:
        listing = data[listing_id]
        reviews = listing['reviews']
        
        if reviews == 0:                                       # Data cleanse: Remove non-reviewed listings
            continue
        
        clean_data[listing_id] = listing
        clean_data[listing_id] = replace_empty_rating(listing) # Data cleanse: Replace empty ratings by -1
        clean_data[listing_id] = change_data_types(listing)    # Data cleanse: Change data types
        clean_data[listing_id] = remove_district_var(listing)  # Data transformation: Remove district variable
       
    return clean_data

dataset = create_dataset(data)
dataset['281420']


# #### R10. Store the prepared dataset
# 
# Finally, we will store the resulting dataset in a new CSV file, so we avoid performing the same cleaning every time we need to analyze the data.

# In[ ]:


def store_data(data: Dict[str, Dict[str, any]], path: str) -> None:
    """ Stores the dataset in the file given as a parameter.
    """
    with open(path, 'w') as outfile:
        varnames = [
            'name',
            'neighbourhood',
            'city',
            'property_type',
            'room_type',
            'accommodates',
            'amenities',
            'price',
            'review_scores_rating',
            'reviews'
        ]
        writer = csv.DictWriter(outfile, fieldnames=varnames)
        writer.writeheader()
        
        for key in data:
            writer.writerow(data[key])
            
store_data(dataset, 'datasets/out_listings.csv')


# We made it! The data is ready to be used for the EDA and confirmatory data analysis stages.
