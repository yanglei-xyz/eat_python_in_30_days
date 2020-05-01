# 递归
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)


d = fact(100)
print(d)

# 尾递归,python并没有对尾递归做优化，所以依旧会堆栈溢出
def fact2(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


d = fact2(200)
print(d)

