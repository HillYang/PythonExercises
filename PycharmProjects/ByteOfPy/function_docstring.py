def print_max(x, y):
    """ Print the maximum of two numbers. 打印两个数值中的最大数

    the two values must be integer. 这两个数都应该是整数 """

    # 如果可能，将其转换至整数类型
    x = int(x)
    y = int(y)
    if x > y:
        print(x, ' is the maximum')
    elif x < y:
        print(y, ' is the maximum')
    else:
        print('The two numbers are equal')


print_max(3, 5)
print(print_max.__doc__)
help(print_max)
__version__ = '123'
a = 5
print(dir())
del a
print(dir())

print(__file__)
