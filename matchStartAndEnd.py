__author__ = 'wwh'

filename = [
    '1.txt',
    '2.py',
    '3.py',
    '4.py',
    '5.c'
]

print([name for name in filename if name.endswith(('.c', '.py'))])