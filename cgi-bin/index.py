import collections
n = int(input())
s = [input() for _ in range(n)]
c = collections.Counter(s)
# c.most_common() [('taro', 2), ('jiro', 1), ('saburo', 1)]
# c.most_common()[0] ('taro', 2)
# c.most_common()[0][0] taro
print(c.most_common()[0][0])
