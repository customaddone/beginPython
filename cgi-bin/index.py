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
sys.setrecursionlimit(10000000)
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
inf = float('inf')
eps = 10 ** (-12)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

class Bitset:
    '''
        N:       bitの長さ
        add():   xビット目を1にする
        sub():   xビット目を0にする
        count(): 1となるビットの数を取得
        self[x]: xビット目を取得
        bit演算子 &, | 対応
    '''
    def __init__(self, N):
        self.bit_size = 63
        self.bits_size = (N + self.bit_size - 1) // self.bit_size
        self.bits = self.bits_size * [0]
        self.N = N

    def add(self, x):
        self.bits[x // self.bit_size] |= 1 << (x % self.bit_size)

    def sub(self, x):
        self.bits[x // self.bit_size] &= ~(1 << (x % self.bit_size))

    def count(self):
        cnt = 0
        for x in self.bits:
            c = (x & 0x5555555555555555) + ((x >> 1) & 0x5555555555555555)
            c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
            c = (c & 0x0f0f0f0f0f0f0f0f) + ((c >> 4) & 0x0f0f0f0f0f0f0f0f)
            c = (c & 0x00ff00ff00ff00ff) + ((c >> 8) & 0x00ff00ff00ff00ff)
            c = (c & 0x0000ffff0000ffff) + ((c >> 16) & 0x0000ffff0000ffff)
            c = (c & 0x00000000ffffffff) + ((c >> 32) & 0x00000000ffffffff)
            cnt += c

        return cnt

    def __and__(self, other):
        _bitset = Bitset(self.N)
        _bits = _bitset.bits
        for i in range(self.bits_size):
            _bits[i] = self.bits[i] & other.bits[i]

        return _bitset

    def __or__(self, other):
        _bitset = Bitset(self.N)
        _bits = _bitset.bits
        for i in range(self.bits_size):
            _bits[i] = self.bits[i] | other.bits[i]

        return _bitset

    def __xor__(self, other):
        _bitset = Bitset(self.N)
        _bits = _bitset.bits
        for i in range(self.bits_size):
            _bits[i] = self.bits[i] ^ other.bits[i]

        return _bitset

    def __getitem__(self, x):
        return self.bits[x // self.bit_size] >> (x % self.bit_size) & 1

N = getN()
bi = [Bitset(N) for i in range(N)]
for i in range(N):
    s = input()
    for j in range(i + 1, N):
        if s[j] == '1':
            bi[i].add(j)

ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        if bi[i][j] == 1:
            ans += (bi[i] & bi[j]).count()
print(ans)
