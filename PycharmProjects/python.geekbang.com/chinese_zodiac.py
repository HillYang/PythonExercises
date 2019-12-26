# 字符串的使用例子
# 记录生肖，根据年份来判断生肖
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

# print (chinese_zodiac[4])
# print (chinese_zodiac[0:4])
# print (chinese_zodiac[-1])

# year = 2020
year = int(input('请输入出生年份:'))

# print(year % 12)
print(chinese_zodiac[year % 12])

if(chinese_zodiac[year % 12]) == '鼠':
    print('鼠年运势。。。')

# print('狗' in chinese_zodiac)
# print('狗' not in chinese_zodiac)
#
# print(chinese_zodiac + ' abc ' + chinese_zodiac)
# print(chinese_zodiac * 3)

for cz in chinese_zodiac:
    print(cz)

for i in range(1, 13):
    print(i)

for year in range(2000, 2019):
    print('%s 年的生肖是 %s' % (year, chinese_zodiac[year % 12]))

num = 5
while True:
    num = num + 1
    if num == 10:
        continue
    print(num)
    if num > 10:
        break
