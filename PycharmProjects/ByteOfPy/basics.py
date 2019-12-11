print("hello world")  # Note that print is a function

age = 20
name = "Swaroop"

print('{0} was {1} years old when he wrote this book'.format(name, age))
print(name + ' is ' + str(age) + ' years old')

# format 方法所做的事情便是将每个参数值替换至格式所在的位

# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0 / 3))
print(f'{1.0/3:.3f}')

# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format('hello'))

# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A byte of python'))

# 通过 end 指定其应以空白结尾
print('a', end='')
print('b', end='')
print('a', end='  ')
print('b', end='  ')
print('c')

# 转义序列
print('This is the first sentence. \
This is the second sentence.')

print('This is the first line.\nThis is the second line.')

print("What's your name?")
print('What\'s your name?')

# 如果你需要指定一些未经过特殊处理的字符串，比如转义序列，那么你需要在字符串前增加
# r 或 R 来指定一个 原始（Raw） 字符
print(r'Newlines are indicated by \n')
print('Newlines are indicated by \\n')

# 文件名 var.py
print('\n--使用变量与字面常量--')
i = 5
print(i)
i = i + 1
print(i)

s = '''This is a multi-line string.
this is the second line.'''
print(s)

