# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    
    if type(count) == int:
        if count < 10:
            print "Number of donuts: %s" % (count)
        else:
            print "Number of donuts: many" 
    else:
        print "Please enter the number of donuts as an integer value."
    

def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    
    if type(s) == str:
        if len(s) < 2: 
            print ""
        else:
            front = s[:2]
            back = s[-2:]
            print front + back
    else:
        print "Please enter the string as an input."


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """

    if type(s) == str:
        #Isolates the first letter of the string.
        first_letter = s[:1]
        #Isolates everythign but first letter of the string.
        rest_of_word = s[1:]
        
        # Replaces all letters in rest of the string which match the first letter with an asteristk.
        # Adds the first letter back to complete the string.
        print first_letter + rest_of_word.replace(first_letter, "*")
    else:
        print "Please enter the string as an input."

    """References:
    http://www.tutorialspoint.com/python/string_replace.htm"""

def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    
    """First 2 char of "b" --> All but first 2 char of "a" -> space -> First 2 char of "a" --> All but first 2 char of "b"
    
    For reasons of efficiency, join is preferred for concatenating more than 2 strings at a time. See references below.
    http://stackoverflow.com/questions/10043636/any-reason-not-to-use-to-concatenate-two-strings
    http://stackoverflow.com/questions/2711579/concatenate-strings-in-python-2-4
    """

    # Simple but inefficient version when scaled:
    # mix_up_word = b[:2] + a[2:] + " "+ a[:2] + b[2:]
    
    mix_up_word = "".join((b[:2], a[2:]," ",a[:2],b[2:]))
    
    return mix_up_word
    print mix_up_word

def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """

    if len(s) < 3:
        print s
    elif s[-3:] == "ing":
        print s + "ly"
    else:
        print s + "ing"

def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    not_location = s.find("not")  
    bad_location = s.find("bad")

    """ The whole 'not'...'bad' substring should start at the the 
    same first instance of "not" and end 2 charachters after where "bad" starts...
    but that needs to be bumped up to 3 b/c python indexes off of 0..."""

    if not_location < bad_location:
        # Everything before the "not" -> good -> everything after the bad
        print s[:not_location] + "good" + s[bad_location+3:]
    else:
        print s

def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    
    """ Note: I could import math and use the cieling function, but choosing to do it this way to avoid importing...
    References: http://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python
    """

    def word_splitter(str):
        length = len(str)
        # Gives you the midpoint if it's even, or the midpoint rounded up if it's odd.
        special_midpoint = int(length / 2) + (length % 2 > 0)
        # front = str[:special_midpoint]
        #back = str[special_midpoint:]
        string_split = {"front" : str[:special_midpoint] , "back" : str[special_midpoint:]}
        return string_split

    # Change a & b from strings into dictionaries composed of front and back keys:
    a = word_splitter(a)
    b = word_splitter(b)

    # Printing as defined by the assignment:
    print a['front'] + b['front'] + a['back'] + b['back']