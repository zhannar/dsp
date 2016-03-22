# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

**How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?**

This is an example of Python lists:

	my_list = [0,1,2,3,4]
	my_list = ["Bohemian Rhapsody","Kashmir","Sweet Emotion", "Fortunate Son", "LA Woman"]

This is an example of Python tuple:

	my_tuple = (a,b,c,d,e)
	my_tuple = ("John", "Wayne", 90210, "Actor", "Male", "Dead")

Python lists and tuples are similar in that they both are ordered collections of values. Besides the shallow difference that lists are created using brackets "[ ... , ... ]" and tuples using parentheses "( ... , ... )", the core technical "hard coded in Python syntax" difference between them is that the elements of a particular tuple are immutable whereas lists are immutable (...so only tuples are hashable and can be used as dictionary/hash keys!). This gives rise to differences in how they can or can't be used (enforced a priori by syntax) and differences in how people choose to use them (encouraged as 'best practices,' a posteriori, this is what *smart* programers do). The main difference a posteriori in differentiating when tuples are used versus when lists are used lies in what *meaning* people give to the order of elements. 

For tuples, 'order' signifies nothing more than just a specific 'structure' for holding information. What values are found in the first field can easily be switched into the second field as each provides values across two different dimensions or scales. They provide answers to different types of questions and are typically of the form: *for a given object/subject, what are its attributes?* The object/subject stays constant, the attributes differ.

For lists, 'order' signifies a sequence or a directionality. The second element *MUST come after* the first element because it's positioned in the 2nd place based on a particular and common scale or dimension. The elements are taken as a whole and mostly provide answers to a single question typically of the form, *for a given attribute, how do these objects/subjects compare?* The attribute stays constant, the object/subject differs.

There are countless examples of people in popular culture and programmers who don't conform to these differences and there are countless people who might use a salad fork for their main course. At the end of the day, it's fine and both can usually get the job done. 

**To summerize some of the finer details...**

**Similarities:**

1.	*Duplicates* - Both tuples and lists allow for duplicates
2.	*Indexing, Selecting, & Slicing* - Both tuples and lists index using integer values found within brackets. So, if you want the first 3 values of a given list or tuple, the syntax would be the same:


		>>> my_list[0:3]
		[0,1,2]
		>>> my_tuple[0:3]
		[a,b,c]

3.	*Comparing & Sorting* - Two tuples or two lists are both compared by their first element, and if there is a tie, then by the second element, and so on. No further attention is paid to subsequent elements after earlier elements show a difference.

		>>> [0,2,0,0,0,0]>[0,0,0,0,0,500]
		True
		>>> (0,2,0,0,0,0)>(0,0,0,0,0,500)
		True


**Differences:** - A priori, by definition

1. *Syntax* - Lists use [], tuples use ()

2. *Mutability* - Elements in a given list are mutable, elements in a given tuple are NOT mutable. 

		# Lists are mutable:
		>>> my_list
		['Bohemian Rhapsody', 'Kashmir', 'Sweet Emotion', 'Fortunate Son', 'LA Woman']
		>>> my_list[1]
		'Kashmir'
		>>> my_list[1] = "Stairway to Heaven"
		>>> my_list
		['Bohemian Rhapsody', 'Stairway to Heaven', 'Sweet Emotion', 'Fortunate Son', 'LA Woman']
		
		# Tuples are NOT mutable:		
		>>> my_tuple
		('John', 'Wayne', 90210, 'Actor', 'Male', 'Dead')
		>>> my_tuple[5]
		'Dead'
		>>> my_tuple[5]="Alive"
		Traceback (most recent call last):
		File "<stdin>", line 1, in <module>
		TypeError: 'tuple' object does not support item assignment

3. *Hashtables (Dictionaries)* - As hashtables (dictionaries) require that its keys are hashable and therefore immutable, only tuples can act as dictionary keys, not lists.

		#Lists CAN'T act as keys for hashtables(dictionaries)
		>>> my_dict = {[a,b,c]:"some value"}
		Traceback (most recent call last):
		File "<stdin>", line 1, in <module>
		TypeError: unhashable type: 'list'

		#Tuples CAN act as keys for hashtables(dictionaries)
		>>> my_dict = {("John","Wayne"): 90210}
		>>> my_dict
		{('John', 'Wayne'): 90210}

Differences - A posteriori, in usage

1. Homo vs. Hetereogeneity of Elements - Generally list objects are homogenous and tuple objects are hetereogenious. That is, lists are used for objects/subjects of the same type (like all presidential candidates, or all songs, or all runners) whereas  although it's not forced by), whereas tuples are more for heterogenous objects.

2. Looping vs. Strucutres - Although both allow for looping (for x in my_list...), it only really makes sense to do it for a list. Tuples are more appropriate for structuring and presenting information (%s %s residing in %s is an %s and presently %s % ("John","Wayne",90210, "Actor","Dead"))
Lists are for looping, tuples are for structures i.e. "%s %s" %tuple.
	
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





