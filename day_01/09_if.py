# if...elif...else...请注意有冒号
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

# if判断条件还可以简写，只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
x = "123"
if x:
    print('True')
