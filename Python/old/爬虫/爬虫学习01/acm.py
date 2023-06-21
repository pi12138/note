
str1 = input('gxd:')
str2 = input("laowen:")

l1 = list(str1)
l2 = list(str2)


m = 0
n = 0

for i in l1:
    if i == 'w' or i == 'W':
        m = m + 1

for j in l2:
    if j == 'w' or i == 'W':
        n = n + 1

# print(m, n)
if m >= n:
    print("I'm the best!")

else:
    print("You take me to the hospital!")