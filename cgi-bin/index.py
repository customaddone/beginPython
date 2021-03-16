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
まず
ルンルンの渡すコインの種類と数を考える
y // An 枚渡す
y %= An する
y // An-1 枚渡す
y %= An-1 する...

y - Xも同様
yとy - Xで同じコインが使われてはならない
二進数の 1001(9)と0110(6)みたいな感じ X = 3の時条件を満たす
互いに背反な要素を2つ作ればいい
ルンルンの渡したコインは崩されないといけない（上限）

最小枚数で渡す Ai * コインの枚数 < Ai+1でないといけない
1 5 10の場合、渡せる5のコインは1まいだけ
Xの上位貨幣An(X <= Anとなる)について 渡せるのは1枚だけ
2枚以上渡すと...

X = 10 An = 10の場合
1枚でぴったし 2枚だと1枚帰ってくるのでNG 一枚使ったらそれ以上の上位貨幣は使えない
Anを逆からdpしていく
3, 9
1 5 10の場合
10: 0 ~ 1枚だけ　上位貨幣なので
5: 0 ~ 1枚 (10 - 1) // 5
1: 0 ~ 4枚
合計で0 ~ 19まで表現できる　ここから絞る dpやろなぁ
桁dpっぽい
各場所で0の部分と1 ~ 枚のところを
yのAi桁部分が0, yのAi桁部分が1~　の桁dpになる
"""

N, X = getNM()
A = getList()
A.sort(reverse = True)
L = [1] * N
sta = 0 # 最大貨幣の場所
alt = [0] * N

for i in range(1, N):
    if X <= A[i]:
        sta = i
    L[i] = (A[i - 1] - 1) // A[i]
# 換算
x = X
for i in range(N):
    alt[i] = x // A[i]
    x %= A[i]
