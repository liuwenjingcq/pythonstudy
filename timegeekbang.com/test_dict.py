# dict1 = {}
# print(type(dict1))
# dict2 = {'x': 1,'y': 2}
# dict2['z'] = 3
# print(dict2)

#dic练习

# name =['marry', 'bob', 'tracy']
# score = [95, 78, 85]
#
# d = {'marry': 95, 'bob': 78, 'tracy': 85}
# d['admin'] = 97
# d['admin'] = 79
# print(d['admin'])
# #print(d['admini'])
# print(d.get('admini'))

# n1 = 255
# print(hex(n1))

# def my_abs(x):
#     if x >0:
#         return x
#     else:
#         return -x
#
# print(my_abs(99))
# print(my_abs(-88))
# import  math
# def quadratic(a,b,c):
#     x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
#     x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
#     return x1, x2
# print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
# print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
#
# if quadratic(2, 3, 1) != (-0.5, -1.0):
#     print('测试失败')
# elif quadratic(1, 3, -4) != (1.0, -4.0):
#     print('测试失败')
# else:
#     print('测试成功')


# def product(x, y):
#     return  x * y
#
#
# print('product(5) =', product(5))
# print('product(5, 6) =', product(5, 6))
# print('product(5, 6, 7) =', product(5, 6, 7))
# print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# if product(5) != 5:
#     print('测试失败!')
# elif product(5, 6) != 30:
#     print('测试失败!')
# elif product(5, 6, 7) != 210:
#     print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         product()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')


def power1(x):
    return  x * x

def power2(x , n):
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s

# print( power2(5,1))
# print( power2(5,2))
# print( power2(5,0))
# print( power2(5,-1))

# def power3(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
#
# print( power3(5,2))
# print( power3(5))

# def add_end(L=[]):
#     L.append('end')
#     return L
#
# print(add_end([1,2,3]))
# print(add_end([]))
# print(add_end([]))

# def calc(number):
#     sum = 0
#     for n in number:
#         sum = sum + n * n
#     return  sum
#
# print(calc([1,2,3]))
# print(calc((1,2,3,7)))
# #可变参数
# def calc1(*number):
#     sum = 0
#     for n in number:
#         sum = sum + n * n
#     return  sum
# print(calc1(1,2,3))
# print(calc1(1,2,3,7))
# nums= [1,2,3]
# print(calc1(nums[0],nums[1],nums[2]))
#
# nums= [1,2,3]
# print(calc1(*nums))

#关键字参数
def person(name,age,**kw):
    print('name:',name ,'age:' ,age, 'other:',kw)
person('miche',30)
person('miche',30 , city= 'bejing')
person('miche',30,gender='m',city ='bejing')
