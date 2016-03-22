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

	
###Q2. Lists &amp; Sets

**How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?**

In the question above, I have already described the essence of a list. A set is an unordered collection of unique items whose primary purpose is in being used to tell whether an item is or is not in it. When you're outside your home, a common question might be do I have my charger? do I have my notebook? A set can be viewed as a bag. You either have the item or you don't. You don't really care about 'where it is' in relation to the other items in the bag.

Another example could be the set of groceries to buy at the store. Let's say you you have a piece of paper on your refrigerator where you add an item when you realize it needs to be bought. On Monday, you add "coffee", Tuesday "eggs", Wedesday "avocados", thursday "grapes", and then on Friday you really wanted Eggs Benedict but in realizing you don't have eggs, you add "eggs" again. When you are really to go to the store, the fact that "eggs." However, for the purposes of shopping at the store, you only need to visit the eggs section once regardless of how many times you thought about buying it. If you turn your paper into a set, all the duplicates get removed:

	>>> paper = ["coffee","eggs","avocados","grapes","eggs"]
	>>> groceries = set(paper)
	>>> groceries
	set(['coffee', 'avocados', 'eggs', 'grapes'])


Then, when you're going through the isles and looking at all the colorful items, you can quickly check if an item is on the set of groceries to buy:

	>>> "eggs" in groceries
	True
	>>> "milk" in groceries
	False


**Performance on checking for membership is faster for sets than lists.** As sets are implemented using hash tables, membership testing is essentially constant O(1) regardless of the size of the set. Lists, in contrast are implemented as dynamic arrays. Membership testing in lists therefore requires testing elements sequentially for equality and thus changes based on the size of the list: O(n). As a result, it takes longer and longer as the list becomes bigger and bigger. It should be noted that this difference only really applies for larger sets/lists... the difference may be negligable for small or medium ones.

**To summerize some of the finer details...**

**Similarities:**

1. *Iteration* - Both allow for iteration.

		for item in groceries:      
		  print item


2. *Length / Item count* - Both provide the number of elements in the container using the len() function.

3. *Mutability, to some extent* - (Like lists) Items in sets can be added and removed, but only if you know what they are first. In sets, is done via methods like update, remove, pop, etc. This has its peculiarities with sets however...


		>>> groceries
		set(['coffee', 'eggs', 'grapes', 'avocados'])

		# Adding "milk" - wrong way
		>>> groceries.update("milk")
		>>> groceries
		set(['coffee', 'i', 'eggs', 'm', 'l', 'grapes', 'avocados', 'k'])

		# Adding "milk" - right way
		>>> groceries.update(["milk"])
		>>> groceries
		set(['coffee', 'i', 'eggs', 'm', 'l', 'milk', 'grapes', 'avocados', 'k'])

		# Removing the coffee...
		>>> groceries.remove("coffee")
		>>> groceries
		set(['i', 'eggs', 'm', 'l', 'milk', 'grapes', 'avocados', 'k'])


**Differences:**

1. *Syntax* - Lists use [] whereas sets use {}.

2. *Dupicates* - Lists allow for duplicates, but sets do not.

3. *Special "Set" functionality :Union/Intersection/Difference* - Sets suport special functionality for comparing sets:


		>>> a
		set([1, 2, 3, 4])
		>>> b
		set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
		>>> a & b		#Letters in both a and b
		set([1, 2, 3, 4])
		>>> a - b		#Letters in a but not in b
		set([])
		>>> b - a		#Letters in b but not in a
		set([5, 6, 7, 8, 9, 10, 11, 12])
		>>> a ^ b		#Letters in a but not in b
		set([5, 6, 7, 8, 9, 10, 11, 12])
		>>> a | b		# Letters in either a or b
		set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

		>>> a.difference(b)
		set([])
		>>> b.difference(a)
		set([5, 6, 7, 8, 9, 10, 11, 12])
		>>> a.issubset(b)
		True
		>>> b.issubset(a)
		False
		>>> a.issuperset(b)
		False
		>>> b.issuperset(a)
		True


4. *Comparing & Sorting* - Unlike lists (described above), sets are compared only by the sheer number of elements contained within them:

		>>> a
		set([1, 2, 3, 4])
		>>> b
		set([0, 1, 2, 3, 4])
		>>> a>b
		False
		>>> b>a
		True

4. *Types of Values* - Lists can have any kind of element, but tuples can only have hashable elements. That is, lists can have lists as elements, but sets cannot. Both can have strings, numbers, and tuples.

		>>> a
		set([1, 2, 3, 4])				# Set contains only integers

		>>> a.update("abc")
		>>> a
		set(['a', 1, 2, 3, 4, 'c', 'b']) 	# Set containers integers & characters

		>>> a.update([tuple])
		>>> a							# Set includes a tuple
		set(['a', 1, 2, 3, 4, 'c', ('abc', 'bcd', 'dep'), 'b'])

		>>> list
		[1, 2, 3, 4, 5]
		>>> a.update([list])				# Set can’t add a list
		Traceback (most recent call last):
		File "<stdin>", line 1, in <module>
		TypeError: unhashable type: 'list'


###Q3. Lambda Function

**Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.**

A 'lambda' in python can be thought simply as a 1-time or disposable function. It is a way of defining a particular function-ality, but without going through the full process of actually defining a function. Because no function is ever defined and given a name, it can't be used outside of the given context or scope from which it is defined. Because a name is never given to the function/functionality, it is also called setting up an 'anonymous function."

**Example #1:** Here's an example where you have a list of ages. If I want to only see those ages which are greater than 25, I can use a lambda function with filter to accomplish that quickly...

	>>> ages_list = [4,5,63,6,53,23,41]
	>>> filter(lambda x: x>=15, ages_list)
	[63, 53, 23, 41]

**Example #2:** If instead of a tuple, the same information was contained in a dictionarywhere people's names are keys and their value pairs are the ages. If I wanted to sort these people by their ages, I could use a lambda in the "key" aregument of sorted:

	>>> ages_dict = {
				'carl' : 4, 
				'danny': 5,
				'matt': 63,
				'roxanne':6,
				'bjork': 53,
				'madonna':23,
				'shepard':41}

	>>> sorted(ages_dict.iteritems(), key = lambda (k,v):(v,k))
	[('carl', 4), ('danny', 5), ('roxanne', 6), ('madonna', 23), ('shepard', 41), ('bjork', 	53), ('matt', 63)]


**Example #3:** A simpler example could occur if one had a list of tuples of celebrity information. One can easily sort by different fields by entering a different index from within the lambda notation. 

	celebrity_info = zip(names,ages,income)
	In[62]: celebrity_info
	Out[59]: 
		[('matt', 63, 1300300),
		 ('matt', 5, 10599000),
		 ('danny', 4, 55000),
		 ('carl', 41, 240000),
		 ('shepard', 6, 16000),
		 ('roxanne', 53, 2834500),
		 ('bjork', 23, 1300300)]
 
	#Sorting by age... 
	In[63]: sorted(celebrity_info, key = lambda person: person[1])
	Out[60]: 
		[('danny', 4, 55000),
		 ('matt', 5, 10599000),
		 ('shepard', 6, 16000),
		 ('bjork', 23, 1300300),
		 ('carl', 41, 240000),
		 ('roxanne', 53, 2834500),
		 ('matt', 63, 1300300)]
	 
	#Sorting by income...
	In[64]: sorted(celebrity_info, key = lambda person: person[2])
	Out[61]: 
	[('shepard', 6, 16000),
	 ('danny', 4, 55000),
	 ('carl', 41, 240000),
	 ('matt', 63, 1300300),
	 ('bjork', 23, 1300300),
	 ('roxanne', 53, 2834500),
	 ('matt', 5, 10599000)]
	
References:
http://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
http://pythoncentral.io/lambda-function-syntax-inline-functions-in-python/

---

###Q4. List Comprehension, Map &amp; Filter

**Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.**

**Part 1: What are comprehensions?**

"Comprehensions," be it list comprehensions, set comprehensions, or dictionary comprehenses are very concise way to create lists, sets, and dictionaries, respectively. This concision derives from the fact that each container is generated by providing a description of what the elements in the set are using techniques like ranges, loops, boolean operators and relational operators instead of the typical way which is to the explicitely mention the element. 

Let's say we wanted a list of all the number between 0 and 20 which are divisble by 3 and whose squares are less than 50. The traditional way would be to write out the members like this:

	list = [0,3,6]

It's quite possible, however, that one doesn't know these numbers off the top of their head or just recognizes that a computer can do this much faster and with lower probability of error (especially as conditions become more complicated and the ranges become bigger). In this case, we can use a list comprehension to generate such a list:

	list = [x for x in range(0,21) if x**2<50 and x % 3 == 0]

Within Python, it reads almost like English: give me all x that are in the range from 0 to 20 if x squared is less than 50 and x is divisible by 3.


**Part 2: Comprehension Syntax for Lists, Sets, and Dictionaries**

The bare minimum syntax for a list comprehensions and set comprehensions generally follows the the structure below. Sets just use curly brackets"{}" instead of straight ones "[.]"

[**Desired Ouput** for **certain variable** in **some range/iterable** if **some optional condition(s) are met**]

Here are some additional examples:

	
	# Powers of Two (for lists):
	powers_2_list = [2 ** i for i in range(10)]
	[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
	
	# Powers of Two that are between 50 and 200.
	# Note how this makes use of a pre-existing list, powers_2
	[x for x in powers_2_list if x>50 and x<200]
	[64, 128]
	
	# The same, for sets
	powers_2_set = {2 ** i for i in range(10)}
	{1, 2, 4, 8, 16, 32, 64, 128, 256, 512}
	{x for x in powers_2_list if x>50 and x<200}
	{64, 128}


The syntax for dictionaries is fairly similar except one needs to specify both the keys and the values

[**Desired Key**:**Desired Vale** for **certain variable** in **some range/iterable** if **some optional condition(s) are met**]

Here is a dictionary created that pairs numbers with letters of the alphabet with numbers. This could easily be the basis of many a cryptographic key....

	>>> import string
	>>> alpha = string.uppercase
	>>> alpha
	'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	
	>>> {i+1:alpha[i] for i in range(26)}
	{1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}

Here is a more complicated example. Assume you have a list of tuples with celebrities' names. If you wanted to create dictionary where the key is the name and the value is the length of their full name, this could easily be done with the following:

	>>> names
	[('Lenny', 'Kravitz'),
	 ('Jessica', 'Alba'),
	 ('Kirsten', 'Durst'),
	 ('Kate', 'Beckinsale')]

	>>> {i:len(i[0]+i[1]) for i in names}
	{('Jessica', 'Alba'): 11,
	 ('Kate', 'Beckinsale'): 14,
	 ('Kirsten', 'Durst'): 12,
	 ('Lenny', 'Kravitz'): 12}
	
**Part 3: Comprehensions vs. Maps & Filters**

In general, most things you can do with list comprehensions you can also do with filters and maps. In cases where the "construction rule is too complicated to be expressed with "for" and "if" statements, or if the construction rule can change dynamically at runtime....in this case, you better use map() and / or filter() with an appropriate function." (Secnetix link)

Example 1: Both are used to express the same thing.



Example 2: When a map/filter doesn't work, use a list comprehension
Example 3: When a list comprehension doesn't work, use a map/filter

quote = "Courage is not the absence of fear, but rather the judgement that something else is more important than fear."


To see how list comprehensions compare with maps and filters. Let's start with a simple sequence:

	>>> numbers = range(11)
	>>>	numbers
	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

If I wanted to filter out only those numbers which were divisble by 2, I could use filter or a list comprehension:

	>>> filter(lambda x:x % 2 == 0, numbers)
	[0, 2, 4, 6, 8, 10]

	>>>[x for x in numbers if x % 2 == 0]
	[0, 2, 4, 6, 8, 10]

Alternatively, if I wanted to get the squares of all the numbers, I could us the map() function:

	>>> map(lambda x:x**2, numbers)
	[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	
	[x**2 for x in numbers]
	[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


The following is an example where the construction rule changes based on the input. Here, a list comprehension wouldn't work.

	def squash_negatives(input):
		if input < 0:
			return 0
		if input >= 0:
			return input
		
	>>> my_list
	[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	
	>>> map(squash_negatives,my_list)
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

**References:**

- [Secnetix](http://www.secnetix.de/olli/Python/list_comprehensions.hawk)
- [Stack Overflow](http://stackoverflow.com/questions/1747817/create-a-dictionary-with-list-comprehension-in-python)
- [Python.org](https://www.python.org/dev/peps/pep-0274/)

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





