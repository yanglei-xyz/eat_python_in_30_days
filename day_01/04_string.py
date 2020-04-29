# 可以用单引号，也可以用双引号
print('abc')
print("xyz")
# 还可以这样
print("I'm Yang Lei!")
print('单引号里面写着"双引号')
# 复杂的可以转义
print('I\'m \"OK\"!')
# 转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
print('I\'m learning\nPython.')
print('\\\n\\')

# 如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义
print(r'\\\t\\')

# 如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
print('''line1
line2
line3''')

# 多行字符串'''...'''还可以在前面加上r使用
print(r'''hello,\n
world''')
