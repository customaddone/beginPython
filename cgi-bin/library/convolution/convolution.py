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

from cmath import pi, exp
def _fft(a, h):
    root = [exp(2.0j * pi / 2 ** i) for i in range(h + 1)]
    for i in range(h):
        m = 1 << (h - i - 1)
        for j in range(1 << i):
            w = 1
            j *= 2 * m
            for k in range(m):
                a[j + k], a[j + k + m] = \
                    a[j + k] + a[j + k + m], (a[j + k] - a[j + k + m]) * w
                w *= root[h - i]


def _ifft(a, h):
    iroot = [exp(-2.0j * pi / 2 ** i) for i in range(h + 1)]
    for i in range(h):
        m = 1 << i
        for j in range(1 << (h - i - 1)):
            w = 1
            j *= 2 * m
            for k in range(m):
                a[j + k], a[j + k + m] = \
                    a[j + k] + a[j + k + m] * w, a[j + k] - a[j + k + m] * w
                w *= iroot[i + 1]
    n = 1 << h
    for i in range(n):
        a[i] /= n

# 各kについて
# sum([A[i] * B[k - i]])をNlogNで計算する
def fft_convolve(a, b):
    n = 1 << (len(a) + len(b) - 1).bit_length()
    h = n.bit_length() - 1
    a = list(a) + [0] * (n - len(a))
    b = list(b) + [0] * (n - len(b))

    _fft(a, h), _fft(b, h)
    a = [va * vb for va, vb in zip(a, b)]
    _ifft(a, h)
    return [int(abs(val) + 0.5) for val in a]

# 使い方 codeforces Educational Codeforces Round 108 (Rated for Div. 2)
# D. Maximum Sum of Products
# 配列Aの連続部分列を反転させることができる
# sum(A[0] * B[0] + A[1] * B[1] +...)の最大値を求める

N = getN()
A = getList()
B = getList()

base = [0]
for i in range(N):
    base.append(base[-1] + A[i] * B[i])

ans = base[-1]
for i in range(N):
    a = [0] + A[i:]
    b = [0] + B[i:]

    fft = fft_convolve(a, b)
    # [i, j]を交換する　fftのj + 2を見る
    for j in range(N - i):
        opt = base[i] + (base[N] - base[i + j + 1]) + fft[j + 2]
        ans = max(ans, opt)

print(ans)
