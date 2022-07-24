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
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
inf = float('inf')
eps = 10 ** (-12)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

#### a >= bかな？　全順序ならマージソートできる ######
def a_bigger(a, b):
    return a >= b

# 同じかな？
def equal(a, b):
    return a[0] * b[1] - a[1] * b[0] == 0
###############################################

# マージソート + 転倒数
def merge_sort(x):
    retary = []
    res_rev = 0
    if len(x) <= 1:
        retary.extend(x)
    else:
        m = len(x) // 2
        # 逆にする
        f, s = merge_sort(x[:m]), merge_sort(x[m:])
        first, rev1 = f[0][::-1], f[1]
        second, rev2 = s[0][::-1], s[1]
        res_rev += (rev1 + rev2)
        while len(first) > 0 and len(second) > 0:
            # 小さい方を取り出してappendする
            if a_bigger(first[-1], second[-1]):
                retary.append(second.pop())
                res_rev += len(first)
            else:
                retary.append(first.pop())
        # 元に戻して繋げる
        retary.extend(first[::-1] if len(first) > 0 else second[::-1])

    return retary, res_rev

N = getN()
print(merge_sort(getList())[1])
