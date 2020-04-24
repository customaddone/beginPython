# https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_c
import itertools
n, m = map(int, input().split())
lista = []
for i in range(n):
    a = list(map(int, input().split()))
    lista.append(a)
# i, jで選曲
for i in range(m):
    for j in range(i + 1, m):
        tmp = 0
        for k in range(n):
            tmp += max(a[k][i], a[k[j])
        res = max(res, tmp)
print(res)

"""
maxscore = 0
# 全ての状態（何番目と何番目を選ぶか）を試す
# combinationsはあんま使わない？
for i in itertools.combinations(range(m), 2):
    score = 0
    for j in range(n):
        score += max(lista[j][i[0]], lista[j][i[1]])
    maxscore = max(maxscore, score)
print(maxscore)
"""
