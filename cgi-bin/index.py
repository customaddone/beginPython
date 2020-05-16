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
V = getList()

# 条件を満たすもののうちで最も多く現れる多い２数を採用する方針
even = [0] * (10 ** 5 + 1)
odd = [0] * (10 ** 5 + 1)
for i in range(N):
    if i % 2 == 0:
        even[V[i]] += 1
    else:
        odd[V[i]] += 1
# 偶数列、奇数列に現れる数字の中で一番多かったもの
topeven = even.index(max(even))
topodd = odd.index(max(odd))
even.sort()
odd.sort()

ans = 0
if topeven == topodd:
    # 偶数列で一番多かった数、奇数列で２番目に多かった数
    opt1 = N - even[-1] - odd[-2]
    # 偶数列で２番目に多かった数、奇数列で一番多かった数
    opt2 = N - even[-2] - odd[-1]
    # どちらか小さい方
    ans = min(opt1, opt2)
else:
    ans = N - even[-1] - odd[-1]
print(ans)
