# Quick setup
Make a new folder off your home directory and clone the GitHub repo
```bash
$ cd ~
$ mkdir isc && cd isc
$ git clone https://github.com/infoscout/python-bootcamp-pv.git
```
Next, open and add the `python-bootcamp-pv` project to your IDE of choice. Once that is complete fire up the python interpreter and we can begin!

## Integers
```
>>> a = 42
>>> a
42
>>> b = 99
>>> print b * 4
396
>>>
```

## Strings
```
>>> a = 'Hello'
>>> print a
Hello
>>> s1 = 'InfoScout'
>>> s2 = ' is awesome'
>>> print s1 + s2
InfoScout is awesome
>>>
```

## String Methods
There are a number of methods available for string objects
```
>>> s = '    Puerto Vallarta  '
>>> len(s)
21
>>> s.lower()
'    puerto vallarta  '
>>> s.strip()
'Puerto Vallarta'
>>> s.lower().strip()
'puerto vallarta'
>>>
```
What other methods are available to strings (or any object)? Use the very helpful `dir()` and `help()` commands
```
>>> z = 'baseball'
>>> dir(z)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
'__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__',
'__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
'__subclasshook__', '_formatter_field_name_split', '_formatter_parser',
'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs',
'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace',
'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace',
'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> len
<built-in function len>
>>> len(z)
8
>>> help(len)
Help on built-in function len in module __builtin__:

len(...)
    len(object) -> integer

    Return the number of items of a sequence or collection.
(END)
```
However when in doubt if you can't find access to a particular method use google to find what you're looking for.

## Accessing String Characters & Slicing
Strings are sequences of individual characters and can be accessed through the index notation

![String indices](https://i.stack.imgur.com/vIKaD.png)
```
>>> a = 'Monty Python'
>>> a
'Monty Python'
>>> a[0]
'M'
>>> a[-1]
'n'
>>> a[4]
'y'
>>>
```
String "slicing" is a pythonic syntax to refer to sub-parts of sequences. The general format is as follows:
```
a[start:end] # items start through end-1
a[start:]    # items start through the rest of the array
a[:end]      # items from the beginning through end-1
a[:]         # a copy of the whole array
```
And here it is in practice
```
>>> a = 'Monty Python'
>>> a[2:8]
'nty Py'
>>> a[1:]
'onty Python'
>>> a[:-1]
'Monty Pytho'
>>> a[:]
'Monty Python'
>>>
```

## String formatting
String formatting is the concept of concating different variables and data types to form a string. Format strings contain “replacement fields” surrounded by curly braces `{}`
```
>>> s = "Here {}, I have {} beers for you.".format("dana", 6)
>>> s
'Here dana, I have 6 beers for you.'
>>>
```
However the more pythonic way of string formatting would be using named placeholders
```
>>> address = '123 Main Street'
>>> city = 'San Francisco'
>>> s = 'I live on {address} in {city}'.format(address=address, city=city)
>>> s
'I live on 123 Main Street in San Francisco'
>>>
```
Here would be an example of how to format a float to 4 decimal places
```
>>> pi = 3.14159265359
>>> a = "Hooray for {pi:.4f}".format(pi=pi)
>>> a
'Hooray for 3.1416'
>>>
```
## Lists
Lists in python are a type of "iterable" meaning it is a data structure that contains a stream of values. They can contain any sequence of data types but generally you would see the same data types.

Unlike the previous primitive data types that we explored, lists are "mutable" (i.e. they can be altered)

Here are a few ways to create lists
```
>>> list1 = []
>>> list2 = [42, 7, 3]
>>> list3 = ['infoscout', 'isc', True]
>>> list1
[]
>>> list2
[42, 7, 3]
>>> list3
['infoscout', 'isc', True]
>>>
```

## List Methods
Similar to string methods, there are a number of different methods you can call on an instance of a list

```
>>> list = [20, 5, 9]
>>> list
[20, 5, 9]
>>> list.append(50)
>>> list
[20, 5, 9, 50]
>>> a = list.pop()
>>> a
50
>>> list
[20, 5, 9]
>>>
>>> list1 = [4,5,6]
>>> list2 = [10, 20, 30]
>>> list1 + list2
[4, 5, 6, 10, 20, 30]
>>>
```

## Iterating through Iterables
How do we look at each element in the list sequentially?

Iterating through iterables is a very common pattern in software development and we use the `FOR` and `IN`
clauses to look at each element in any type of iterable.

The general syntax is `for var in list`. Here are a few examples:

```
>>> numbers = [9, 235, 6, 0, 4]
>>> for number in numbers:
...  print number
...
9
235
6
0
4
>>>
>>> name = 'InfoScout'
>>> for c in name:
...  print c
...
I
n
f
o
S
c
o
u
t
>>>
>>> total = 0
>>> nums = [10, 20, 30]
>>> for num in nums:
...  total += num
...
>>> print total
60
>>>
```

## Sorting Iterables
The easy way to sort a list is using the `sorted` construct.

```
>>> l = [12, 2, 99, 4, 8, 14]
>>> sorted(l)
[2, 4, 8, 12, 14, 99]
>>>
```

The sorted function also takes a handy optional parameter, `reverse`, that will sort an iterable in reverse
```
>>> l = ['l', 'p', 'a', 'c', 'g', 'b', 'm']
>>> sorted(l, reverse=True)
['p', 'm', 'l', 'g', 'c', 'b', 'a']
>>>
```

However what if you would like to perform a more complex sort?

Sorting takes an optional `key=` parameter that allows one to define custom sorting. The key function takes in 1 value
and returns 1 value, and the returned "proxy" value is used for the comparisons within the sort.

An example
```
>>> # sort by element length
>>> l = ['san francisco', 'boston', 'chicago', 'new york city']
>>> sorted(l, key=len)
['boston', 'chicago', 'san francisco', 'new york city']
>>>
```
It is important to note that the `key=` parameter can take any function as long as that function returns 1 value

So how would we sort a list of strings by their last character in ascending order?
```
>>> l = ['jsnl', 'ahxb', 'nla', 'uownk']
>>> def last_char(s):
...  return s[-1]
...
>>> sorted(l, key=last_char)
['nla', 'ahxb', 'uownk', 'jsnl']
>>>
```

## Dictionaries
Dictionaries are a very common and powerful data structure in software. They are a key/value hash table
that allows for extremely fast lookup and insertion.

The contents of a dictionary can be written as key:value pairs with braces `{}` and brackets `[]`.

Strings, numbers, and tuples can be used for keys. Values accept any data type.

Here are a few examples for creating a dictionary:

```
>>> d = {}
>>> print d
{}
>>> d['fname'] = 'Dana'
>>> d['lname'] = 'Ford'
>>> print d
{'lname': 'Ford', 'fname': 'Dana'}
>>>
>>> z = {1: ['hello', 'word'], 9: ['abc']}
>>> print z
{1: ['hello', 'word'], 9: ['abc']}
>>>
```
To look up or set a value use brackets. Note that if the key you are looking for does not exist
then a `KeyError` exception will get raised
```
>>> d
{'lname': 'Ford', 'fname': 'Dana'}
>>> d['lname']
'Ford'
>>>
>>> d['city']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'city'
>>> d['city'] = 'San Francisco'
>>> d
{'lname': 'Ford', 'city': 'San Francisco', 'fname': 'Dana'}
```
Dictionaries are like lists in that they are both iterables however dictionaries do not store items
in order. Key/Value access is non-deterministic.

But like lists you can iterate through them. Since dictionaries have key and values you can iterate
though the keys, values, or both (items).

```
>>> d
{'lname': 'Ford', 'city': 'San Francisco', 'fname': 'Dana'}
>>> for key in d.keys():
...  print key
...
lname
city
fname
>>> for value in d.values():
...  print value
...
Ford
San Francisco
Dana
>>> for key, value in d.items():
...  print "Key: {key}. Value: {value}".format(key=key, value=value)
...
Key: lname. Value: Ford
Key: city. Value: San Francisco
Key: fname. Value: Dana
>>>
```

## Sets
A set is a data structure that holds an unordered collection of objects with no duplicates. A basic use case of
when to use a set would be removing duplicates in a list.

The syntax for sets use parenthesis `()`

```
>>> s1 = set()
>>> s1
set([])
>>>
>>> s2 = set([1,2,3])
>>> s2
set([1, 2, 3])
>>>
>>> s3 = set([1,2,3,4,4,4,4])
>>> s3
set([1, 2, 3, 4])
>>>
```

## Tuples
Tuples are another data structure (iterable) that holds a stream of values.

A tuple uses the parenthesis `()` seperated by commas
```
>>> t = (1,2,3)
>>> t
(1, 2, 3)
>>> type(t)
<type 'tuple'>
>>> t[0]
1
>>>
>>> len(t)
3
```
Though tuples may seem similar to lists, they are often used in different situations and for different purposes.
Tuples are immutable and usually contain a sequence of values that are different from each other.
```
>>> t = (10, 20, 30)
>>> t[0]
10
>>> t[0] = 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
```

## The Python Standard Library
[The Python Standard Library](https://docs.python.org/2/library/) is an extensive library that is distributed with every version of python. It offers a wide
range of utilities, components, and frameworks. It also contains several modules that provide standardized solutions
for many problems that occur in everyday programming.

Here are some of the most common libraries that are available:
```
>>> import datetime
>>> import re
>>> import math
>>> import os
>>> import sys
```

## PyPI - The Python Package Index
[The Python Package Index (PyPI)](https://pypi.python.org/pypi) is the official third party software repository for Python.
It currently has over 100,000 projects is the central location for getting any library.

Here are some of the most common libraries that are available:
```
>>> import requests
>>> import boto
>>> import django
>>> import mock

## The csv module
The `csv` module implements classes to read and write tabular data in CSV format. The csv module’s
`reader` and `writer` objects read and write sequences.


