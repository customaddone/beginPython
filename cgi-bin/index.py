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
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
inf = float('inf')
eps = 10 ** (-12)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

def euler_tour(N, E, sta):
    q = deque([[sta, 1]])
    dis = [-1] * N
    dis[sta] = 0
    par = [-1] * N

    dp = things

    while q:
        u, f = q.pop()
        if f:
            #### 行きがけ処理をここに書く ###
            # do function
            #############################
            q.append([u, 0])
            for v in E[u]:
                if dis[v] == -1:
                    dis[v] = dis[u] + 1
                    par[v] = u
                    q.append([v, 1])
                    #### 子に操作するときはここに書く
                    # do function
                    #############################

        else:
            #### 帰りがけ処理をここに書く ###
            # do function
            if dp[u] and u != sta:
                dp[par[u]] = 1
            #############################

    return dp, dis

T = getN()
for _ in range(T):
    _ = input()
    N, K = getNM()
    sta, end = getNM()
    sta -= 1
    end -= 1
    col = getListGraph()
    E = [[] for i in range(N)]
    for i in range(N - 1):
        u, v = getNM()
        E[u - 1].append(v - 1)
        E[v - 1].append(u - 1)
    things = [0] * N
    things[end] = 1
    for c in col:
        things[c] = 1

    tour, dis = euler_tour(N, E, sta)
    print((sum(tour) - 1) * 2 - dis[end])
