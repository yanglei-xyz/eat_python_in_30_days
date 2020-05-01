# 生成器:
# 列表元素可以按照某种算法推算出来，那我们可以在循环的过程中不断推算出后续的元素

# 第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
L = [x * x for x in range(10)]
g = (x * x for x in range(10))
# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
for n in g:
    print(n)


# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
        a, b = b, a + b  # 相当于：t = (b, a + b);   a = t[0];   b = t[1]
        n = n + 1
    return 'done'


f = fib(60)
for a in f:
    print(a)


g = fib(10)
# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


# 杨辉三角
def triangles():
    arr = [1]
    yield arr
    while True:
        arr = [1]+[arr[x]+arr[x+1] for x in range(len(arr)-1)]+[1]
        yield arr


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 100:
        break


