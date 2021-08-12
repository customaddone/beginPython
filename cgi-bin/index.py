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
            over = -heappop(self.MIN)
            self.mi_sum -= over
            under = heappop(self.MAX)
            self.ma_sum -= under
            heappush(self.MIN, -under)
            self.mi_sum += under
            heappush(self.MAX, over)
            self.ma_sum += over

    # 中央値が出てくる
    def val(self):
        return -self.MIN[0]

    # 中央値以下の数字、中央値以上の数字の個数と合計
    def val_sum(self):
        return len(self.MIN), len(self.MAX), self.mi_sum, self.ma_sum

Q = getN()
a = [getList() for i in range(Q)]
# (n + 1) // 2個目を見る
cnt, add = 0, 0
que = Median()
for q in a:
    if q[0] == 1:
        cnt += 1
        add += q[2]
        que.add(q[1])
    else:
        med = que.val()
        nu, no, su_u, su_o = que.val_sum()
        print(med, nu * med - su_u + su_o - no * med + add)
