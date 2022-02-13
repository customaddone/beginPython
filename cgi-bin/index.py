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
eps = 10 ** (-15)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

"""
左にいくつかずらしてXをxorして揃える
ずらしてai ^ biして全て揃うかどうか
N^2かかるが、実際にxorしないとわからないか？　差分とか
kを1つ増やすと(B[i] ^ B[i - 1])がxorされる
ループさせていく中で全て一致するところはあるか

一桁ごとに分解して考えると
 110110
001      これが一致する場所を考える ロリハ
左回りなので逆に進める
"""

N = getN()
A = getList()[::-1]
B = getList()[::-1]

for i in range(2):
    a = ''.join(['1' if (A[j] & (1 << i)) > 0 else '0' for j in range(N)])
    a_rev = ''.join(['0' if (A[j] & (1 << i)) > 0 else '1' for j in range(N)])
    b = ''.join(['1' if (B[j] & (1 << i)) > 0 else '0' for j in range(N)])
    print(a)
    print(a_rev)
    b += b
    print(b)
