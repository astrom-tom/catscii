# catscii

**catscii** is a very simple python module that allows one to extract in a very easy way columns or line from ascii catalogs. 


Installation
============

catscii is currently placed in the pypi test repository.
To install it 

    pip install -i https://test.pypi.org/simple/ catscii

The only dependency is numpy.

How to
======

Once you installed it you can get started importing the module:

    from catscii import catscii 


**1-Catalogs with header**

Then you must load your ascii catalog. For the purpose of this short tutorial we take a very easy catalog called *test_catscii.txt*: 

    #A	 B	C	D 
    X	 11	12	13 
    Y	 15	15	15 
    Z	 17	15	12


To read the catalog you must create a catalog with the **load_cat** class:

    >>cat = catscii.load_cat('test_catscii.txt', 'yes') 

The first argument is the name of your catalog, and the second tells if there is a proper header. A proper header is when each columns has a name and starts with a '#' symbol (see the example above). The catalog as some interesting attributes, like header or the catalog itself.

    >>cat.header
      ['A', 'B', 'C', 'D']

    >>cat.cat
    array([['X', 'Y', 'Z'],
       ['11', '15', '17'],
       ['12', '15', '15'],
       ['13', '15', '12']], dtype='<U2')

By default, the catalog is extracted with a string format.


After you can extract columns calling the column name:

    >>cat.get_column('A') 
    array(['11', '15', '17'], dtype='<U2')

By default the column is extracted in string format. If you want another type you can precise it like this:

    >>cat.get_column('B', 'int')
    array([11, 15, 17])


To extract a line you have to give a given column and a given value in that column:

    >> cat.get_line('A', 'X')
    [{'A': 'X', 'B': '11', 'C': '12', 'D': '13'}]

It returns a list dictionnaries of key/value corresponding to column_name/value. In the case you have multiple line with the same value for a given column, the list will grow:

    >> cat.get_line('C', '15')
    [{'A': 'Y', 'B': '15', 'C': '15', 'D': '15'},
     {'A': 'Z', 'B': '17', 'C': '15', 'D': '12'}]  


Help
====

You can also display the help of the module like this:





Contribute
==========
If you want to contribute to catscii please drop me a mail [the.spartan.proj@gmail.com]



