#import pytest

###test catalog:
cat = 'test_error_bars.txt'

####import catscii
import catscii

CAT = catscii.load_cat(cat, True)
print(CAT.Ncolumn)
print(CAT.header)
print(CAT.cat)




