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
info = []
for i in range(N):
    x, y, h = getNM()
    info.append([x, y, h])
info.sort(reverse = True,key = lambda info:info[2])

ans = []
for i in range(101):
    for j in range(101):
        height = -1
        flag = True
        for k in range(N):
            minusx = abs(i - info[k][0])
            minusy = abs(j - info[k][1])
            if height == -1:
                # 上で逆順にソートしてるので確実に１以上の高さがでる
                height = info[k][2] + minusx + minusy
            else:
                # 問題の式に沿うように
                if info[k][2] != max(height - minusx - minusy, 0):
                    flag = False
                    break
        if flag:
            ans = [i, j, height]
print(*ans)
