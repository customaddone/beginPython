# https://atcoder.jp/contests/abc138/tasks/abc138_dfro
from collections import deque

n, q = map(int, input().split())
dist = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    dist[a - 1].append(b - 1)
    # aftercontest対策
    # https://qiita.com/c-yan/items/887e2c2f410ecec60650
    # 双方向にappendしないと
    # dist = [[3, 2], [2], [], []]
    #   0
    #  / \
    # 2   3
    # \
    #  1　　　にしたいところが

    #   0      1
    #  / \    /
    # 2   3  2    のような変な木になる
    dist[b - 1].append(a - 1)
value = [0 for i in range(n)]

# 1つ目の[1, 10]と2つ目の[1, 10]混ぜても問題なし
# ここでvalueの構造を工夫して計算量を下げる努力を
for i in range(q):
    p, x = map(int, input().split())
    value[p - 1] += x
#  重複を防ぐ
ignore = [0] * n
ignore[0] = 1

pos = deque([0])
# 上から順に自身のvalueの値を子のvalueに加算していく
# value [100, 10, 1, 0]
# pos.popleft() = 1 → [100, 10 + 100, 1 + 100, 0 + 100]
# pos.popleft() = 2 → [100, 110, 101 + 10, 100 + 10]
while len(pos) > 0:
    u = pos.popleft()
    for i in dist[u]:
        if ignore[i] == 0:
            ignore[i] = 1
            value[i] += value[u]
            pos.append(i)
# 覚える
print(*value)
