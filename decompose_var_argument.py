__author__ = 'wwh'

records = [
    ('foo', 1,2),
    ('bar', 'hello'),
    ('foo', 2,3)
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
        print(args)
        print(*args)
    elif tag == 'bar':
        do_bar(*args)
        print(args)
        print(*args)

    s = [1,2,3]
    print(s)
    print(*s)
    print(type(s))

    tup = (1,2,3)
    s,*t = tup
    print(s)
    print(t)
    print(*t)
