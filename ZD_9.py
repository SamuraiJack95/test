import random


# ZD_2

# chek = 0

# list_eval = [random.randint(1,12) for i in range(11)]
# print(list_eval)
#
# while chek != 5:
#     print('Выбирите что хотите сделать: \n 1. Покажи оценки \n 2. Пересдача экзамена'
#       '\n 3. Проверка стипендии \n 4. Отсортировать список 1.(да, по возрст) 2.(нет, по убыванию) \n 5. Выход')
#
#     chek = int(input())
#
#     if chek == 1:
#         print(list_eval)
#
#     elif chek == 2:
#         print('Выбирите какой экзамен пересдать(0-9) и поставьте оценку')
#         print(list_eval)
#         chek2 = int(input())
#         eval = int(input())
#
#         list_eval[chek2] = eval
#         print(list_eval)
#
#     elif chek == 3:
#
#         medium_eval = sum(list_eval) / 10
#         print(medium_eval)
#
#         if medium_eval >= 10.7:
#             print('Степендия есть')
#         else:
#             print('Степендии нет')
#
#     elif chek == 4:
#         chekk = int(input())
#         if chekk == 1:
#             for i in range(11):
#                 key = list_eval[i]
#                 j = i
#                 while j >= 1 and list_eval[j - 1] > key:
#                     list_eval[j] = list_eval[j - 1]
#                     j -= 1
#                 list_eval[j] = key
#
#         if chekk == 2:
#             for i in range(11):
#                 key = list_eval[i]
#                 j = i
#                 while j >= 1 and list_eval[j - 1] < key:
#                     list_eval[j] = list_eval[j - 1]
#                     j -= 1
#                 list_eval[j] = key
#         print(list_eval)
#     elif chek == 5:
#         break

# ZD_1

# list_ev = []
# print('Введите длину массива')
# number_mas = int(input())
#
# list_eval = [random.randint(-100, 100) for i in range(number_mas)]
# onethree = int(round((number_mas * 1) / 3, 0))
# twothree = int(round((number_mas * 2) / 3, 0))
#
# sum_mas = sum(list_eval[:twothree])
#
# if sum_mas > 0:
#     for i in range(twothree):
#         key = list_eval[i]
#         j = i
#         while j >= 1 and list_eval[j - 1] > key:
#             list_eval[j] = list_eval[j - 1]
#             j -= 1
#         list_eval[j] = key
#
# else:
#     for i in range(onethree):
#         key = list_eval[i]
#         j = i
#         while j >= 1 and list_eval[j - 1] > key:
#             list_eval[j] = list_eval[j - 1]
#             j -= 1
#         list_eval[j] = key
#
#     print(list_eval)
#
#     list_ev = list(reversed(list_eval[onethree:]))
#     del list_eval[onethree:]
#
#     list_eval = list_eval + list_ev
#
# print(onethree)
# print(twothree)
# print(sum_mas)
# print(list_eval)

# ZD_3

print('Введите количество элементов')
elements = int(input())

numbers = [random.randint(-100, 100) for i in range(elements)]
swapped = True
while swapped:
    swapped = False
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            swapped = True

print(numbers)