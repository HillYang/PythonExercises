# 闭包的使用：实现数学方程
# a * x + b = y


def a_line(a, b):
    def arg_y(x):
        return a * x + b
    return arg_y


line1 = a_line(3, 5)    # a=3 b=5
line2 = a_line(5, 10)

print(line1(10))          # x=10 y=?
print(line1(20))


# 闭包内使用 lambdam 表达式

def a_line2(a, b):
    return lambda x: a*x+b

