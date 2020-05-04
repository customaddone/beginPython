# https://atcoder.jp/contests/abc014/tasks/abc014_3
n = int(input())
lista = []
for i in range(n):
    a, b = map(int, input().split())
    lista.append([a, b])
listb = [0] * (10 ** 6 + 2)
for i in lista:
    listb[i[0]] += 1
    listb[i[1] + 1] -= 1
listc = [0]
for i in range(10 ** 6 + 2):
    listc.append(listb[i] + listc[i])
print(max(listc))
