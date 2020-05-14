def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()

from collections import defaultdict, deque, Counter
from sys import exit
import heapq
import math
import copy
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)

N = getN()
dist = [[] for i in range(N + 1)]
for i in range(N - 1):
    a, b, c = getNM()
    dist[a].append([b, c])
    dist[b].append([a, c])
ignore = [-1] * (N + 1)

# Kからの最短距離をbfsで測る
# 必ずKを経由するのがポイント
# 前処理O(n)だけですむ
def distance(sta):
    # 木をKから順にたどる（戻るの禁止）
    pos = deque([sta])

    while len(pos) > 0:
        u = pos.popleft()
        for i in dist[u]:
            if ignore[i[0]] == -1:
                ignore[i[0]] = ignore[u] + i[1]
                pos.append(i[0])

Q, K = getNM()
ignore[K] = 0
distance(K)
# 答えはK~xまでの距離+K~yまでの距離
ans = []
for i in range(Q):
    x, y = getNM()
    ans.append(ignore[x] + ignore[y])
for i in ans:
    print(i)
