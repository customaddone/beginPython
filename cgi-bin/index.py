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

#############
# Main Code #
#############

"""
転倒数を操作する
[1, 2, 3, 4, 5]:転倒数0
[5, 1, 2, 3, 4]:転倒数4
[3, 1, 2, 4, 5]:転倒数2
[5, 4, 1, 2, 3](5と4を前方に):転倒数4 + 5 = 9
転倒数5 * (5 - 1) // 2 = 10までは行内を入れ替えることで対応できる

[1, 2, 3, 4, 5]
[6, 7, 8, 9, 10]
[11, 12, 13, 14, 15] 転倒数0

[11, 12, 13, 14, 15]
[1, 2, 3, 4, 5]
[6, 7, 8, 9, 10] 転倒数2 * 5 = 10

Mの倍数分については行ごと入れ替え、残りについては行内を入れ替える

1 ~ (N - 1)までを使って数字Kを作ろう
1 ~ 15までを使って数字Kを作ろう
def assem(n, k):
    cnt = n * (n + 1) // 2
    use = []
    left = [] # 一つ目は転倒させても意味ないので
    for i in range(n, 0, -1):
        if cnt - i >= k:
            cnt -= i
            left.append(i)
        else:
            use.append(i)

    return use, left
"""

# 1 ~ Nまでを使って数字Kを作ろう
def assem(n, k):
    cnt = n * (n + 1) // 2
    use = []
    left = [1] # 一つ目は転倒させても意味ないので
    for i in range(n, 0, -1):
        if cnt - i >= k:
            cnt -= i
            left.append(i + 1)
        else:
            use.append(i + 1)
    left.sort()
    return use, left

N, M, K = getNM()
# 行の入れ替え
# 上限は行全てを全転倒させるN * (N - 1) // 2
c_row = min(K // M, N * (N - 1) // 2)
K -= M * c_row
# i行について全転倒させる
# M = 1の場合に注意
c_inner = 0
if M > 1:
    c_inner = K // (M * (M - 1) // 2)
K -= (M * (M - 1) // 2) * c_inner
left = K

# どの行を転倒させるか
row_fore, row_aft = assem(N - 1, c_row)
row = row_fore + row_aft

# 全転倒
row_rev = [i + 1 for i in range(M - 1, -1, -1)]

# c_inner + 1行目の順番
inner_bef, inner_aft = assem(M - 1, left)
last = inner_bef + inner_aft

maze = [[0] * M for i in range(N)]
for i in range(N):
    for j in range(M):
        # 行内の要素について
        # 全転倒
        if i <= c_inner - 1:
            maze[i][j] = (row[i] - 1) * M + row_rev[j]
        # 少し転倒
        elif i == c_inner:
            maze[i][j] = (row[i] - 1) * M + last[j]
        # 順番のまま
        else:
            maze[i][j] = (row[i] - 1) * M + (j + 1)

for i in maze:
    print(*i)
