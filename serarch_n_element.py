__author__ = 'wwh'

import heapq

nums = [1,2,3,77,23,-12,0,100]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))
#print(dir(heapq))