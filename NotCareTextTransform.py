__author__ = 'wwh'

import re

line = 'PYTHON, python, PyThOn'
print(re.findall('python', line, re.IGNORECASE))

