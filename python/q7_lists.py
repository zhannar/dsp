# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    count = 0

    for word in words:        
        # Passes over all empty or 1 letter inputs in the list.
        if len(word) >= 2: 
            # Passes over those words which don't have the first letter match the last letter.
            if word[0] == word[-1]:
            # Bumps the count for all words which pass both requirements.    
                count += 1
            else:
                continue            
        else:
            continue
    print count

"""Test Cases -- All passed
match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
match_ends(['', 'x', 'xy', 'xyx', 'xx'])
match_ends(['aaa', 'be', 'abc', 'hello'])
"""

def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """

    # Disclaimer: This code doesn't account for uppercase words. This is a feature to 
    # possibly add later. 

    """Step 1 - This outer logic will iteratively go through each word in the list, 
    and assign the items in the list to either a list of words that begin with 
    the special letter, or words which don't."""

    special_letter = "x"
    special_words_list = []
    other_words_list = []

    for word in words:
        if word[0] == special_letter:
            special_words_list.append(word)
        else:
            other_words_list.append(word)

    """Step 2 - Sorts the two lists alphabettically."""
    special_words_list.sort()
    other_words_list.sort()

    """Step 3 - Recombines the two lists."""
    sorted_words = special_words_list + other_words_list
    print sorted_words
    return sorted_words
    
"""Test Cases -- All passed
front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
"""

def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """

    """Method 1: Defines a function to determine which key to sort the tuples from.
    Then sorts it.
    References: http://pythoncentral.io/how-to-sort-a-list-tuple-or-object-with-sorted-in-python/
    
    def getKey(tuple):
        return tuple[-1]
    print sorted(tuples, key = getKey)
    """

    """Method 2: This is a bit more condennsed as it uses a lambda to 
    define the function and carry it out in the same step."""
    
    print sorted(tuples, key = lambda tuple: tuple[-1])    

    
"""Test Cases -- All passed
sort_last([(1, 3), (3, 2), (2, 1)])
sort_last([(2, 3), (1, 2), (3, 1)])
sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
"""

def remove_adjacent(numbers):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """
    
    last_number = None
    remove_adjacent_list = []

    for current_number in numbers:          #Begins to look through list, number by number
        if last_number == current_number:   #If there are adjacent equal numbers, moves on
            pass
        else:
            remove_adjacent_list.append(current_number)
            last_number = current_number    #Once the number has been added to the list, it becomes the new 'last number'

    print remove_adjacent_list

"""Test Cases -- All passed
remove_adjacent([1, 2, 2, 3])
remove_adjacent([2, 2, 3, 3, 3])
remove_adjacent([3, 2, 3, 3, 3])
remove_adjacent([])
"""

def linear_merge(left, right):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.

    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """
    
    """References: This is a python-ified version of the stackoverflow code which 
    seems to draw upon the wikipedia article.
    http://stackoverflow.com/questions/3051603/how-to-merge-two-ordered-list-of-objects
    http://stackoverflow.com/questions/11039217/time-complexity-for-merging-two-sorted-arrays-of-size-n-and-m
    http://stackoverflow.com/questions/10393627/merging-two-sorted-arrays-into-a-third-one-can-be-done-in-on

    """
    result = []

    while len(left) > 0 and len(right) > 0:   # As long as the two comparing sets aren't empty...
        """
        Uncomment for debugging purposes
        print "This is the left list, originally: %s" % (left)     
        print "This is the right list, originally: %s" % (right)
        """

        if left[0] <= right[0]:             # If the first value of the left set is smaller than the first value of the right set...
            result.append(left[0])              # Then add it must be the smallest number, and we add it to our result list...
            left = left[1:]                   # The left list gets redefined to remove the first element.
        else:
            result.append(right[0])         # Otherwise, the first value of the right set is smaller than the one on the left... we add it to the result list.
            right = right[1:]               # The left list gets redefined to remove the first element.  
        
        """
        Uncomment for debugging purposes
        print "This is the left list, : %s" % (left)
        print "This is the right list, : %s" % (right)
        print "This is the result list, : %s" % (result)
        """
        
    # Once one of the lists becomes empty, the other non-empty set must have numbers which are all greater, so we just add it to the end of our result list. 
    # Note that the syntax of adding the remaining elements is slightly different than above as we may be adding more than one element at a time to result.
    if len(left) > 0:
        result = result + left
    else: 
        result = result + right
    print result


"""Test Cases -- All passed
linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
"""