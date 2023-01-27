# zd_1

# def gcd(a, b):
#     if (b == 0):
#         return a
#     else:
#         return gcd(b, a % b)
#
# print('введите первое число')
# a = int(input())
#
# print('Введите второе число')
# b = int(input())
#
# GCD = gcd(a, b)
# print("НОД: ")
# print(GCD)

# zd_2

# Генерируем число

import random
n = 0
z = '0123456789'
x = random.choice(z[1:10])
for i in range(3):
    x += random.choice(z)
print(x)

# Задача решена через цикл

# n = 0

# while True:
#     y = input("Введите четырёхзначное число: ")
#     n += 1
#     b = 0; c = 0
#     for i in range(4):
#         if x[i] == y[i]:
#             b += 1
#         elif y[i] in x:
#             c += 1
#     print(y + ' содержит ' + str(b) + ' быка и ' + str(c) + ' коровы')
#     if b == 4:
#         print('Вы победили за', n, 'ходов')
#         break

# Задача решена через рекурсию

def game(x,n):
    b = 0
    c = 0
    y = input("Введите четырёхзначное число: ")
    for i in range(4):
        if x[i] == y[i]:
            b += 1
        elif y[i] in x:
            c += 1
    print(y + ' содержит ' + str(b) + ' быка и ' + str(c) + ' коровы')
    if b == 4:
        return n + 1
    else:
        n += 1
        return game(x,n)

s = game(x,n)

print('Вы победили за', s, 'ходов')