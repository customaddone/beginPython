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
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353
sys.setrecursionlimit(1000000)
INF = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# codeforces round722 C - Parsa's Humongous Tree

"""
point v has two integer l, r
全ての辺について両端の点の絶対値を求める
これを最大化したい
普通に全探索するか　頂点0から始めてOKか
dfsでもしてみるか　l, rのどちらか一方
0をlにした時、rにした時
絶対値はリニアーになっている
ジグザグに走っていけばいいが
"""

T = getN()
for _ in range(T):
    N = getN()
    ran = [getList() for i in range(N)]
    E = [[] for i in range(N)]
    for i in range(N - 1):
        a, b = getNM()
        E[a - 1].append(b - 1)
        E[b - 1].append(a - 1)

    def dfs(u, p):
        lef = 0
        rig = 0
        for v in E[u]:
            if v != p:
                c_l, c_r = dfs(v, u)
                lef += max(abs(ran[u][0] - ran[v][0]) + c_l, abs(ran[u][0] - ran[v][1]) + c_r)
                rig += max(abs(ran[u][1] - ran[v][0]) + c_l, abs(ran[u][1] - ran[u][1]) + c_r)

        return lef, rig

    ans = dfs(0, -1)
    print(max(ans))
