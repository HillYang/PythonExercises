x = 60
y = 99


def print_max(a, b):
    if a > b:
        print(a, ' is the max')
    elif a < b:
        print(b, ' is the max')
    else:
        print(a, ' is equal to ', b)


# 2 blank line after function definition.


print_max(3, 8)
print_max(x, y)
print_max(18, 18)

print('------------ function_global -----------------\n')


def func():
    global x, y
    print('x is ', x)
    x = 100
    print('changed global x value to ', x)
    print_max(x, y)


func()
print('x is', x, ' now')
print('------------ function_default -----------------\n')


def say_messages(message, times=1):  # 在函数的参数列表中拥有默认参数值的参数不能位于没有默认参数值的参数之前。
    print(message * times)  # 末尾的参数才能被赋予默认参数值


say_messages('hello ')
say_messages(12)
say_messages('hello ', 12)
say_messages(12, 12)
say_messages('12', 12)
print('------------ function_keyword -----------------\n')


def func_word(a, b=5, c=10):
    print('a is ', a, ' b is ', b, ' c is ', c)


func_word(1, 2)
func_word(1, 2, 3)
func_word(25, c=88)
func_word(c=88, a=111)
print('------------ function_varargs -----------------\n')


def total(a=5, *numbers, **phonebook):  # 有时你可能想定义的函数里面能够有任意数量的变量，也就是参数数量是可变
    print('a is ', a)
    # 遍历元组中的所有项目
    for single_item in numbers:
        print('single_item is ', single_item)
    # 遍历字典中的所有项目
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)

# 当我们声明一个诸如 *param 的星号参数时，从此处开始直到结束的所有位置参数
# （Positional Arguments）都将被收集并汇集成一个称为“param”的元组（Tuple）。


total(10, 1, 2, 3, jack=1123, John=2231, Inge=1560)
print('------- add another print\n')
# 类似地，当我们声明一个诸如 **param 的双星号参数时，从此处开始直至结束的所有关键字
# 参数都将被收集并汇集成一个名为 param 的字典（Dictionary）。
print(total(10, 1, 2, 3, jack=1123, John=2231, Inge=1560))
