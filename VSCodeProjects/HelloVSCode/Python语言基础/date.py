# 输入某年月日，判断这一天是这一年的第几天？
import datetime

# datestr = input('Enter the date like (20170210):')

# datestr = '20200727'

print(datetime.date.today())

# use date.today() get the current date
datestr = str(datetime.date.today())

dt = datetime.datetime.strptime(datestr, "%Y-%m-%d")
another_datestr = datestr[:4] + '0101'
another_dt = datetime.datetime.strptime(another_datestr, "%Y%m%d")
num = int((dt - another_dt).days) + 1


def year_days_num(year):

    #这一年第一天和这一年最后一天
    startDay = str(year)+'-01-01'
    endDay = str(year)+'-12-31'

    #天数
    year_days_mum = (datetime.datetime.strptime(endDay, "%Y-%m-%d") - datetime.datetime.strptime(startDay, "%Y-%m-%d")).days +1

    print('{}年一共{}天'.format(year,year_days_mum))
    return year_days_mum

year_days_num(datestr[:4])


print('今天是第%d天' % num)
print("%.0f%%" % (num/365*100))

print('今年已经过了%.2f%%' % (num/365*100))