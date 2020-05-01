# 定义一个函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-99))


# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return。

# pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def nop():
    pass


age = 10
if age >= 18:
    pass


# 对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand ty/pe')
    if x >= 0:
        return x
    else:
        return -x


# 返回多个值
import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
# 但其实这只是一种假象，Python函数返回的仍然是单一值：
r = move(100, 100, 60, math.pi / 6)
print(r)  # (151.96152422706632, 70.0)
# 返回值是一个tuple。在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

