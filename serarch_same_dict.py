__author__ = 'wwh'


a = {
    'x':1,
    'y':2,
    'z':3
}

b = {
    'w':10,
    'x':11,
    'y':2
}
#寻找key值相同的
print(a.keys() & b.keys())
#寻找key-value相同的
print(a.items() & b.items())
#字典推导式(python2.7引入)，'-'是去除某item
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)