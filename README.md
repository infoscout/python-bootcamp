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

## Sorting Iterables
Fill in