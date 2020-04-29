# dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])
d['Adam'] = 67
print(d)

# 判断某个元素是否存在
print('Thomas' in d)  # false

# 通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('Thomas'))  # None
print(d.get('Thomas', -1))  # -1

# 删除一个key，用pop(key)方法
print(d.pop('Bob'))
print(d)
