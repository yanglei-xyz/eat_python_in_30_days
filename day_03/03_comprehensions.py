# 列表生成式
import os


list(range(1, 11))  # 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))

[x * x for x in range(1, 11)]  # 自然数的平方，[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

[x * x for x in range(1, 11) if x % 2 == 0]  # 仅偶数的平方,[4, 16, 36, 64, 100]

[m + n for m in 'ABC' for n in 'XYZ']  # 使用两层循环，可以生成全排列，['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

[d for d in os.listdir('.')]  # 列出当前目录下的所有文件和目录名

d = {'x': 'A', 'y': 'B', 'z': 'C'}
[k + '=' + v for k, v in d.items()]  # 可以使用两个变量来生成list
# ['y=B', 'x=A', 'z=C']

# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]  # ['hello', 'world', 'ibm', 'apple']


# 在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else。

