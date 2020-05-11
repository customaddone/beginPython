def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

from collections import defaultdict, deque
from sys import exit
import heapq
import math
import copy
from bisect import bisect_left

import sys
# sys.setrecursionlimit(1000000)
# list(map(int, input().split()))
mod = 10 ** 9 + 7
# https://atcoder.jp/contests/abc141/tasks/abc141_d

N,M = getNM()
# mapをlambdaで改造
A = list(map(lambda x:int(x) * (-1), input().split())) #-1倍してからリストに格納
heapq.heapify(A) #優先度付きキューに変換

for _ in range(M):
    max_value = heapq.heappop(A) * (-1) #最大値の取得
    heapq.heappush(A, (max_value // 2) * (-1)) #半額にして-1倍してからキューに戻す

print((-1)*sum(A)) #最後に-1倍を忘れずに
