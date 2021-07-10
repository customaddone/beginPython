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
sys.setrecursionlimit(10000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# 座圧BIT
class Comp_BIT:
    def __init__(self, N, array):
        self.N = N
        self.bit = [0] * (N + 1)
        self.b = 1 << N.bit_length() - 1
        # 座圧 1-indexで
        s = set(array)
        s = sorted(list(s))
        self.alter = {}
        self.rev = {}
        for i in range(len(s)):
            self.alter[s[i]] = i + 1
            self.rev[i + 1] = s[i]

    def add(self, a, w):
        x = self.alter[a]
        while(x <= self.N):
            self.bit[x] += w
            x += x & -x

    # [0, a)の合計
    def get(self, a):
        ret, x = 0, self.alter[a] - 1
        while(x > 0):
            ret += self.bit[x]
            x -= x & -x
        return ret

    # [0, a]（閉区間）の合計
    def get_rig(self, a):
        ret, x = 0, self.alter[a]
        while(x > 0):
            ret += self.bit[x]
            x -= x & -x
        return ret

    # [l, r)の合計
    def cum(self, l, r):
        return self.get(r) - self.get(l)

    # 最も近くにあるフラグの立っている場所を探す
    def lowerbound(self, w):
        if w <= 0:
            return 0
        x = 0
        k = self.b
        while k > 0:
            if x + k <= self.N and self.bit[x + k] < w:
                w -= self.bit[x + k]
                x += k
            k //= 2
        return self.rev[x + 1]

"""
[0, a)までの転倒数　求められる
[1, a)の転倒数は？
0番目の数字について、a)までの数字の中で自分より小さい数字の個数を引く
bit = BIT(N + 1)
cnt = 0
for i in range(1, N + 1):
    cnt += i - 1 - bit.get(A[i] + 1)
    bit.add(A[i], 1)
    print(cnt)
"""

N, K = getNM()
A = getList()

bit = Comp_BIT(N + 1, A)
cnt = 0
for i in range(N):
    cnt += i - bit.get_rig(A[i])
    bit.add(A[i], 1)
    print(cnt)
