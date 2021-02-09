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

# N進数
n = 12
list = []
digit = 7
i = 0

while n != 0:
    list.insert(0, str(n % digit))
    n //= digit
    i += 1
print(''.join(list))

# 文字列２進数を整数に変換
print(int('010100', 2))

# nを超えない最大のbase ** mは何か
def max_pow(n, base):
    if n == 0:
        return None
    opt = 1
    cnt = 0
    while base ** (cnt + 1) <= n:
        opt *= base
        cnt += 1
    return opt, cnt

# (16, 4)
print(max_pow(27, 2))

# 任意の整数で割り続ける
def spliter(n, split):
    splited = n
    cnt = 0

    while splited % split == 0:
        if splited == 0:
            break
        splited //= split
        cnt += 1
    # print(cnt)
    return splited, cnt

# (3, 4)
print(spliter(48, 2))

# -2進数（いるこれ？）
def minus_digit(rev_n):
    if rev_n == 0:
        print('0')
        return

    cnt = 0
    rep = rev_n
    lista = []

    while rep != 0:
        split = (abs(rep) % 2 ** (cnt + 1)) // 2 ** cnt
        if split == 0:
            lista.append(0)
        else:
            lista.append(1)
        rep -= (split * ((-2) ** cnt))
        cnt += 1
    lista.reverse()
    return''.join(map(str, lista))

# 11100
print(minus_digit(12))

# 1(1), 2(1 + 2), 3(1 + 2 + 3)...を超えられるか
def factime(ny):
    cnt = 1
    sum = 0
    while True:
        if sum + cnt > ny:
            return cnt - 1
            break
        sum += cnt
        cnt += 1
# 2
print(factime(2))
