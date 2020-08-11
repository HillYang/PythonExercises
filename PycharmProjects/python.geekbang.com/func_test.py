# 关键字参数，忽略参数顺序
# print('abc', end='\n')
# print('abc')


def func(a, b, c):
    print('a=%s' % a)
    print('b=%s' % b)
    print('c=%s' % c)


func(1, c=3, b=2)

# 取得参数个数

value = 123


# 变量作用域演示


def length(first, *other):
    global value
    value = 888
    print(1 + len(other))
    print('first = %s' % first)


length(123, 234, 456)
print(value)

list1 = [1, 2, 3]
it = iter(list1)
print(next(it))
print(next(it))
print(next(it))


# print(next(it)) #except


# 函数的迭代器与生成器
def frange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step


for i in frange(10, 20, 0.5):
    print(i)

# lambda 表达式

adict = {'a': 'AA', 'b': 'BB'}


def func2(item):
    return item[1]


for i in adict.items():
    print(func2(i))

for i in adict.items():
    g = lambda item: item[1]
    print(g(i))


# filter() map() reduce() zip() 类似于数学中的矩阵转换
# 以上函数多用于用于合并，累加

a = [1, 2, 3, 4, 5, 6]
b = [2, 3, 4]
print(list(filter(lambda x: x > 2, a)))

print(list(map(lambda x, y: x+y, a, b)))

from functools import reduce
print(reduce(lambda x, y: x+y, b, 1))

print(list(zip(a, b)))

dicta = {'a': 'aa', 'b': 'bb'}
dictb = dict(zip(dicta.values(), dicta.keys()))

print(dictb)

# 闭包：内部函数引用外部变量
# add 函数名称或函数的引用
# add() 函数的调用


def sum(a):
    def add(b):
        return a + b
    return add


num1 = sum(2)
num2 = num1(4)
print(num2)
print(type(num1))
print(type(num2))
