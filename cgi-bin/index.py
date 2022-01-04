from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product, combinations_with_replacement
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
def getListGraph():
    return list(map(lambda x:int(x) - 1, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353
# sys.setrecursionlimit(10000000)
inf = float('inf')
eps = 10 ** (-15)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

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

# E - + Graph

"""
まず木グラフを作る
奇数個目 x+a
偶数個目 b-x ができる
x + a > 0, b - x > 0より-a < x < bの正の部分
二分グラフの問題
"""

N, M = getNM()
E = [[] for i in range(N)]
for _ in range(M):
    u, v, s = getNM()
    E[u - 1].append([v - 1, s])
    E[v - 1].append([u - 1, s])

# 0が偶数個目、1が奇数個目
ignore = [-1] * N
dist = [-1] * N
ignore[0] = 0
dist[0] = 0
decided = set() # 二個以上あるとだめ
q = deque([0])

mi, ma = 0, inf
while q:
    u = q.popleft()
    for v, s in E[u]:
        # 未探索
        if ignore[v] == -1:
            ignore[v] = ignore[u] ^ 1
            dist[v] = s - dist[u]
            q.append(v)
        # 探索済み　検査する
        # グループが違う
        if ignore[u] ^ ignore[v]:
            # 矛盾
            if (s - dist[u]) != dist[v]:
                ma = -inf # なし 0になる
        # グループが同じ
        else:
            decided.add((s - dist[u] - dist[v]) * ((-1) ** (ignore[u] % 2)))

for i in range(N):
    # -aの最大値を探す
    if ignore[i] == 0:
        mi = max(mi, -dist[i])
    # bの最小値を探す
    else:
        ma = min(ma, dist[i])

# 矛盾
if len(decided) > 1:
    print(0)
elif len(decided) == 1:
    opt = list(decided)[0]
    # 偶数かつ範囲内にある
    if opt % 2 == 0 and mi < (opt // 2) and (opt // 2) < ma:
        print(1)
    else:
        print(0)
else:
    print(max(0, ma - mi - 1))
