'''
This is the main file of catscii
It imports all the submodule that are used

Author: R. THOMAS
Place: ESO
Year: GPL v3.0
'''
##python imports
import numpy

def excolumn(cat, column):
    '''
    This function extracts from the catalog the column
    given in parameter

    Parameters
    ----------
    cat : obj, 
          catalog object created by catscii.load_cat

    column : str
             name of the column to extract

    Returns
    -------

    extracted_column : numpy array
                       1D numpy array of the column that was extracted
    '''
    
    if column not in cat.header:
        raise ValueError('%s not in catalog header'%column)

    else:
        ##find the index of the column in the catalog
        index = numpy.where(numpy.array(cat.header) == column)
        
        ##and extract it
        extracted_column = cat.cat[index][0]

    return extracted_column
    

     
def exline(cat, column, line):
    '''
    This function extracts from the catalog the line
    given in parameter

    Parameters
    ----------
    cat : obj, 
          catalog object created by catscii.load_cat

    column: str
            Column where to look at for line identification

    line : str
           in the column given we will extract the line where the value is line


    Returns
    -------
    Line : list of dictionnary
           each dictionnary correspond to a line where the column given by the user is equal
           to the line value that was passed
           The keywords of the dictionnary are the name of the column and the values are the
           value at line = line
    '''
    
    if column not in cat.header:
        raise ValueError('%s not in catalog header'%column)

    else:
        pass


    ###extract the columm
    col = excolumn(cat, column) 

    ###and look for the line where column = line
    index = numpy.where(col == line)
    
    
    Line = []
    ##and extract line
    for i in cat.cat.T[index]: 
        indiv_line = {}
        for j in range(len(cat.header)):
            indiv_line[cat.header[j]] = i[j] 
        Line.append(indiv_line) 

    if len(Line) < 1:
        Line = Line[0]

    return Line

