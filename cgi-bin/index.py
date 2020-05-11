def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

from collections import defaultdict, deque
from sys import exit
import math
import copy
from bisect import bisect_left

import sys
# sys.setrecursionlimit(1000000)
# list(map(int, input().split()))
mod = 10 ** 9 + 7

from collections import deque

# まず、Kの最小値を求める
#　頂点に繋がる辺の数 <= Kを全ての頂点で満たす
N = getN()
dist = [[] for i in range(N + 1)]
# エッジの配列はこうする
edge = {}
for i in range(N - 1):
    a, b = getNM()
    dist[a].append(b)
    dist[b].append(a)
    # エッジの色の入力の仕方
    edge[(a, b)] = i
    edge[(b, a)] = i

ignore = [-1] * (N + 1)
ignore[1] = 0
# 辺の数は頂点の数より一つ少ない
ans = [0] * (N - 1)

pos = deque([1])
while len(pos) > 0:
    u = pos.popleft()
    # 一番最初の色から順にサーチしていく
    j = 1
    for i in dist[u]:
        if ignore[i] < 0:
            # 根元の頂点の色と一致していたら色を変える
            if j == ignore[u]:
                j += 1
            # 辺をスライドしていくたびに行先の頂点の色を変える
            ignore[i] = j
            # 辺の色は行先の頂点の色に合わせる
            ans[edge[(i, u)]] = j
            pos.append(i)
            j += 1
print(max(ans))
for a in ans:
    print(a)
