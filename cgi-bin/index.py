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

"""
XとYを分割するんだろ
X方向のみ　Yは変動なし
もともとのdiffの分だけ
LとRのみの場合は
頂点が2つの場合を考える
互いに近づいて行くなら最も近づいた時
遠ざかるなら0秒地点で
頂点3つR L L の場合
Rが一番右にある場合は0秒地点で止める
左、中にある場合は二つのLの差になる
R R L L の場合は
Rが一番右にいる場合は0秒地点
Lが一番左にいる場合も0秒地点
R L R Lとかの場合は互いが近づき合う
Rで挟む場合0秒地点
R L
0 1　とかの場合は一秒後は　1 0になる 0.5秒とかでもいい

動くものの下限と上限を持っておけばいい
steadyなラインを考えて
３分探索にならなそう
A * Bの掛け算を小さくすることを考える

最小値の候補
0秒地点
地点がいくつかあるので地点ごとに計算して求める
"""
