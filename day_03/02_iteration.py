# 迭代
# Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)


# 通过collections模块的Iterable类型判断一个对象是可迭代对象
from collections import Iterable
isinstance('abc', Iterable)
isinstance([1,2,3], Iterable)

# 下标循环
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。