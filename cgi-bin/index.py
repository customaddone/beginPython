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
# sys.setrecursionlimit(1000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# ABC153 F - Silver Fox vs Monster

# 遅延セグは使わない
# 二分探索したい
# imosする
# どこに爆弾を投下するか
# 効率のいい方法
# 現在地点に爆弾を投下してモンスターを倒すまで
# -D ~ Dまで = 前に2 * Dの範囲に効くと
# bisect_right

N, D, A = getNM()
# 座標Xにいる 体力はH
mons = [getList() for i in range(N)]
mons.sort()
X = []
H = []
for x, h in mons:
    X.append(x)
    H.append(h)

# 累積ダメージ
cnt = 0
r = 0
imos = [0] * (N + 1)
for i in range(N):
    # 爆風範囲
    while r < N and X[i] + 2 * D >= X[r]:
        r += 1
    if i > 0:
        imos[i] += imos[i - 1]
    # ここで爆弾を投下する回数
    hp = max(H[i] - imos[i], 0)
    t = (hp + A - 1) // A # 爆風のぶんを削る
    cnt += t
    # imos
    imos[i] += t * A
    imos[r] -= t * A

print(cnt)

# edufo #102 D. Program

"""
l~r間のinstructionを実行して値が何種類出るか
値は連続するので最大値と最小値を求めればいい
imosするだけでは...
[0, -1, 0, -1, -2, -1, -2, -3, -2]
I[r] - I[l - 1]するとどれだけ変化したかがわかる
これを全区間でやって最大値、最小値をだす

選ばれた区間は除外して
つまり前と後ろからimosする　区間の最大値、最小値は保持しておく
"""

T = getN()
for _ in range(T):
    N, Q = getNM()
    # 累積和
    Ins = [0] + [1 if s == '+' else -1 for s in list(input())]
    for i in range(1, N + 1):
        Ins[i] += Ins[i - 1]

    # ラムダ式でseg木を立てられる
    seg_min = SegTree(Ins, lambda x, y: min(x, y), inf)
    seg_max = SegTree(Ins, lambda x, y: max(x, y), -inf)
    for _ in range(Q):
        l, r = getNM()
        mi, ma = seg_min.query(0, l), seg_max.query(0, l)
        if r < N:
            # 中間の区間で増えた分を差し引く
            mi = min(mi, seg_min.query(r + 1, N + 1) - (Ins[r] - Ins[l - 1]))
            ma = max(ma, seg_max.query(r + 1, N + 1) - (Ins[r] - Ins[l - 1]))

        print(ma - mi + 1)
