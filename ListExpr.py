__author__ = 'wwh'

fruit = {
    'apple':10,
    'banana':20,
    'orange':5,
    'pineapple':15
}

print({key:value for key, value in fruit.items() if 10 <= value <= 20})
