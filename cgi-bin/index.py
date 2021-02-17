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

def check(n, s, k, base, alp):
    power = [1] * (N + 1)
    # 部分文字列を数字に
    # ハッシュ生成
    for i in range(1, N + 1):
        power[i] = power[i - 1] * base % mod

    res = 0
    # 頭m文字のハッシュ生成
    for i in range(k):
        res += s[i] * power[k - i - 1]
        res %= mod
    dic = {res: 0}
    for i in range(N - k):
        # ハッシュをローリングしていって次々m文字のハッシュを生成していく
        res = ((res - s[i] * power[k - 1]) * base + s[i + k]) % mod
        # もし既出なら
        if res in dic.keys():
            index = dic[res]
            if index + k <= i + 1: # 重ならないか
                return True
        else:
            dic[res] = i + 1 # i + 1:頭の位置を記録する

    return False

def rolling_hash(n, s, m):
    s = list(map(ord, s)) # pythonは遅いので

    res = True
    # 原子根を適当に手動で乱択してね
    for base in [161971, 167329, 191911]:
        # アルファベットをランダムに並べた表でエンコード表を作る
        for alp in ['qwertyuioplkmnjhbvgfcdxsaz','qazxcsdwertfgvbnmhjyuioklp']:
            # これ一回の計算量はO(N)
            res &= check(n, s, m, base, alp)
    return res

N, M = getNM()
S = input()

if rolling_hash(N, S, M):
    print('YES')
else:
    print('NO')
