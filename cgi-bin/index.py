# https://atcoder.jp/contests/abc084/tasks/abc084_d
import math

prime = [2]
max = 10 ** 5
limit = int(math.sqrt(max))
data = [i + 1 for i in range(2, max, 2)]

# エラストテネスの篩
while limit > data[0]:
    prime.append(data[0])
    data = [j for j in data if j % data[0] != 0]
prime = prime + data

# if (i + 1) / 2 in primeのにぶたん
def binary_search_loop(data, target):
    imin = 0
    imax = len(data) - 1
    while imin <= imax:
        imid = imin + (imax - imin) // 2
        if target == data[imid]:
            return True
        elif target < data[imid]:
            imax = imid - 1
        else:
            imin = imid + 1
    return False

# 累積和
lista = [0] * max
for i in prime:
    if binary_search_loop(prime, (i + 1) / 2):
        lista[i - 1] = 1
listb = [0]
for i in range(max):
    listb.append(lista[i] + listb[i])

# rまでの累積 - l - 1までの累積
q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(listb[r] - listb[l - 1])
