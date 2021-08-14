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
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

"""
N個のボールを入れる
maxflowしたいが
limitは更新されるか
"""

from heapq import *
for _ in range(int(input())):
	n = int(input())
	lr = [list(map(int, input().split())) for i in range(n)]
	lr.sort()
	lr.append((10 ** 18, 10 ** 18))
	cur = -(10 ** 18)
	Q = []
	heapify(Q)
	ans = "Yes"
	for i in range(n + 1):
		while Q and cur < lr[i][0]:
			g = heappop(Q)
			if cur > g: ans = "No"; break
			cur += 1
		cur = lr[i][0]
		heappush(Q, lr[i][1])
	print(ans)
