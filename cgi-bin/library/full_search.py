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

# bit全探索
# 計算量: (2 ** N) * N
N = 5
for bit in range(1 << N):
    # bitの「右から」何番目にフラグが立っているか数える
    for j in range(N):
        if bit & (1 << j):
            print(bin(bit), j)
    # bitの本数を数える
    print(bin(bit), bin(bit).count('1'))

# itertools系
# 0 ~ power - 1までの数字がpower ** exponent個出る
def power_func(power, exponent):
    def child_pow(i, array):
        global cnt
        if i == exponent:
            print(array) # ここに何か操作を入れる
            return
        for j in range(power):
            new_array = array + [j]
            child_pow(i + 1, new_array)

    child_pow(0, [])

power_func(4, 2)

# 0 ~ n - 1までのうちr個取ってくれる
def comb_pow(n, r):
    def child_pow(i, array):
        global cnt
        if i == r:
            print(array)
            return

        last = -1
        if len(array) > 0:
            last = array[-1]

        for j in range(last + 1, n):
            new_array = array + [j]
            child_pow(i + 1, new_array)

    child_pow(0, [])

comb_pow(4, 2)

# 0 ~ n - 1までのうち重複を許して個取ってくれる
def rep_comb_pow(n, r):
    def child_pow(i, array):
        global cnt
        if i == r:
            print(array)
            return

        last = -1
        if len(array) > 0:
            last = array[-1]

        for j in range(last, n):
            new_array = array + [j]
            child_pow(i + 1, new_array)

    child_pow(0, [])

rep_comb_pow(4, 2)
