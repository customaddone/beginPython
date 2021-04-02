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
mod = 998244353
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# CODE FESTIVAL 2017 qual B C - 3 Steps

"""
N頂点の連結な無向グラフがある　M辺既にある(M >= N - 1)
N <= 10 ** 5
一応M <= 10 ** 5なのでダイクストラ使える
辺を追加していく
頂点uから距離3ある（最短距離でなくてもいい）vを取り、直通の辺をプラス
最大でいくつ

辺を追加する度に他の頂点の選択肢は増えるはずだから
parentから3 = childから2]
uのchildでない頂点vに線を引く　そこから
u - vに線を引くと
uのchild - vのchildにも線を引ける
つまりuのchildとvのchildは同じグループであり、互いに線を引ける

M本の辺について順に探索していくか
結局グループは２つにしかならないのでは
頂点1から見た距離
頂点uのchildのどれかと頂点vのchildのどれかに線があれば繋げる

一本ずつ引いていくと最悪N ** 2になる
UnionFindか
1とiはufか
u - vに線を引くと
uのchild - vのchildにも線を引ける

周４の輪ができる
距離３、５、７...の辺はあるか
距離１の場合は既に線がある
奇数長のパスはあるか

二部グラフでなければ偶奇関係なく好きな回数で好きな場所に行ける
"""

N, M = getNM()
Q = [getList() for i in range(M)]

# 1 - indexで
def bipartite(N, M, edges):
    g = defaultdict(list)
    for a, b in edges:
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)

    color = [0] * (N + 1)
    dq = deque([(0, 1)])

    while dq:
        v, c = dq.popleft()
        color[v] = c
        c *= -1
        for nv in g[v]: # 頂点vの各childを調べる
            if color[nv] == 0: # もし未探索なら
                dq.append((nv, c))
            if color[nv] == -c: # もしcolor[nv]がvの色を反転させたものでなければ
                dq = []
                return False, color

    return True, color

res =  bipartite(N, M, Q)
if res[0]:
    nb = res[1].count(1)
    nw = res[1].count(-1)
    print(nb * nw - M)
else:
    print(N * (N - 1) // 2 - M)

# ARC099 E - Independence
# 補グラフ　エッジの反転を考える
# iとjは同じグループにならない　を繰り返す

"""
N <= 700 探索できるか
貪欲しかないが
N個の都市、M個の道
２つのグループにする

まず分けることは可能かどうか　
最低でも道はi(i + 1) / 2ないといけない
鳩の巣原理使う？
グループ1の大きさ:a
グループ2の大きさ:b とすると
求める答えはM - a(a+1)/2 - b(b+1)/2
なるべくaとbがイーブンになるようにしたいね

分けることは可能かどうか
グループaに都市iを加えることはできるか
N <= 700しかないのか
前にエッジが飛ぶようにする
各頂点は頂点0と同じか違うかしかない
aとbがイーブンになるように
[[], [0], [0], [2], [2, 3]]
頂点1は0とグループ可能
頂点3は2とグループ可能
頂点4は2, 3とグループ可能
N ** 2までは十分可能なので
0と同じにするか違うにするか

単純な方法だと2 ** Nこれを減らす
自明に違うグループに属するものは
二部グラフについて考える

ないもの（グループにできない）をエッジにする
二部グラフ　残ったやつで二部グラフ
"""

N, M = getNM()
E = [[i for i in range(N)] for j in range(N)]
for i in range(M):
    a, b = getNM()
    E[b - 1].remove(a - 1)
    E[a - 1].remove(b - 1)
for i in range(N):
    E[i].remove(i)

ign = [1] * N
flag = True
l = []

# 二部グラフ判定
for i in range(N):
    if ign[i] == 0:
        continue
    ign[i] = 0
    color = [0] * N
    color[i] = 1
    q = deque([i])
    while q:
        u = q.popleft()
        for v in E[u]:
            if color[v] == 0:
                color[v] = color[u] * (-1)
                ign[v] = 0
                q.append(v)
            elif color[v] != color[u] * (-1):
                flag = False
                break

    l.append([color.count(1), color.count(-1)])

if not flag:
    print(-1)
    exit()

# 部分和
prev = [0] * 701
prev[0] = 1
for i in range(len(l)):
    next = [0] * 701
    for j in range(701):
        if j - l[i][0] >= 0:
            next[j] += prev[j - l[i][0]]
        if j - l[i][1] >= 0:
            next[j] += prev[j - l[i][1]]
    prev = next

ans = float('inf')
for i in range(701):
    if prev[i]:
        o = N - i
        ans = min(ans, i * (i - 1) // 2 + o * (o - 1) // 2)
print(ans)

# C - オレンジグラフ

"""
奇数長の閉路はできない　二分グラフか
まず木の作り方は何通りあるか
そして偶数長を埋めると
木だから条件は緩いはず

bitでグループAとグループBに分ける
グループAの頂点はグループBの頂点につなぐ
全てつなぐ　だから
"""

N, M = getNM()
E = []
for i in range(M):
    x, y = getNM()
    E.append([x - 1, y - 1])

ans = 0
for bit in range(1 << N):
    a = set()
    b = set()
    U = UnionFind(N)
    for i in range(N):
        if bit & (1 << i):
            a.add(i)
        else:
            b.add(i)
    for x, y in E:
        # 違うグループにあったら
        # 条件を満たすものは全てつなぐ
        if not ((x in a) ^ (y in b)):
            U.union(x, y)

    if len(U.roots()) == 1:
        ans += 1

# 0101と1010は同じものであるため
print(ans // 2)
