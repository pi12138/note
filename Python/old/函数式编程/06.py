
# 排序案例

# help(sorted)

list1 = [222, 333, 1, 444, 5555, 6666, 22]

list2 = sorted(list1)
list3 = sorted(list1, reverse = True)

print("list2:", list2)
print('list3:', list3)
print('-' * 50)

list4 = [-11, 22, -3, 555, 666, -888]
list5 = sorted(list4)
list6 = sorted(list4, key = abs)
print('list5:', list5)
print('list6:', list6)
print("*" * 50)

list7 = ['zyp', 'zy', 'gzy', 'gyj', 'lfs', 'kah', 'ZYP']
list8 = sorted(list7)
list9 = sorted(list7, key = str.lower)
print('list8:', list8)
print('list9:', list9)




