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

# a[i]はlike 2017
lista = [0] * max
for i in prime:
    if (i + 1) / 2 in prime:
        lista[i - 1] = 1

# 累積和
listb = [0]
for i in range(max):
    listb.append(lista[i] + listb[i])

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(listb[r] - listb[l - 1])
