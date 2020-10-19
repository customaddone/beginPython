def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()
def rand_N(ran1, ran2):
    return random.randint(ran1, ran2)
def rand_List(ran1, ran2, rantime):
    return [random.randint(ran1, ran2) for i in range(rantime)]
def rand_ints_nodup(ran1, ran2, rantime):
  ns = []
  while len(ns) < rantime:
    n = random.randint(ran1, ran2)
    if not n in ns:
      ns.append(n)
  return sorted(ns)

def rand_query(ran1, ran2, rantime):
  r_query = []
  while len(r_query) < rantime:
    n_q = rand_ints_nodup(ran1, ran2, 2)
    if not n_q in r_query:
      r_query.append(n_q)
  return sorted(r_query)

from collections import defaultdict, deque, Counter
from sys import exit
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

# NOMURA プログラミングコンテスト 2020 C - Folia
"""
N = 3
A = [0, 1, 1, 2]の場合
葉の数を求める
まず完全二分木から考える
ここから取り除く
深さ3の葉は4つある
深さ4の葉は8つある
深さnの葉は2 ** (n - 1)つある

深さ3の葉は4つある完全二分木について
A = [0, 0, 0, 4]
深さ3の葉を一つ刈ると
A = [0, 0, 0, 3]
二つ刈ってみる　この時、１つ目と同じ親のを刈ると
A = [0, 0, 1, 2]
違うのを刈ると
A = [0, 0, 0, 2]
根となる頂点を１つ作る
A[0] = 1ならその頂点は葉（下に頂点を繋げない)
A[0] = 0ならその頂点は生きる

頂点の最大値を求めるなら
なるべく大きく分岐させた方がいい
エッジ貼らなくても頂点数求めるだけでいい
A[i]を探索するたびに ans += する

現在用意している仮の頂点数を保持しておく
確定させた頂点数も抑えておく

A = [0, 0, 1, 0, 2]を逆から見ると
psuedo = [1, 2, 4, 8, 16]
psuedoのそれぞれとA[4]どちらか小さい方をpsuedoから引く
psuedo = [0, 0, 2, 6, 14]

left[0] ~ left[i]のそれぞれでA[i]を引けるだけ引く
順に見ると
psuedo = []
left = [] # ansに加える値
A[0] = 0
psuedo = [1]
left = [1]
A[1] = 0
psuedo = [1, 2]
left = [1, 2]
A[2] = 1
psuedo = [1, 2, 3]
left = [0, 1, 3]
A[3] = 0
psuedo = [1, 2, 3, 6]
left = [0, 1, 3, 6]
A[4] = 2
psuedo = [1, 2, 3, 6, 10]
left = [0, 0, 1, 4, 10]

葉にならない点の上限を考える
"""

# 根から探索するか
# 葉から探索するか

# 私は根から
# 総和には累積和が効く
N = getN()
A = getList()

# 深さ0の二分木の場合
if N == 0:
    if A[0] == 1:
        print(1)
    else:
        print(-1)
    exit()

if A[0] == 0:
    psuedo = [1]
    left = [1] # 確定させる用
else:
    psuedo = [0]
    left = [0]

alta = deepcopy(A)
for i in range(N - 1, -1, -1):
    alta[i] += alta[i + 1]
ma = max(alta)

# i + 1番目について調べる
for i in range(1, N + 1):
    opt = min(psuedo[-1] * 2, ma) # stop指数爆発 今回max(alta)以上の数字は必要ない
    psuedo.append(opt)
    left.append(opt)
    if psuedo[-1] - A[i] < 0:
        print(-1)
        exit()
    psuedo[-1] -= A[i]
    # 確定させていく
    """
    明らか追いつかないので累積する
    for j in range(i, -1, -1):
        if dete[j] == 0:
            break
        add = min(dete[j], A[i])
        ans += add
        dete[j] -= add
    """

ans = 0

for i in range(N + 1):
    ans += min(left[i], alta[i])
print(ans)

# ARC011 ダブレット
# つまり最短経路問題
s1, s2 = input().split(' ')
N = getN()
S = set()

S.add(s1)
S.add(s2)

for i in range(N):
    S.add(input())

if s1 == s2:
    print(0)
    print(s1)
    print(s2)
    exit()

S = list(S)
N = len(S)

# 2つにエッジを貼れるか
def judge(s1, s2):
    cnt = 0
    n = len(s1)
    for i in range(n):
        if s1[i] != s2[i]:
            cnt += 1
    if cnt <= 1:
        return True
    else:
        return False

dist = [[] for i in range(N)]
d = [[float('inf')] * N for i in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        if judge(S[i], S[j]):
            dist[i].append(j)
            dist[j].append(i)
            d[i][j] = 1
            d[j][i] = 1

sta = 0
end = 0
for i in range(N):
    if S[i] == s1:
        sta = i
        break
for i in range(N):
    if S[i] == s2:
        end = i
        break

# ダイクストラする
def dij(start, edges):
    dist = [float('inf') for i in range(N)]
    dist[start] = 0
    pq = [(0, start)]

    # pqの先頭がgoal行きのものなら最短距離を返す
    while len(pq) > 0:
        di, now = heapq.heappop(pq)
        if (di > dist[now]):
            continue
        for i in edges[now]:
            if dist[i] > dist[now] + d[i][now]:
                dist[i] = dist[now] + d[i][now]
                heapq.heappush(pq, (dist[i], i))
    return dist

distance = dij(sta, dist)
if distance[end] == float('inf'):
    print(-1)
    exit()

# 最短経路を示す矢印を求める
# ダイクストラと同じ要領で
def router(n, sta):
    pos = deque([sta])
    ignore = [0] * n
    path = [0] * n
    ignore[sta] = 0
    path[sta] = -1

    while pos:
        u = pos.popleft()

        for i in dist[u]:
            if ignore[i] != 1 and distance[i] == ignore[u] + d[i][u]:
                path[i] = u
                ignore[i] = ignore[u] + d[i][u]
                pos.append(i)

    return path

path = router(N, sta)
ans = [S[end]]
now = end
while True:
    now = path[now]
    ans.append(S[now])
    if now == sta:
        break

print(len(ans) - 2)
for i in range(len(ans)):
    print(ans[-i - 1])
