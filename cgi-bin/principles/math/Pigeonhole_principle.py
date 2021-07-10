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

# 鳩の巣原理
# 組み合わせの通りと比べてその取りうる値の種類が小さい時に使われる

"""
088 - Similar but Different Ways（★6）

二つの異なる部分集合を探す
条件1→条件2　or 条件2→条件1か
条件1→条件2は総和がkになる組み合わせを求めた後DPの復元が難しい　2^Nいる
条件2→条件1は条件Qを満たすのを求めるのが難しい

そもそも2^N通りをすべて出すのは無理では？
最適な方法で2つ構築していく

N <= 20ならできるか？計算量はN^2 * 2^Nぐらい
最大2^N通りの異なる総和が作れる
条件1→条件2をすることを考えると...
sum(A)が <= 8888なので結構denseじゃない？
この上限ならN <= 12で済むはず

鳩の巣原理
上限が小さければ意外と一回あたりの探索の量が少ない
"""

N, Q = getNM()
A = getList()
ng = [set() for i in range(N)]
for _ in range(Q):
    x, y = getNM()
    ng[x - 1].add(y - 1)
    ng[y - 1].add(x - 1)

su = sum(A)
L = [set()] * (su + 1)

for i in range(N):
    # 新しい集合を作る
    for j in range(su, -1, -1):
        if j > 0 and not L[j]:
            continue
        # ngがなく数字を書き込める
        if not (L[j] & ng[i]):
            # すでに存在していれば
            if L[j + A[i]]:
                # 古い集合、新しい集合
                prev, next = L[j + A[i]], L[j] | set([i])
                print(len(prev))
                print(*[i + 1 for i in prev])
                print(len(next))
                print(*[i + 1 for i in next])
                exit()
            else:
                L[j + A[i]] = L[j] | set([i])
