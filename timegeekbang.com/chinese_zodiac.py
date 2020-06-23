# # 生肖
# chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
# for i in range(1, 13):
#     print(i)
# for year in range(2013, 2020):
#     print('%s 年的生肖是 %s'%(year, chinese_zodiac[year % 12]))
import   time
num = 5
while True:
    num = num + 1
    if num == 10:
        continue
    print(num)
    time.sleep(1)