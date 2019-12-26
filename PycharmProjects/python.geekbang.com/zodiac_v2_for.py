# for 使用例子
# 根据输入 (month, day) 判断星座
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
               u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')

zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23),
               (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

# a = (1, 3, 5, 7, 9)
# b = 4
# list(filter(lambda x: x < b, a))
# print(list(filter(lambda x: x < b, a)))

# (month, day) = (10, 1)

for i in range(1, 5):
    print(i)

print(list(range(1, 5)))

int_month = int(input('''please 
enter 
month:'''))
int_day = int(input('please enter day:'))

for zd_num in range(len(zodiac_days)):
    if zodiac_days[zd_num] >= (int_month, int_day):
        print(zodiac_name[zd_num])
        break
    elif int_month == 12 and int_day > 23:
        print(zodiac_name[0])
        break

# zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
# # print(zodiac_day)
# zodiac_len = len(list(zodiac_day)) % 12
# print(zodiac_name[zodiac_len])
