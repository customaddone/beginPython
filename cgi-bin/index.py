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
def rand_N(ran1, ran2):
    return random.randint(ran1, ran2)
def rand_List(ran1, ran2, rantime):
    return [random.randint(ran1, ran2) for i in range(rantime)]
def rand_ints_nodup(ran1, ran2, rantime):
  ns = []
  while len(ns) < rantime:
    n = random.randint(ran1, ran2)
    if not n in ns:
      ns.append(n)
  return sorted(ns)

def rand_query(ran1, ran2, rantime):
  r_query = []
  while len(r_query) < rantime:
    n_q = rand_ints_nodup(ran1, ran2, 2)
    if not n_q in r_query:
      r_query.append(n_q)
  return sorted(r_query)

from collections import defaultdict, deque, Counter
from sys import exit
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

num = [2, 4, 6, 8]
limit = 10

def part_bitset1(num, limit):
    N = len(num)
    dp = 1 # 最初の0

    for i in range(N):
        dp |= (dp << num[i])

    return bin(dp)

max_diff = 30

def part_bitset2(num, limit):
    N = len(num)
    dp = 1 << max_diff # 最初の0
    print(bin(dp))

    for i in range(N):
        # +, -を加える
        dp |= (dp << num[i]) | (dp >> num[i])

    return dp

l = part_bitset2(num, limit)
ans = []
for i in range(l.bit_length()):
    if l & (1 << i):
        ans.append(i - max_diff)
# [-20, -18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# print(ans)

# ABC147 E - Balanced Path

MAX_DIFF = 80
h, w = getNM()

A = [getList() for i in range(h)]
B = [getList() for i in range(h)]
c = [[abs(A[i][j] - B[i][j]) for j in range(w)] for i in range(h)]

# bitset高速化
# 集合を010110...の形で持つ
sets = [[0 for j in range(w)] for i in range(h)]
# 中央0: 1 << MAX_DIFFに + c[0][0], - c[0][0]
sets[0][0] = (1 << MAX_DIFF + c[0][0]) | (1 << MAX_DIFF - c[0][0])

# 縦方向に進む
for i in range(1, h):
    # c[i][0]の+-を足したもの
    sets[i][0] |= (sets[i - 1][0] << MAX_DIFF + c[i][0]) | (sets[i - 1][0] << MAX_DIFF - c[i][0])
# 下方向に進む
for i in range(1, w):
    sets[0][i] |= (sets[0][i - 1] << MAX_DIFF + c[0][i]) | (sets[0][i - 1] << MAX_DIFF - c[0][i])
for i in range(1, h):
    for j in range(1, w):
        sets[i][j] |= (sets[i - 1][j] << MAX_DIFF + c[i][j]) | (sets[i - 1][j] << MAX_DIFF - c[i][j])
        sets[i][j] |= (sets[i][j - 1] << MAX_DIFF + c[i][j]) | (sets[i][j - 1] << MAX_DIFF - c[i][j])

# 終点の集合を見る
s = bin(sets[h - 1][w - 1] + (1 << (h + w) * MAX_DIFF))
min_diff = 1 << MAX_DIFF
for i in range(len(s)):
    if s[- 1 - i] == '1': # フラグが立っているなら判定
        min_diff = min(min_diff, abs(i - (h + w - 1) * MAX_DIFF))
print(min_diff)

# CODE FESTIVAL 2014 予選B C - 錬金術士

def ord_chr(array, fanc):
    if fanc == 0:
        res = [ord(s) - ord('A') for s in array]
        return res

    if fanc == 1:
        res = [chr(i + ord('a')) for i in array]
        res = ''.join(res)
        return res

"""
S1, S2からN文字なので、S1にパーツが全部揃っててもNG
S1からどのパーツを取ったら、残りをS2で取れるか
AABCCD
ABEDDA
EDDAAA の場合

S1: A * 2, B * 1, C * 2, D * 1
S2: A * 2, B * 1, D * 2, E * 1
S3: A * 3, D * 2, E * 1　がほしい
AについてはS1から1 ~ 2個（aとする)
BについてはS1から0 ~ 0個（bとする）...
DについてはS1から0 ~ 1個（dとする）個取ればいい
EについてはS1から0 ~ 0個(s2で全てカバー)
a + b +...+dがNになればいいのでdp部分和

下限: max(S3[i] - S2[i], 0) S2でカバーできない分
S1から出さないといけない　これを超えないとout
上限: min(S1[i], S3[i])

S1から文字A[i]をいくつとるかをdp
"""

S1 = ord_chr(input(), 0)
S2 = ord_chr(input(), 0)
S3 = ord_chr(input(), 0)
N = len(S1)

s1_table, s2_table, s3_table = [0] * 26, [0] * 26, [0] * 26

for i in range(N):
    s1_table[S1[i]] += 1
    s2_table[S2[i]] += 1
    s3_table[S3[i]] += 1

prev = 1 # 最初の0
# 部分和はbitset dpでやれる
for s1, s2, s3 in zip(s1_table, s2_table, s3_table):
    if s1 + s2 < s3:
        print('NO')
        exit()

    # あとはs1の個数を決めてdp
    # print(max(s3 - s2, 0), min(s1, s3))
    mi, ma = max(s3 - s2, 0), min(s1, s3)
    next = 0 # 選ばない選択もできるなら next = prevに変更
    for i in range(mi, ma + 1):
        next |= (prev << i)

    prev = next

# 集計　
res = []
for i in range(prev.bit_length()):
    if prev & (1 << i):
        res.append(i)

if N // 2 in set(res):
    print('YES')
else:
    print('NO')
