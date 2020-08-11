# 闭包实现计数器功能
def counter(first=0):
    cnt = [first]

    def add_one():
        cnt[0] += 1
        return cnt[0]
    return add_one


num1 = counter(0)
print(num1)
print(num1())
print(num1())

num5 = counter(5)
print(num5())
print(num5())
