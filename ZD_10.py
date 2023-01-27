# ZD_1

# a = (1, 2, 3, 4, 4, 4, 5)
# b = (1, 2, 5, 6)
# c = (5, 5, 7, 2)
#
# um1 = set(a)
# um2 = set(b)
# um3 = set(c)
#
# g = um1.intersection(um1, um2,um3)
#
# print(g)

# ZD_2

# a = (1,2,3)
# b = (3,4,5)
# c = (3,2,5,7)
#
# um1 = set(a)
# um2 = set(b)
# um3 = set(c)
#
# g = um1.difference(um2,um3)
# h = um2.difference(um1,um3)
# j = um3.difference(um1,um2)
#
# l = g.union(h,j)
# print(g,h,j)
# print(l)

# ZD_3

a = (8, 7, 6, 5, 4)
b = (4, 7, 6, 5, 8)
c = (8, 7, 6, 5, 4)

count = 0
elem = []
ind = []

for i in range(len(a)):
    if a[i] == b[i] == c[i]:
        count += 1
        ind.append(i)
        elem.append(a[i])

print(count)
print(ind)
print(elem)