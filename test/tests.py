#import pytest

###test catalog:
cat = 'test_error_bars.txt'

####import catscii
import catscii

CAT = catscii.load_cat(cat, True)

col = catscii.excolumn(CAT, 'X')
line = catscii.exline(CAT, 'X', '2')

print(line)



