from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from bisect import bisect_left, bisect_right

import sys
def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# ABC021 C - 正直者の高橋くん
# 経路の通りを求める問題
N = 7
a, b = 1, 7
M = 8
que = [
[1, 2],
[1, 3],
[4, 2],
[4, 3],
[4, 5],
[4, 6],
[7, 5],
[7, 6]
]
dist = [[] for i in range(N)]
for x, y in que:
    dist[x - 1].append(y - 1)
    dist[y - 1].append(x - 1)

# スタートからの最短距離測定
def distance(sta):
    # 木をstaから順にたどる（戻るの禁止）
    pos = deque([sta])
    ignore = [-1] * N
    ignore[sta] = 0

    while len(pos) > 0:
        u = pos.popleft()
        for i in dist[u]:
            if ignore[i] == -1:
                ignore[i] = ignore[u] + 1
                pos.append(i)

    return ignore

d = distance(a - 1)

# スタートから特定の点まで最短距離で行く通りの数
def counter(sta):
    pos = deque([sta])
    ignore = [0] * N
    cnt = [0] * N
    cnt[sta] = 1

    while len(pos) > 0:
        u = pos.popleft()
        if ignore[u] == 0:
            ignore[u] = 1
            # d[i] == d[u] + 1を満たすuの子ノード全てに
            # 「スタートからuまでの通りの数」をプラス（他のルートからも来る）
            for i in dist[u]:
                if d[i] == d[u] + 1:
                    cnt[i] += cnt[u]
                    pos.append(i)
    return cnt

print(counter(a - 1)[b - 1] % mod)

# ARC044 B - 最短路問題
# 通りの数を求める問題
# 深さ1のものは,深さ2のものは
N = getN()
A = getList()
M = max(A)

if A[0] != 0:
    print(0)
    exit()

lista = [0] * (M + 1)
lista[0] = 1
for i in range(1, N):
    if A[i] == 0:
        print(0)
        exit()
    lista[A[i]] += 1

ans = 1
for i in range(1, M + 1):
    if lista[i] == 0:
        print(0)
        exit()
    # 全ての距離i - 1の点とある距離iの点との辺について
    # 繋いだ場合辺はi - 1の点の数だけあるが、これらのうち１つ以上と繋ぐ
    opt1 = (pow(2, lista[i - 1], mod) - 1)
    # それが距離iの点の数分ある
    depth = pow(opt1, lista[i], mod)
    # 距離i間の辺について
    # 辺はlista[i] * (lista[i] - 1) // 2だけあるが、そのうち０本以上と繋ぐ
    # これによって頂点の最短距離が変わることはない
    width = pow(2, lista[i] * (lista[i] - 1) // 2, mod)
    ans *=  depth * width
    ans %= mod
print(ans)

# F - Pure

"""
強連結成分分解とかの話に繋がってくる
つまりループを作ればいい
1 - 2 - 3 - 4 - 1みたいな
1 が2以外の例えば1 - 3みたいなパスがあれば
1 - 3 - 4 - 1で作ればいい

最小のループが答え
bfsなら早々に最小のものが見つかる

強連結
有向グラフにおいて、すべての頂点間で互いに行き来できる
強連結成分を一つの頂点に潰すと、DAGになる　トポソできる

まずbfsする　その後、戻れるエッジがあるか
あればその最小値が答え

まずbfsしてDAGで考えるともう処理したものを考えなくていいのでいろいろ便利
"""

N, M = getNM()
dist = [set() for i in range(N)]
for i in range(M):
    a, b = getNM()
    dist[a - 1].add(b - 1)

ignore = [-1] * N
path = [set() for i in range(N)] # 始点からのパス
parents = [-1] * N
roop = [-1] * N #  ループの始点と終点
roop_len = [-1] * N # ループの長さ

for i in range(N):
    if ignore[i] >= 0:
        continue

    ignore[i] = i
    pos = deque([[i, 0]])
    path[i].add(i)

    while pos:
        u, dis = pos.popleft()
        for j in list(dist[u]):
            if ignore[j] == -1:
                ignore[j] = i
                parents[j] = u
                # ループ判定
                path[j] = deepcopy(path[u])
                path[j].add(j)
                for i, e in enumerate(list(path[j])[::-1]): # 後ろから一つずつ
                    if e in dist[j]: # もし戻るパスがあれば
                        roop[j] = e # 終点j, 始点eのループがある
                        roop_len[j] = i + 1 # ループの長さ
                        break # 一番小さいのしかいらない

                pos.append([j, dis + 1])

# 最小のループを探す
l = float('inf')
index = -1
for i in range(N):
    if roop_len[i] >= 0 and roop_len[i] < l:
        l = min(l, roop_len[i])
        index = i

if index == -1:
    print(-1)
    exit()

# 構築
ans = [index + 1]
now = index
while now != roop[index]: # 始点に戻るまで
    now = parents[now]
    ans.append(now + 1)

print(l)
for i in ans[::-1]:
    print(i)

# AtCoder Beginner Contest 197（Sponsored by Panasonic）
# F Construct a Palindrome

N, M = getNM()
E = [[[] for i in range(26)] for i in range(N)]
adj = [set() for i in range(N)] # 隣接する頂点について
for _ in range(M):
    a, b, c = input().split()
    a = int(a) - 1
    b = int(b) - 1
    E[a][ord(c) - ord('a')].append(b)
    E[b][ord(c) - ord('a')].append(a)
    adj[a].add(b)
    adj[b].add(a)

ans = float('inf')
que = deque([(0, N - 1, 0)])
used = set()

while que:
    s, e, d = que.popleft()
    # 探索が一回目か
    if (s, e) in used:
        continue
    used.add((s, e))
    if s == e:
        ans = min(ans, d * 2)
    if e in adj[s]:
        ans = min(ans, d * 2 + 1)
    # a ~ zまでについて同じ文字の辺はあるか
    for i in range(26):
        for n_s in E[s][i]:
            for n_e in E[e][i]:
                que.append((n_s, n_e, d + 1))

if ans == float('inf'):
    print(-1)
else:
    print(ans)
