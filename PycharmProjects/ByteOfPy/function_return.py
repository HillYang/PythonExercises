def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        print('The numbers are equal.')
    else:
        return y


x = input('please enter x = ')
y = input('please enter y = ')

print(maximum(x, y))
# 每一个函数都在其末尾隐含了一句 return None ，除非你写了你自己的 return 语句


def some_function():
    pass


print(some_function())
