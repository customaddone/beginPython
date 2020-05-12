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
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
# list(map(int, input().split()))
mod = 10 ** 9 + 7

N, Q = getNM()
board = [0] * (N + 1)
boardalta = [0]
# ひっくり返す(+=1)何もしない(-=1)で累積和
for i in range(Q):
    l, r = getNM()
    board[l - 1] += 1
    # board[r + 1]より向こうは何も操作しない
    board[r] -= 1
for i in range(N):
    # 累積和の亜種
    if (boardalta[i] + board[i]) % 2 == 0:
        boardalta.append(0)
    else:
        boardalta.append(1)
# joinはlistでは使えないためmapでstrに
print(''.join(map(str, boardalta[1:])))
