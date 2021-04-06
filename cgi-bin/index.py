from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product
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

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

def array_cnt(ar1, ar2):
    h = len(ar1)
    w = len(ar2[0])
    row = ar1
    col = []
    for j in range(w):
        opt = []
        for i in range(len(ar2)):
            opt.append(ar2[i][j])
        col.append(opt)

    res = [[[0, 0] for i in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            cnt = 0
            for x, y in zip(row[i], col[j]):
                cnt += x * y
            res[i][j] = cnt
    return res

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
o1 = [[1, 0, 0], [0, 1, 0], [-7, 0, 1]]
o2 = [[1, 0, 0], [-4, 1, 0], [0, 0, 1]]
o3 = [[1, -2, 0], [0, 1, 0], [0, 0, 1]]
o4 = [[1, 0, -3], [0, 1, 0], [0, 0, 1]]
a = array_cnt(o1, a) # 右
a = array_cnt(o2, a)
a = array_cnt(a, o3) # 左
a = array_cnt(a, o4)
# [[1, 0, 0], [0, -3, -6], [0, -6, -12]]
print(a)
