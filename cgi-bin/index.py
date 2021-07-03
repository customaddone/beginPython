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
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

"""
エッジの本数が多い√M頂点については別に監視する

まずそれ以外の頂点について考える
読み取る場合は隣接する頂点の色について調べる

特殊頂点について
隣接頂点をすべて読むことは不可能
何色になっているかは実際に自身が何色になってるかだけ見る

つまり
特殊頂点
それ以外の頂点からの書き込み + スプレッダーからの書き込み
が書き込まれる
それ以外の頂点
周囲の頂点の色を見る　一番最後にクエリがあったとこの色が自身の色
書き込みがされないので周囲を見る
"""

N, M = getNM()
G = [getListGraph() for i in range(M)]
E = [[] for i in range(N)]
for a, b in G:
    E[a].append(b)
    E[b].append(a)

# 特殊頂点は最高√M個
spec = set([i for i in range(N) if len(E[i]) >= math.sqrt(N) + 1])
s_E = [[] for i in range(N)]
for a, b in G:
    # 子要素がspecであれば追加
    if b in spec:
        s_E[a].append(b)
    if a in spec:
        s_E[b].append(a)

Q = getN()
last = [-1] * N
color = [1] * N # 最後のクエリがあったときの色を見る
spec_c = [1] * N # spec頂点について現在の色
for i in range(Q):
    x, c = getNM()
    x -= 1
    # 現在の頂点がspecなら自身の現在の色（書き込まれてる）を見る
    if x in spec:
        print(spec_c[x])
    # それ以外　頂点数が少ないのですべて探索できる
    else:
        opt = x
        l = last[x] # 自身も候補
        # 最後にクエリがあった箇所を探す
        for v in E[x]:
            if last[v] > l:
                opt = v
                l = last[v]
        # 最後にクエリがあった場所の色が現在の自身の色
        print(color[opt])

    # 書き込み last, color, spec_cに書き込み
    last[x] = i
    color[x] = spec_c[x] = c

    # 隣接するspec_cの書き込み
    for v in s_E[x]:
        spec_c[v] = color[x]
