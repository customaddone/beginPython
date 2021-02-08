from collections import defaultdict, deque, Counter
import sys
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce, lru_cache
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

# 全探索

# 全ての条件をクリアできるものの個数を調べる
# 三井住友信託銀行プログラミングコンテスト2019 D - Lucky PIN

N = 19
S = '3141592653589793238'

# 種類数は最大1000個(000 ~ 999)それらについて全探索
# それぞれの候補targetについて条件が3つある
# 1: target[0]がある
# 2: 1の後ろにtarget[1]がある
# 3: 2の後ろにtarget[2]がある
# いくつ条件をクリアしたかcntで管理する
ans = 0
for i in range(1000):
    target = str(i).zfill(3) # 3桁になるよう桁埋め
    cnt = 0
    for j in range(len(S)):
        if target[cnt] == S[j]:
            cnt += 1
        if cnt == 3:
            ans += 1
            break

print(ans)
