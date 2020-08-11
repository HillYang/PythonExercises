# 从1到10 所有偶数的平方

a_list = []
for i in range(1, 11):
    if i % 2 == 0:
        a_list.append(i * i)

print(a_list)

# 列表推导式 Python 特有
b_list = [i*i for i in range(1, 11) if i % 2 == 0]

print(b_list)

# 字典推导式 Python 特有
z_num = {}
for i in range(1, 11):
    z_num[i] = 0

print(z_num)

a_num = {i:0 for i in range(1, 11)}

print(a_num)
