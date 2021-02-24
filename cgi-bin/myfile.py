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

"""
K = 3なら
1 4 9(爆心地) 4 1という風にダメージを受ける　これは固定
これは好きな回数できる

まず最初の1つを落とせるか　2番目を落とせるか...をやっていく
これは必ず1でやらないといけない
1 4 10 9 14 13 5 1
1 4  9 4  1
0 0  1 5 13 13 5 1
     1 4  9  4 1
0 0  0 1  4  9 4 1
K ~ N - K + 1番目までこの方法でやって全て0になるか

足し合わせが面倒そう
blastした位置を保存しておくと？　毎回ごとに計算できない？
i番目のモンスターの体力を0にしたい
残り体力はAi - (これまでのダメージ)
与えるダメージが平均であれば簡単なんだけど
二乗しなければ　これまでのblast位置の合計 - 現在の地点
二乗すると
0 0  1 5 13 13 5 1 blast位置は3
i = 2について
(K - (y - x))**2 = (K**2 - 2Ky + y**2) + (x**2 + 2Kx) - 2yx
squに収納 K**2 - 2Ky + y**2
minusに収納 -2y
後で計算 x**2 + 2Kx
2yをどこかに保持する　あとで
squ = 0
minus = 0
3にblast
squ = [9]
minus = [-6]
i = 2の計算
通りすぎたら引く

全部足せばOK
爆心地がyの時xの相手に与えるダメージ
def cal_squ(y):
    return K ** 2 - (2 * K * y) + y ** 2
def cal_x(x):
    return x ** 2 + 2 * K * x
def minus(y):
    return -2 * y
print(cal_squ(5), cal_x(5), minus(5) * 5)
逆側はどうなっている？
"""

N, K = getNM()
A = getList()
def cal_squ(y):
    return K ** 2 - (2 * K * y) + y ** 2
def cal_x(x):
    return x ** 2 + 2 * K * x
def minus(y):
    return -2 * y

squ = 0
minus = 0
blast = deque([])
for i in range(N - K + 1):
    # A[i]回blast
    blast.append([i + K - 1, A[i]])
    squ += cal_squ(i + K - 1) * A[i]
    minus += minus()
