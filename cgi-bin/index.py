from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import sys
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from bisect import bisect_left, bisect_right

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

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import sys
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from bisect import bisect_left, bisect_right

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

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# ABC144 F - Fork in the Road

"""
塞いだあと高橋くんがどこかで詰まったらだめ
辺を一つ消す　判定するをN回繰り返す
dpする？
dp[i][j]: 頂点iにj回の移動で到達する確率

# dp[i][j]: 頂点iにj回の移動で到達する確率
dp = [[0] * (N + 1) for i in range(N)]
dp[0][0] = 1

# 頂点
for i in range(N):
    # j回の移動で
    for j in range(i + 1):
        for v in E[i]:
            dp[v][j + 1] += dp[i][j] / len(E[i])
print(dp)

一回の判定でO(M)ぐらいかかる
エッジにウェートをかけると？
エッジを見るだけでなんとかなるように
dpの全てについて調べる必要はないんでは
P[s] * (1 / M)の大きさが最も大きいものが一番Nの期待値への寄与度が大きい
"""

N, M = getNM()
dist = [[] for i in range(N)]
for i in range(M):
    s, t = getNM()
    dist[s - 1].append(t - 1)
for i in range(N):
    dist[i].sort()

# トポロジカルソートにすればs < tの条件がなくても使える
def calc(edges):
    # 確率を計算
    P = [0] * N
    P[0] = 1
    for u in range(N):
        for v in edges[u]:
            P[v] += P[u] / len(edges[u])

    # 期待値を計算　ゴールから逆向きで期待値を求める
    # あと何回進めばゴールまで行けるか
    E = [0] * N
    for u in range(N - 1, -1, -1):
        for v in edges[u]:
            # この(E[v] + 1)が大きくなるものを削ればいい
            E[u] += (E[v] + 1) / len(edges[u])

    return P, E

P, E = calc(dist)
ans = E[0]
diff = 0

for u in range(N):
    for v in dist[u]:
        if len(dist[u]) > 1:
            # u ~ vの辺を削ると(E[v] + 1) / len(dist[u])の分だけ軽くなるが
            # 残った分が len(dist[u]) / (len(dist[u]) - 1)でかけられる
            ban = (E[v] + 1) / len(dist[u]) # これが消える予定
            new = (E[u] - ban) * len(dist[u]) / (len(dist[u]) - 1)
            diff = max(diff, (E[u] - new) * P[u])

print(ans - diff)
