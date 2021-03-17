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

# ABC189 Fより
# 1 ~ Mの目が出るサイコロで0 ~ Nまでいく場合の確率と期待値
# ゴールは超過していい
N, M = getNM()

# 0からマスiに到達する確率を求める
P = [0] * (N + M + 1)
P[0] = 1
rec = [0] * (N + M + 1)

for i in range(N + M + 1):
    if 0 < i:
        rec[i] += rec[i - 1]
    P[i] += rec[i]
    P[i] = max(0, P[i])

    if i < N:
        rec[i + 1] += P[i] / M
        rec[i + M + 1] -= P[i] / M

# 0からマスiに到達する期待値を求める
E = [0] * (N + M + 1)
rec = [0] * (N + M + 1)

for i in range(N + M + 1):
    if 0 < i:
        rec[i] += rec[i - 1]
    E[i] += rec[i]
    E[i] = max(E[i], 0)
    # iにくる確率の逆数でかける
    if P[i]:
        E[i] = E[i] / P[i]

    if i < N:
        # P[i] / M:その方面から飛んでくることがある確率
        rec[i + 1] += P[i] * (E[i] + 1) / M
        rec[i + M + 1] -= P[i] * (E[i] + 1) / M
print(P, E, rec)
