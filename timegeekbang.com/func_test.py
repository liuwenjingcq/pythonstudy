# print('abc',end='\n')
#
# def func(a,b,c):
#     print('a= %s' %a)
#     print('b= %s' %b)
#     print('c= %s' %c)
#
# func('a','b','c')
# func('aa',c='cc')

def howlong(first, *other):
    print(1+len(other))
howlong(123)
howlong(123,234,345)
howlong(123,234,345,'asd')
howlong()
