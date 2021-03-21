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

N = getN()
manu = [getList() for i in range(N)]
Q = getN()
que = getList()

# 上界と下界を求める
def f(x):
    res = x
    for a, t in manu:
        if t == 1:
            res += a
        elif t == 2:
            res = max(res, a)
        else:
            res = min(res, a)

    return res

### マイナス付き二分探索するときの方法 ###

# 幅は2 * 10 ** 9
# 2 ** 32 - 1あれば十分 4294967296
# ある程度upperの値が大きいと数値を少し下げてもresの値は変わらない
upper = (2 ** 32) - 1 # 1111111111...
diff = 2 ** 31 # 調整用　十分2 * 10 ** 9より大きい
for i in range(31, -1, -1):
    if f(upper - diff) == f(upper - (2 ** i) - diff):
        upper -= 2 ** i

under = 0
for i in range(31, -1, -1):
    if f(under - diff) == f(under + (2 ** i) - diff):
        under += 2 ** i

upper -= diff
under -= diff
ans_under = f(under)
ans_upper = f(upper)
su = sum([i[0] for i in manu if i[1] == 1])

for q in que:
    # under以下であればf(under)
    if q <= under:
        print(ans_under)
    elif upper <= q:
        print(ans_upper)
    else:
        print(q + su)
