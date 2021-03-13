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

class BIT:
    def __init__(self, N):
        self.N = N
        self.bit = [0] * (N + 1)
        self.b = 1 << N.bit_length() - 1

    def add(self, a, w):
        x = a
        while(x <= self.N):
            self.bit[x] += w
            x += x & -x

    def get(self, a):
        ret, x = 0, a - 1
        while(x > 0):
            ret += self.bit[x]
            x -= x & -x
        return ret

    def cum(self, l, r):
        return self.get(r) - self.get(l)

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
        return x + 1

"""
T個のテストケースについて答えましょう
(Nの総和は2 * 10 ** 5を超えない)
できれば全てのラクダについて最大値の方を選択したい
愚直にやればN!
以内にいる時　ヒープキュー愚直とか
ソートはする
L - Rのdiffを保持する
これが大きい順にしたい
ただし賞味期限があるのでそれを考慮したい
各L - Rについて都合がつくように並べる
期限が迫っているものから置いていく
プラスとマイナスに分ける
プラスのもの　できるなら置きたい　マイナスのもの（期限がない）　できるなら置きたくない
プラスのものが存在するならプラスのものをおく　そうでなければ嫌々マイナスのものをマイナスが小さい順に置く
プラスのものの選び方

マイナスのものは期限がすぎると反転させた値で確定する　これは一番後ろに置いていい
プラスが大きいものから順に探索していく
期限ギリギリに置く　置けない場合はその前に置く
逆にマイナスの方にもリミットはある
"""

N = getN()
K = []
for i in range(N):
    k, l, r = getList()
    # l - rは反転させている
    heappush(K, [r - l, k, l, r])

bit = BIT(N) # 最寄りの空いている場所を探す
for i in range(N):
    bit.add(i + 1, 1)

for i in range(N):
    diff, lim, ok, ng = heappop(K)
    # bit.get(lim + 1)になる点、つまりlim + 1地点よりフラグが1小さくなる地点を探す
    flag = bit.get(lim + 1)
    if flag:
        index = bit.lowerbound(flag)
        bit.add(index, -1)
    else:
        index = float('inf')
    # print(index, diff, lim, ok, ng)
