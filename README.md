# catscii

**catscii** is a very simple python module that allows one to extract in a very easy way data from ascii catalogs. 


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


Catalogs with header
^^^^^^^^^^^^^^^^^^^^

Then you must load your ascii catalog. For the purpose of this short tutorial we take a very easy catalog called *test_catscii.txt*: 

    #A	 B	C	D 
    X	 11	12	13 
    Y	 15	15	15 
    Z	 17	15	12


To read the catalog you must run the **load_cat** method:

    cat = catscii.load_cat('test_catscii.txt', 'yes') 

The first argument is the name of your catalog, and the second tells if there is a proper header


Help
====

You can also display the help of the module like this:





Contribute
==========
If you want to contribute to catscii please drop me a mail [the.spartan.proj@gmail.com]



