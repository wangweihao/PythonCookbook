__author__ = 'wwh'

from collections import Counter

words = [
    'look', 'into', 'he', 'she', 'is', 'my',
    'you', 'into', 'hi', 'into', 'is', 'look',
    'eyes', 'the', 'a'
]

#计数
word_count = Counter(words)
print(word_count)
#运算
word_count += word_count
print(word_count)
#获得出现次数最多的前3个值
top_three = word_count.most_common(3)
print(top_three)
