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

# ABC127 F - Absolute Minima

"""
基礎ポイントはb
愚直は a b大きいな
クエリに対してlogNぐらいで求めたい
次々と|x - a|が立っていく　
|x - a|に近づけると小さくなる
つまりsum(aとの差) + bが答え
なるべく真ん中に置けばいいと思うけど
aが2つの場合はa1 ~ a2のどれ選んでもいい
aが3つの場合は？
a1    a2   a3 三分探索したいが
a1 ~ a2間にpがある場合　右に動かすことで減らせる
小さい方から(aの数 + 1) // 2番目に置けばOK ヒープ使えばできるはず
値の求め方　BITでも使うか 合計なのでBITで間に合う
中央値をpとすると
左側の値 p * n - sum
右側の値 sum(p以降) - p * n
右側、左側で考える

1こ 1
2こ 1
3こ 2
4こ 2
5こ 3
"""

MIN = []
MAX = []
ans = 0
value = 0

Q = getN()
for i in range(Q):
    q = getList()

    if q[0] == 1:
        ans += q[2] # bを足す
        heappush(MIN, q[1]) # 右半分
        heappush(MAX, -q[1]) # 左半分　マイナスつける

        if MIN[0] < -MAX[0]: # オーバーすれば
            x = heappop(MIN) # 最小値
            y = -heappop(MAX) # 最大値

            value += (y - x)
            heappush(MIN, y) # 反対側に入れる
            heappush(MAX, -x)

    else:
        print(-MAX[0], ans + value)
