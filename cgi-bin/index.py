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

n = getNM()
cc = []
ss = []
ff = []
for i in range(n - 1):
    c, s, f = getList()
    cc.append(c)
    ss.append(s)
    ff.append(f)
for l in range(n - 1):
    ans = ss[l] + cc[l]
    for k in range(l + 1, n - 1):
        temp = ss[k]
        while temp < ans:
            temp += ff[k]
        ans = temp + cc[k]
    print(ans)
print(0)
