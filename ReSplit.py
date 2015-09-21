__author__ = 'wwh'

import re

line = 'asdf fasd; asdqw,  asdqw, awsdasd    foo'
NewLine = re.split(r'[;,\s]\s*', line)
print(NewLine)