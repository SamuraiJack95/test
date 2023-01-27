# zd1

# def task1():
#     return print(f"“Don't compare yourself with anyone in this world…\nif you do so, you are insulting yourself.”\n\t\t\t\t\t\t\t\t\tBill Gates")
#
# task1()

# zd2

# def dip_add(a, b):
#     for i in range(a, b):
#         if i % 2 != 0:
#             print(i)
# print ('введите два числа')
#
# numb1 = int(input())
# numb2 = int(input())
#
# dip_add(numb1, numb2)

# zd3

# def draw_square(sym, n, check=True):
#     line = n * sym
#     if check:
#         for i in range(n):
#             print(line)
#     else:
#         print(line)
#         for i in range(n - 2):
#             print(sym + " " * (n - 2) + sym)
#         print(line)
#
# draw_square("*", 10, True)

# zd4
#
# num1 = 3
# num2 = 5
# num3 = 6
# num4 = -56
# num5 = 56
#
# def comparison(a, b, c, d, f):
#     mas = [a, b, c, d, f]
#     return min(mas)
# mem = comparison(num1, num2, num3, num4, num5)
# print(mem)

# zd5
#
# print('Введите два числа для диапозона')
# num1 = int(input())
# num2 = int(input())
#
# def multiplication(a, b):
#
#     if a < b:
#         um = a
#         for i in range(a + 1, b + 1):
#             um = um * i
#     elif a > b:
#         um = b
#         for i in range(b + 1, a + 1):
#             um = um * i
#     return um
#
# mul = multiplication(num1, num2)
# print(mul)

# zd6
#
# print('Введите число')
# num1 = int(input())
#
# def count_number(num):
#     count = 0
#     while (num != 0):
#         count +=  1
#         num = num // 10
#
#     return count
#
# print(count_number(num1))

# zd7
#
# print('Введите число')
# num1 = int(input())
#
# def polim(num):
#     srav = num
#     perem = 0
#     while num != 0:
#         dil = num % 10
#         perem = perem * 10 + dil
#         num = num // 10
#     if srav == perem:
#         return True
#     else:
#         return False
#
# a = polim(num1)
# print(a)