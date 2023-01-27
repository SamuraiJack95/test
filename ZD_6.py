# надеюсь такой вариант решения задания сойдет через множества?
# просто оно выглядет куда проще чем через куча циклов и сравнений списков

import random

size_list = 10
lis = []
lis2 = []

i = 0

for i in range(size_list):
    lis.append(random.randint(-10, 10))
for i in range(size_list):
    lis2.append(random.randint(-10, 10))

print(lis)
print(lis2)

# zd1

lis3 = lis + lis2

print(lis3)
print('\n')

# zd2

lis_s = set(lis)
lis_s1 = set(lis2)

lis_s2 = lis_s.union(lis_s1)
lis2_2 = list(lis_s2)

print(lis_s2)
print(lis2_2)
print('\n')

# zd3

lis3_3 = []
lis_s2_3 = set(lis2)

for i in range(size_list):
    if lis[i] in lis_s2_3:
        lis3_3.append(lis[i])

print(lis)
print(lis2)
print(lis3_3)
print('\n')

# zd4

lis_4 = set(lis)
lis2_4 = set(lis2)
lis_4_4 = list(lis_4)
lis2_4_4 = list(lis2_4)
lis3_4 = lis_4_4 + lis2_4_4

print(lis_4_4)
print(lis2_4_4)
print(lis3_4)
print('\n')

# zd5

max1 = max(lis)
min1 = min(lis)

max2 = max(lis2)
min2 = min(lis2)

lis3_5 = []

lis3_5.append(max1)
lis3_5.append(min1)
lis3_5.append(max2)
lis3_5.append(min2)

print(lis3_5)
