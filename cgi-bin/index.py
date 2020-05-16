def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()

from collections import defaultdict, deque, Counter
from sys import exit
import heapq
import math
import copy
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

N = getN()
train = []

for i in range(N - 1):
    c, s, f = getNM()
    train.append([c, s, f])

# sta~Nまで行くのにかかる時間を求める関数
def gotowest(sta):
    # sta ~ sta + 1まで
    time = train[sta][0] + train[sta][1]
    # sta + 1~ Nまで
    for j in range(sta + 1, N - 1):
        if time <= train[j][1]:
            # もし到着した時間が一本目の列車が出発する前なら
            time = train[j][0] + train[j][1]
        else:
            # 最初の一本のその次の便(train[j][1] + train[j][2]分後出発)から数えてwait本目の列車に乗る
            wait = ((time - train[j][1]) + train[j][2] - 1) // train[j][2]
            time = train[j][1] + (train[j][2] * wait) + train[j][0]
    return time

ans = []
for i in range(N - 1):
    ans.append(gotowest(i))
# N~Nまで（０分）
ans.append(0)
for i in ans:
    print(i)
