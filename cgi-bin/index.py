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
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# codeforces 717 C - Baby Ehab Partitions Again
# 半公倍数を思い出す
# 総和の偶奇により戦略が変わる
# 全ての数が偶数なら割る　をする

N = getN()
A = getList()

while all([a % 2 == 0 for a in A]):
    A = [a // 2 for a in A]

if sum(A) % 2 != 0:
    print(0)
    exit()

prev = [0] * 200007
prev[0] = 1

for i in range(N):
    next = [0] * 200007
    for j in range(200007):
        next[j] += prev[j]
        if j + A[i] < 200007:
            next[j + A[i]] += prev[j]
    prev = next

if prev[sum(A) // 2] == 0:
    print(0)
else:
    for i in range(N):
        if A[i] % 2 != 0:
            print(1)
            print(i + 1)
            exit()
