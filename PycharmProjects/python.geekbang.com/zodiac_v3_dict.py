# dict使用例子
# 根据输入 (month, day) 判断星座
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
               u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')

zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23),
               (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

cz_num = {}
for i in chinese_zodiac:
    cz_num[i] = 0

z_num = {}
for i in zodiac_name:
    z_num[i] = 0

while True:
    int_year = int(input('please enter year:'))
    int_month = int(input('please enter month:'))
    int_day = int(input('please enter day:'))

    n = 0
    while zodiac_days[n] < (int_month, int_day):
        if int_month == 12 and int_day > 23:
            break
        n += 1
    # 输出星座和生肖
    print(zodiac_name[n])

    print('%s 年的生肖是 %s' % (int_year, chinese_zodiac[int_year % 12]))
    print(cz_num)
    print(z_num)

    cz_num[chinese_zodiac[int_year % 12]] += 1
    z_num[zodiac_name[n]] += 1

    for each_key in cz_num:
        print('生肖 %s 有 %d 个' % (each_key, cz_num[each_key]))
    for each_key in z_num:
        print('星座 %s 有 %d 个' % (each_key, z_num[each_key]))

