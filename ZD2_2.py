# ZD1_2

# print('Введите число от 1 до 100')
# a = int(input())
# if a > 0 and a < 100:
#     if a % 3 == 0 and a % 5 != 0:
#         print('Fizz')
#     elif a % 5 == 0 and a % 3 != 0:
#         print('Buzz')
#     elif a % 3 == 0 and a % 5 == 0:
#         print('Fizz Buzz')
# else:
#     print('Число вне диапозона')

# ZD2_2

# mas = [1, 2, 3, 4, 5, 6, 7]
# print('Введите число')
# a = int(input())
# print('выбирете в какую степень от 1 до 7 вам возвести')
# b = int(input())
#
# if b == 1:
#     c = a ** mas[0]
#     print(c)
# elif b == 2:
#     c = a ** mas[1]
#     print(c)
# elif b == 3:
#     c = a ** mas[2]
#     print(c)
# elif b == 4:
#     c = a ** mas[3]
#     print(c)
# elif b == 5:
#     c = a ** mas[4]
#     print(c)
# elif b == 6:
#     c = a ** mas[5]
#     print(c)
# elif b == 7:
#     c = a ** mas[6]
#     print(c)

# ZD3_2

# print('введите стоимость разговора')
# speak = int(input())
#
# print("""Выбирете с какого на кого оператора вы звоните от 1 до 9
#       1 - MTS - MTS
#       2 - MTS - Beeline
#       3 - MTS - Megafone
#       4 - Beeline - MTS
#       5 - Beeline - Beeline
#       6 - Beeline - Megafone
#       7 - Megafone - MTS
#       8 - Megafone - Beeline
#       9 - Megafone - Megafone""")
#
# price_oper = int(input())
#
# if price_oper == 1:
#     sum = speak * 1
# elif price_oper == 2:
#     sum = speak * 1.15
# elif price_oper == 3:
#     sum = speak * 1.2
# elif price_oper == 4:
#     sum = speak * 1.25
# elif price_oper == 5:
#     sum = speak * 1.3
# elif price_oper == 6:
#     sum = speak * 1.5
# elif price_oper == 7:
#     sum = speak * 2
# elif price_oper == 8:
#     sum = speak * 3
# elif price_oper == 9:
#     sum = speak * 2.5
#
# print(sum)

# ZD4_2

# не пойму что не так, можете поправить и подсказать что не так !!!

# print('Введите уровень продаж для трех менеджеров')
# men_prod_a = int(input())
# men_prod_b = int(input())
# men_prod_c = int(input())
#
# if men_prod_a > 500:
#     men_a = 200 + men_prod_a * 0.03
# elif (men_prod_a > 500) and (men_prod_a < 1000):
#     men_a = 200 + men_prod_a * 0.05
# elif men_prod_a > 1000:
#     men_a = 200 + men_prod_a * 0.08
#
# if men_prod_b > 500:
#     men_b = 200 + men_prod_b * 0.03
# elif (men_prod_b > 500) and (men_prod_b < 1000):
#     men_b = 200 + men_prod_b * 0.05
# elif men_prod_b > 1000:
#     men_b = 200 + men_prod_b * 0.08
#
# if men_prod_c > 500:
#     men_c = 200 + men_prod_c * 0.03
# elif (men_prod_c > 500) and (men_prod_c < 1000):
#     men_c = 200 + men_prod_c * 0.05
# elif men_prod_c > 1000:
#     men_c = 200 + men_prod_c * 0.08
#
# if men_prod_a > men_prod_b and men_prod_a > men_prod_c:
#     res_a = men_a + 200
# elif men_prod_b > men_prod_a and men_prod_b > men_prod_c:
#     res_b = men_b + 200
# elif men_prod_c > men_prod_a and men_prod_c > men_prod_b:
#     res_c = men_c + 200
#
# print(res_a, res_b, res_c)
# # print(men_a, men_b, men_c)
