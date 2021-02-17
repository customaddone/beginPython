from collections import defaultdict, deque, Counter
import sys
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce, lru_cache
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
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
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# ABC075 C-bridge

# O(N + M)解 lowlink解
# 橋: 取り除くとグラフが連結でなくなる辺　取り除いてはいけない辺
# 後退辺: dfsする時に通らなかった辺

# 辺(u, v)について
# order[u]: uを何番目に通ったか
# low[v]: vから葉の方向に何回でも、後退辺を１回以下辿っていける点wについて、order[w]の最小値
# そもそも後退辺がない場合はlow[v] = order[v]である
# low[v] <= order[u]の場合、
# 自分より下流にある頂点が自分より上流の頂点と繋がっている = 外しても連結のままの辺
# そうではないものorder[u] < low[v]の辺(u, v)が橋

N, M = getNM()
edges = [getList() for i in range(M)]
edges = [[a - 1, b - 1] for a, b in edges]
E = [[] for i in range(N)]
for i, (a, b) in enumerate(edges):
    E[a].append([b, i])
    E[b].append([a, i])

cnt = 0
order = [-1] * N # 何番目に通ったか
e_cnt = [0] * M
# 木をdfsする
def dfs(u):
    global cnt
    # 何番目に通ったかを記録する
    order[u] = cnt
    cnt += 1
    for v, index in E[u]:
        if order[v] == -1:
            # 使った辺を記録する
            e_cnt[index] = 1
            dfs(v)

dfs(0)

low = deepcopy(order) # vからの後退辺を１回辿っていける点wについて、order[w]の最小値
for i, (a, b) in enumerate(edges):
    if e_cnt[i] == 0:
        low[a] = min(low[a], order[b])
        low[b] = min(low[b], order[a])

# lowlinkを求める
ignore = [0] * N
def lowlink(u):
    global ignore # 木ではないのでroot型ではなくignore型
    res = low[u]
    ignore[u] = 1
    for v, index in E[u]:
        if ignore[v] == 0:
            res = min(res, lowlink(v))
    low[u] = res
    return res

lowlink(0)

ans = [0] * M
for i, (a, b) in enumerate(edges):
    # 順番になるように
    if order[a] > order[b]:
        a, b = b, a
    if order[a] < low[b]:
        ans[i] += 1
print(sum(ans))
