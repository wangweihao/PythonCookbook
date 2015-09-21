__author__ = 'wwh'

line = '  hello world , good moring '
print(line.strip(' '))

lines = [
    ' hehe ',
    'ha haha ',
    'xi   xi ',
    ' heihei'
]

t = (i.strip() for i in lines)
for s in t:
    print(s)