# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Question Status: In progress
Python lists and tuples are similar in that they both hold collections of values. By examining some "prototypical" examples of each, we can best understand the differences between these two data structures, what each is ideally suited for and therefor why one would use one over another. Note, in certain cases one is "softly" urged to use one data structure over another because one's only been acquanted with examples that use that particular datatype. In other cases, one is "hard"-forced to use a particular data structure because of the constraints of Python. 

The List -- The foundamental and most easy to understand data structure which is a collection of objects is a list.
A list is most closely defined as a "sequence of values."

A list can be defined as:


(both 'softly'-implied through it's usage hard-implied through the constraints of Python)
>> Python Lists are different 


>> Python Lists & Tuples: Similarities

>> Python Lists & Tuples: Differences -- The differences betwen lists and tuples are the following:
- Heteogenity/Homoegenity of objects: Generally lists work better for objects of the same type (although it's not forced by), whereas tuples are more for heterogenous objects.
- Structured vs. Unstructured - Tuples have structure, whereas lists of have order. As a consequence of tuples being designed for different types of objects, the position of each type of object creates a specific structure.

- Mutability: Lists are mutable; Tuples are not. while the heterogenity/homogenity is suggested,, the structured/unstructuredness is baed on an individuals pov, 

References:
http://stackoverflow.com/questions/626759/whats-the-difference-between-list-and-tuples#


Tupples are more ideal to being used to store keys in dictionaries beccause they are immutale)


---



###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> REPLACE THIS TEXT WITH YOUR RESPONSE
Question Status: In progress
>>
>>
>>


---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

A 'lambda' in python can be thought simply as a 1-time or disposable function. It is a way of defining a particular function-ality, but without going through the full process of actually defining a function. Because no function is ever defined and given a name, it can't be used outside of the given context or scope from which it is defined. Because a name is never given to the function/functionality, it is also called setting up an 'anonymous function."

Example #1: Here's an example where you have a list of ages. If I want to only see those ages which are greater than 25, I can merely use a lambda function with filter to accomplish that quickly...

>>> ages_list = [4,5,63,6,53,23,41]
>>> filter(lambda x: x>=15, ages_list)
[63, 53, 23, 41]

Example #2: Let's say instead had a dictionary of ages, where people's names are keys and their value pairs are the ages. If I wanted to sort these people by their ages, I could use a lambda in the "key" aregument of sorted:

>>> ages_dict = {
	'carl' : 4, 
	'danny': 5,
	'matt': 63,
	'roxanne':6,
	'bjork': 53,
	'madonna':23,
	'shepard':41}

>>> sorted(ages_dict.iteritems(), key = lambda (k,v):(v,k))
[('carl', 4), ('danny', 5), ('roxanne', 6), ('madonna', 23), ('shepard', 41), ('bjork', 53), ('matt', 63)]

References:
http://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

Part a: The number of days between 01-02-2013 and 07-28-2015 is 937 days.


b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

Part b: The number of days between 12312013 and 05282015 is 513 day.

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

Part c: The number of days between 15-Jan-1994 and 14-Jul-2015 is 7850 days.

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





