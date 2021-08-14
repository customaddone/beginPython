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

# 集合の中央値を求める　各操作につきlogN
# multiset使わずにできるように
class Median():
    from heapq import heappop, heappush
    def __init__(self):
        self.MIN, self.MAX = [], []
        self.total = 0
        self.mi_sum, self.ma_sum = 0, 0

    def add(self, x):
        self.total += 1
        # 足りない場合
        if len(self.MIN) < (self.total + 1) // 2:
            heappush(self.MIN, -x) # 小さい方に
            self.mi_sum += x
        else:
            heappush(self.MAX, x) # 大きい方に
            self.ma_sum += x
        # 常にMINの最大値 < MAXの最小値になるように保つ
        if self.MAX and -self.MIN[0] > self.MAX[0]:
            self.mi_sum += (self.MAX[0] - (-self.MIN[0]))
            self.ma_sum += (-self.MIN[0] - self.MAX[0])
            heappush(self.MIN, -heappop(self.MAX))
            heappush(self.MAX, -heappop(self.MIN))

    # 中央値が出てくる
    def val(self):
        return -self.MIN[0]

    # 中央値以下の数、中央値以上の数の個数と合計
    def val_sum(self):
        return len(self.MIN), len(self.MAX), self.mi_sum, self.ma_sum
