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
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
inf = float('inf')
eps = 10 ** (-15)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

"""
順列内の連続するK個の最大値
目指す最大値がiである場合、区間の左の端っこはi-K+1 ~ i
つまりiを置くとi-K+1 ~ iまでが確定する
N=7, K=3
A = [?, ?, ?, ?, ?, ?, ?]
val = [?, ?, ?, ?, ?, '0', '0'] N-K+1個
下から順番に上書きしていく
1, 7, 2, 4, 5, 3, 6の場合
[1, ?, ?, ?, ?, '0', '0']
[2, 2, 2, ?, ?, '0', '0']
[2, 2, 2, 3, 3, 3, '0']
[2, 4, 4, 4, 3, 3, '0']
[2, 4, 5, 5, 5, 3, '0']
[2, 4, 5, 5, 6, 6, 6]
[7, 7, 5, 5, 6, 6, 6]

上書きされたら消していくのは？　確率は均等
塗る部分で後から上書きされない条件は？
jについてj~j+K-1までに自身より大きいやつがない
v=5であれば     ここ
[1, 7, 2, 4, 5, 3, 6]
[7, 7, 5, 5, 6, 6, 6]
　　　　[      ]
          [      ]
             [      ]
全て既に塗られている　の個数
[      ]が全て塗られている確率は
N-KCv-1-(K-1)
今の時点で全て塗られてるならプラス
[1, ?, 2, 4, 5, 3, ?] 以下の数字が連続する確率
前後に何個の数字が連続するか　その期待値
[1, 7, 2, 4, 5, 3, 6]
[       ]
    [      ]
       [      ]...

それぞれ連続して置かれている確率
端っこにある場合チャンスは少ないmax(0, i-K+1) ~ min(i, N-K)の間
i=0 チャンスは1回
i=2 チャンスは2回...
1, 2, 3, 3, 3
3, 3, 3, 2, 1...みたいに

N = 8
sum = N
for k in range(1, N):
    print(sum)
    sum += max(0, (N - 2 * k))
K個全てが塗られている確率
"""

N = 3
sum = N
for k in range(1, N + 1):
    print(sum)
    sum += (N - 2 * k)
