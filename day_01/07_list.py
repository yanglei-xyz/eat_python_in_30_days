# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))

# 用索引来访问list中每一个位置的元素
print(classmates[0])
print(classmates[2])

# 还可以用-1做索引，直接获取最后一个元素：
print(classmates[-1])  # 'Tracy'
print(classmates[-2])  # 'Bob'

# 添加数据
classmates.append('Adam')
print(classmates)

# 也可以把元素插入到指定的位置，比如索引号为1的位置：
classmates.insert(1, 'Jack')
print(classmates)

# 要删除list末尾的元素，用pop()方法：
print(classmates.pop())
print(classmates)

# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(1)
print(classmates)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[1] = 'Sarah'
print(classmates)

# list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]

# list元素也可以是另一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']

# 如果一个list中一个元素也没有，就是一个空的list，它的长度为0
L = []

