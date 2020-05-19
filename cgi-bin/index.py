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
import fractions
import copy
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_B

N, X = getNM()
lista = [i for i in range(1, N + 1)]
dp = [[0] * (N + 1) for i in range(N)]
ans = 0

def rec_memo(i, plus, sum):
    global ans
    if i == N or plus == 3:
        if plus == 3:
            print([i, sum])
            ans += (sum == 0)
    elif sum < lista[i]:
        rec_memo(i + 1, plus, sum)
    else:
        rec_memo(i + 1, plus, sum)
        rec_memo(i + 1, plus + 1, sum - lista[i])
rec_memo(0, 0, X)
print(ans)
