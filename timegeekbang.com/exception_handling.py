# i = j
#print())

# # a = '123'
# # print(a[3])
# d = {'a':1,'b':2}
# print(d['c'])

# year = int(input("input year :"))
# try:
#     year = int (input('input year:'))
# except ValueError:
#     print("年份要输入数字")

# a = 123
# try:
#     a.append()
# except AttributeError:
#     print("int 类型没有append ")
# except (ValueError,AttributeError,KeyError)

# try:
#     print(1/0)
# except Exception as e:
#     print('0 不能做除数 %s' %e)


# try:
#     raise NameError('hellError')
# except NameError:
#     print('my custom error')



try:
    a = open('name.txt')
except Exception as e:
    print(e)
finally:
    a.close()
