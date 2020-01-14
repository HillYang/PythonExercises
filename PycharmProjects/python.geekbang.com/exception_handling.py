# i = j
# print())
# a = '123'
# print(a[3])

# d = {'a': 1, 'b': 2}
# print(d['c'])

# year = int(input('input year:'))

# try:
#     year = int(input('input year:'))
# except ValueError:
#     print('please input int！')

# a = 123
# a.append()

# try:
#     a = 123
#     a.append()
# except AttributeError:
#     print('没有属性')

# try:
#     raise NameError('helloError')
# except NameError:
#     print('my custom error')

try:
    a = open('name.txt')
except Exception as e:
    # print(e)
    print('hello error')
finally:
    a.close()

