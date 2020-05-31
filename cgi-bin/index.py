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
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

N, K = 14, 2
S = "11101010110011"

flag = S[0]
sta = 1
lista = []

for i in range(1, N):
    if flag != S[i]:
        # flag(0か1か), sta(どこから続いているか), i(最終的にどこまで続いたか)
        lista.append([flag, sta, i])
        flag = S[i]
        sta = i + 1
lista.append([flag, sta, N])

print(lista)
