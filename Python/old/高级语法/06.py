from collections import Counter

# 需要括号里的内容可迭代

str1 = 'aaaahdjkahsdkahsdkashkdhjkahsdkhajkhdiquweyoqyweoquwhjo'
c1 = Counter(str1)
print(c1)

list1 = ['zyp', 'zy', 'zyy', 'gzy', 'kah', 'lfs', 'gyj', 'zyp']
c2 = Counter(list1)
print(c2)

help(Counter)