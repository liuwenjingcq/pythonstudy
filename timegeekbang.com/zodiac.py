#星座
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座',
               u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
zodic_days =((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23),
(8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
int_month = int(input ("请输入月份："))
int_day = int(input("请输入日期： "))

# for zd_num in range(len(zodic_days)):
#     if zodic_days[zd_num] >= (int_month, int_day):
#         print(zodiac_name[zd_num])
#         break
#     elif int_month == 12 and int_day> 23:
#         print(zodiac_name[0])
#         break
# n = 0
# while zodic_days[n] < (int_month, int_day):
#     if int_month == 12 and int_day > 23:
#         break
#     #n= n+1
#     n += 1
# print(zodiac_name[n])

cz_num = {}
for i in zodiac_name:
    cz_num[i]=0
print(cz_num)

