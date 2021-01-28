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
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

N = 5
#es = [[1,2,3],[0,2],[0,1],[0,4],[3]] # False
dist = [
[1, 3],
[0, 2],
[1, 3],
[0, 2, 4],
[3]
] # True

#n個の頂点の色を初期化。0:未着色、1:黒、-1:白
colors = [0] * N

#頂点vをcolor(1 or -1)で塗り、再帰的に矛盾がないか調べる。矛盾があればFalse
def dfs(v, color):
    #今いる点を着色
    colors[v] = color
    #今の頂点から行けるところをチェック
    for to in dist[v]:
        #同じ色が隣接してしまったらFalse
        if colors[to] == color:
            return False
        #未着色の頂点があったら反転した色を指定し、再帰的に調べる
        if colors[to] == 0 and not dfs(to, -color):
            return False
    #調べ終わったら矛盾がないのでTrue
    return True

#2部グラフならTrue, そうでなければFalse
def is_bipartite():
    return dfs(0,1) # 頂点0を黒(1)で塗ってDFS開始

print(is_bipartite())

# AGC039 B-Graph Partition

N = getN()
S = [list(input()) for i in range(N)]
G = [[] for i in range(N)]
E = [[INF] * N for i in range(N)]
for i in range(N):
    E[i][i] = 0
for i in range(N):
    for j in range(N):
        if S[i][j] == '1':
            G[i].append(j)
            E[i][j] = 1

def bipartite(edges):
    colors = [0] * N

    def dfs(v, color):
        colors[v] = color
        for to in edges[v]:
            if colors[to] == color:
                return False
            if colors[to] == 0 and not dfs(to, -color):
                return False

        return True

    return dfs(0, 1) # 頂点0を黒(1)で塗ってDFS開始

if not bipartite(G):
    print(-1)
    exit()

def warshall_floyd(dist):
    for k in range(N):
        # i:start j:goal k:中間地点でループ回す
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

warshall_floyd(E)
print(max([max(E[i]) for i in range(N)]) + 1)
