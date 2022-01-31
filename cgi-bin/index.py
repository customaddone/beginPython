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
eps = 10 ** (-15)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# ここの設定を変えて使う
#####segfunc#####
def segfunc(x, y):
    return (min(x[0], x[1] + y[0]), x[1] + y[1])
#################

#####ide_ele#####
ide_ele = (0, 0)
#################

class SegTree():
    def __init__(self, n, op, e, v = None):
        """演算子,単位元,データ数,初期値"""
        self._n = n
        self._op = op
        self._e = e
        self._log = (n-1).bit_length()
        self._size = 1<<self._log
        self._d = [self._e]*(self._size*2)
        if v is not None:
            for i in range(self._n):
                self._d[self._size+i]=v[i]
        for i in range(self._size-1,0,-1):
            self._update(i)

    def set(self,p,x):
        """一点更新(p番目の値をxに)"""
        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self,p):
        """p番目の値"""
        return self._d[p+self._size]

    def prod(self,l,r):
        """区間取得[l,r)"""
        sml,smr=self._e,self._e
        l+=self._size
        r+=self._size
        while l < r:
            if l&1:
                sml = self._op(sml,self._d[l])
                l+=1
            if r&1:
                r-=1
                smr = self._op(self._d[r],smr)
            l>>=1
            r>>=1
        return self._op(sml,smr)

    def all_prod(self):
        """全区間での演算結果"""
        return self._d[1]

    def max_right(self, l, f):
        """単調性のある関数fがf(prod(l,r))=True となる最大のr"""
        if l==self._n:return self._n
        l += self._size
        sm = self._e
        while True:
            if l%2==0:l>>=1
            if not f(self._op(sm,self._d[l])):
                while l<self._size:
                    l<<=1
                    if f(self._op(sm,self._d[l])):
                        sm = self._op(sm,self._d[l])
                        l+=1
                return l-self._size
            sm = self._op(sm,self._d[l])
            l+=1
            if (l&-l)==l:break
        return self._n

    def min_left(self,r,f):
        """単調性のある関数fがf(prod(l,r))=True となる最小のl"""
        if r == 0: return 0
        r += self._size
        sm = self._e
        while True:
            r -= 1
            while r > 1 and r % 2: r >>= 1
            if not f(self._op(self._d[r], sm)):
                while r < self._size:
                    r = 2 * r + 1
                    if f(self._op(self._d[r], sm)):
                        sm = self._op(self._d[r], sm)
                        r -= 1
                return r + 1 - self._size
            sm = self._op(self._d[r], sm)
            if r & -r == r: break
        return 0

    def _update(self,k):
        self._d[k]=self._op(self._d[2*k],self._d[2*k+1])

    def _update(self,k):
        self._d[k]=self._op(self._d[2*k],self._d[2*k+1])

"""
(累積和の最小値、累積和)を持ち、
def segfunc(x, y):
    return (min(x[0], x[1] + y[0]), x[1] + y[1])
とすると
区間aと区間bをマージするとき、a[1](aの累積和)からスタートし、
bに入ると途中a[1] + b[0](bの最小地点)を通るのでそこがマイナスでないか

セグ木で前からの累積和の最小値がわかる
"""

N, Q = getNM()
S = [(0, 1) if s == '(' else (-1, -1) for s in input()]
seg = SegTree(N, segfunc, ide_ele)
for i in range(N):
    seg.set(i, S[i])

for _ in range(Q):
    d, l, r = getNM()
    l -= 1
    r -= 1
    if d == 1:
        S[l], S[r] = S[r], S[l]
        seg.set(l, S[l])
        seg.set(r, S[r])
    else:
        if seg.prod(l, r + 1) == (0, 0):
            print('Yes')
        else:
            print('No')
