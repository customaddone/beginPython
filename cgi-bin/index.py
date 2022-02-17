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
sys.setrecursionlimit(10000000)
inf = float('inf')
eps = 10 ** (-15)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

"""
刻まれるとしんどい
時間が来たら頂点iの人を頂点jに動かす
この操作は2M回しかない
頂点にいる人をいっぺんに動かせれば
効率的な付け替え方法

マージする
辺を頂点にする
"""

N, M, Q = getNM()
e_d = {}
E = [] # イベント
for i in range(M):
    a, b, s, t = getNM()
    e_d[i + N] = (a, b)
    E.append([s + 0.5, a - 1, i + N])
    E.append([t + 0.5, i + N, b - 1])

for i in range(Q):
    x, y, z = getNM()
    # start
    E.append([y, -1, x - 1, i])
    # goal
    E.append([z, -2, x - 1, i])

E.sort()
# グループiの名前は何か
g_name = [i for i in range(N + M)]
# グループiには誰が属するか
g = [set() for i in range(N + M)]
# 名前jのグループはどこにあるか
rev_g = [i for i in range(N + M)]
# どのグループに属するか
bel = [-1 for i in range(N + M)]
for e in E:
    # start グループの名称はe[2], グループはrev_g[e[2]]
    if e[1] == -1:
        bel[e[3]] = g_name[rev_g[e[2]]]
        g[rev_g[e[2]]] .add(i)
    # goal
    elif e[1] == -2:
        bel[e[3]] = -1
    else:
        # グループ名称xからグループ名称yへと移動する
        _, x, y = e
        # そのまま移動させたらいい
        if len(x) <= len(y):
