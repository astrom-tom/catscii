'''
This file contains the code to 
open the catalogs passed by the user.

Each catalog that is open becomes a python 
object with attributes.

Author: R. THOMAS
Place: ESO
Year: GPL v3.0
'''

###python imports
import numpy

###local import
from . import errors

class load_cat(object):
    '''
    This class creates, from an ascii catalog,
    a python object
    '''

    def __init__(self, catalog, header):
        '''
        Class constructor

        Parameters
        ----------
        catalog : str
                  this is the catalog (eventually with its path) you want to open

        header  : Boolean
                  True if the catalog contains a header, otherwise false

        Attributes
        ----------
        name    : str
                  Name of the catalog, as passed by the user

        cat     : numpy array
                  numpy array loaded from the catalog (all columns are string by default)

        header  : list of string
                  identification of each column. If no header is present in the catalog
                  then each column are renames col1, col2, ....colN

        Note
        ----
        For the header of the catalog to be recognized, it must start by an hash (#)
        and provide a name for EVERY column Ex:
        #X     Y   Xerrp   Xerrm   Yerrp   Yerrm
        1       1   0.5     0.2     0.3     0.1
        2       2   0.3     0.2     0.1     0.4
        3      3   0.1     0.05    0.1     0.4
        4      4   0.1     0.07    0.8     0.2
        5      5   0.2     0.3     0.15    0.23
        6      6   0.1     0.4     0.6     0.1
        7      7   0.2     0.3     0.4     0.1
        '''
       
        ###the name of the catalog becomes an attribute
        self.name = catalog

        if header:
            self.get_header()
        else:
            self.fake_header()

    def fake_header(self):
        '''
        In case there is no header in the catalog we create a fake one
        Attributes
        ----------
        Ncolumn  : int
              number of column from the catalog

        header: list
                list of column names

        Nrows:  int
                number of rows
        '''

        ####extract number of column
        self.cat = numpy.genfromtxt(self.name, dtype='str').T
        self.Ncolumn = len(self.cat)  ###--> number of column
        self.Nrows = len(self.cat.T)

        ##create fake header
        self.header = []
        for i in range(self.Ncolumn):
            self.header.append('Col%s'%(i+1))

        
    def get_header(self):
        '''
        This method take the catalog
        and extract the header
        
        Attributes
        ----------
        Nc  : int
              number of column from the catalog

        header: list
                list of column names

        Nrows:  int
                number of rows
        '''
        ####extract number of column
        self.cat = numpy.genfromtxt(self.name, dtype='str').T
        self.Ncolumn = len(self.cat)  ###--> number of column
        self.Nrows = len(self.cat.T)
        

        ####read the first line of the raw file
        with open(self.name, 'r') as F:
            firstLine = F.readline()

        hashtag = firstLine[0]

        ###we check if the header start with the hash, if not we raise the error
        if hashtag != '#':
            raise errors.header_hash('No hash at the beginning of the header')
        else:
            firstLine = firstLine[1:-1] 

        ##split the header:
        N_header = len(firstLine.split())
            
        ###if the number of header detected is different from the number of column..error
        if N_header != self.Ncolumn:
            raise errors.header_length('The number of headers is different from the number of columns')
        else:
            self.header = firstLine.split()

