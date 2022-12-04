# переменной присвоили функцию
# def f(x):
#     x**2

# g  = f
# print(type(f(1)))
# print(type(g(1)))

# Функция в агрументе другой функции
# def f(x):
#     return x**2
# g = f

# print(type(f))
# print(type(g))
# print(f(4))
# print(g(4))  # работает также как функция

# def calc1(x):
#    return x+10

# print(calc1(10))

# def calc2(x):
#     return x*10

# print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2, 10)
# math(calc1, 10)

# def sum(x, y):
#     return x+y

#sum = lambda x, y: x+y +1 # тоже что и выше

# def mylt(x, y):
#     return x*y

# def calc(op, a, b):
#     print(op(a, b))

# calc(lambda x, y: x+y, 4, 5) 



# List Comprehension

# list= []

# for i in range(1, 101):
#     if(i%2 == 0):
#         list.append(i)

# print(list)

# list = [i for i in range(1, 101)]
# print(list)

# list1 = [i for i in range(1, 21) if i%2 == 0]
# print(list1)

# list2 = [(i, i) for i in range(1, 21) if i%2 == 0]
# print(list2)

# def f(x):
#     return x**3

# list3 = [f(i) for i in range(1, 21) if i%2 == 0]
# print(list3)

# list4 = [(i, f(i)) for i in range(1, 21) if i%2 == 0]
# print(list4)

# Задачка. выбрать четные и составить кортеж с числом и его квадратом
# def f(x):
#     return x**2
# list1 = [1, 2, 3, 5, 8, 15, 23, 38]
# list2 = [(i, f(i)) for i in list1 if i%2 == 0]
# print(list2)

# path = 'c:\Users\HP\Desktop\Учеба на прграмиста\Python\Lesson\file.txt'
# f = open(path, 'r')
# data = f.read() + ''
# f.close()

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]

# out = []
# for e in numbers:
#     if not e%2:
#         out.append((e, e ** 2))
# print(out)


# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int, data)
# res = where(lambda x: not x%2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)

# MAP
# li = [x for x in range(1, 20)]

# li = list(map(lambda x:x+10, li))

# print(li)


# data = list(map(int, input().split()))
# data = list(map(int, '1 2 3'.split()))

# for e in data:
#     print(e)
# print('---')
# for e in data:
#     print (e)

# FILTER
# data = [x for x in range(10)]

# res = list(filter(lambda x: x%2==0, data))
# print(res)

# ZIP 
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

data = list(zip(users, ids, salary))
print(data)

data2 = list(enumerate(users))
print(data2)

