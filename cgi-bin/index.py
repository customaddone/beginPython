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
convict = [[] for _ in range(N)]
for i in range(N):
    a = getN()
    for j in range(a):
        x, y = getNM()
        convict[i].append([x - 1, y])
ans = 0
# 状態を生成
for bit in range(1 << N):
    flag = True
    # 人iの証言について
    for i in range(N):
        # 正直者のフラグが立っていれば
        if bit & (1 << i):
            for j in convict[i]:
                # もし正直者が行ったことに間違いがあれば
                if j[1] == 0 and bit & (1 << j[0]) > 0:
                    flag = False
                if j[1] == 1 and bit & (1 << j[0]) == 0:
                    flag = False
    if flag:
        index = str(bin(bit)).count('1')
        ans = max(ans, index)
print(ans)
