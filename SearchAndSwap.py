__author__ = 'wwh'

import re
line = 'Today is 11/27/2012, PyCin starts 3/13/2013'
ret = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', line)
print(ret)