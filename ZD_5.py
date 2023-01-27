# import random

# ZD_1

# print('Введите выражение для подсчета используя мат знаки (+,-,*,/)')
#
# vir = input()
#
# if '+' in vir:
#     numb1, numb2 = vir.split('+')
#     print(round(float(numb1) + float(numb2), 3))
# elif '-' in vir:
#     numb1, numb2 = vir.split('-')
#     print(round(float(numb1) - float(numb2), 3))
# elif '*' in vir:
#     numb1, numb2 = vir.split('*')
#     print(round(float(numb1) * float(numb2), 3))
# elif '/' in vir:
#     numb1, numb2 = vir.split('/')
#     print((round(float(numb1) / float(numb2), 3)))

# ZD_2

# print('Введите размер списка')
# raz = int(input())
# lis = []
# i = 0
#
# count_minus = 0
# count_plus = 0
# count_zero = 0
#
# for i in range(raz):
#     lis.append(round(random.uniform(-100, 100), 2))
#
# max = max(lis)
# min = min(lis)
#
# # max = lis[0]
# # min = lis[0]
# # i = 0
#
# # for i in range(raz):
# #     if lis[i] > max:
# #         max = lis[i]
# #
# # for i in range(raz):
# #     if lis[i] < min:
# #         min = lis[i]
#
# for i in range(raz):
#     if lis[i] > 0:
#         count_plus += 1
#
# for i in range(raz):
#     if lis[i] < 0:
#         count_minus += 1
#
# for i in range(raz):
#     if lis[i] == 0:
#         count_zero += 1
#
# print(lis)
# print(max, '\n', min, '\n', count_plus, '\n', count_minus, '\n', count_zero)

