#https://atcoder.jp/contests/abc106/tasks/abc106_b
n = int(input())
cnt = 0
lista = [0] * (n + 1)
for i in range(1, n + 1, 2):
    # 内部でカウント用cを持つ
    c = 1
    # 1からi（現在の数字）まで
    for j in range(1, i, 2):
        if i % j == 0:
            c += 1
    if c == 8:
        cnt += 1
print(cnt)
"""
# 奇数のみ
for i in range(1, n + 1, 2):
    # 3 * 1, 3 * 3, 3 * 5...
    for j in range(i, n + 1, 2 * i):
        lista[j] += 1
for i in range(n + 1):
    if lista[i] == 8:
        cnt += 1
print(cnt)
"""
