# 详细介绍：https://www.liaoxuefeng.com/wiki/1016959663602400/1017075323632896

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord('A'))    # 65
print(ord('中'))   # 20013
print(chr(66))     # B
print(chr(25991))  # 文

# 如果知道字符的整数编码，还可以用十六进制这么写str：
print('\u4e2d\u6587')

# Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'ABC'
print(x)
# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
print('ABC'.encode('ascii'))    # b'ABC'
print('中文'.encode('utf-8'))    # b'\xe4\xb8\xad\xe6\x96\x87'

# 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
print(b'ABC'.decode('ascii'))   # ABC
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  # 中文

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')) # 中

# 要计算str包含多少个字符，可以用len()函数：
print(len('ABC'))  # 3
print(len('中文'))  # 2
# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：(1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节)
print(len(b'ABC'))  # 3
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))  # 6
print(len('中文'.encode('utf-8')))  # 6







