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
mod = 998244353

#############
# Main Code #
#############

# ABC114 C - 755
N = getN()
rength = len(str(N))
numlist = [3, 5, 7]
cnt = 0

def sevfivthr(i, strint):
    global cnt
    if i == rength:
        return
    else:
        for num in numlist:
            newstr = strint + str(num)
            if ('3' in newstr) and ('5' in newstr) and ('7' in newstr):
                if int(newstr) <= N:
                    cnt += 1
            sevfivthr(i + 1, newstr)
for i in numlist:
    sevfivthr(1, str(i))
print(cnt)

# ABC115 D - Christmas
# レベルNバーガーの下からX層目まで
N, X = getNM()

# レベルNバーガーの中間地点、全体のサイズ
cnt_burger = [[0 for i in range(2)] for i in range(51)]
cnt_burger[0] = [1, 1]
for i in range(1, 51):
    cnt_burger[i][0] = 1 + cnt_burger[i - 1][1] + 1
    cnt_burger[i][1] = cnt_burger[i][0] + cnt_burger[i - 1][1] + 1

# レベルNバーガーにパティが何枚含まれる？
cnt_patty = [0] * 51
cnt_patty[0] = 1
for i in range(1, 51):
    cnt_patty[i] = 2 * cnt_patty[i - 1] + 1

# レベルNの下からX番目までにパティが何枚含まれるか
# xが大きいのでdpはできない
def count(n, x):
    # レベル0バーガーの場合
    if n == 0 and x == 1:
        return 1

    # バーガーの一番下のパンのみ食べる場合
    if x == 1:
        return 0

    # 中間地点以前のどこかまで食べる場合
    elif 1 < x < cnt_burger[n][0]:
        # レベルn - 1バーガーの下からx - 1層目まで
        return count(n - 1, x - 1)

    # 中間地点まで食べる
    elif x == cnt_burger[n][0]:
        return cnt_patty[n - 1] + 1

    # 中間地点 ~ 最後以前のうちのどこか
    elif cnt_burger[n][0] < x < cnt_burger[n][1]:
        return cnt_patty[n - 1] + 1 + count(n - 1, x - cnt_burger[n][0])

    # 最後
    else:
         return 2 * cnt_patty[n - 1] + 1

print(count(N, X))

# ABC122 D - We Like AGC 
N = getN()
memo = [{} for i in range(N + 1)]
def ok(last4):
    for i in range(4):
        t = list(last4)
        if i >= 1:
            t[i - 1],t[i] = t[i], t[i - 1]
        if ''.join(t).count('AGC') >= 1:
            return False
    return True
def dfs(cur, last3):
    if last3 in memo[cur]:
        return memo[cur][last3]
    if cur == N: return 1
    res = 0
    for c in 'ACGT':
        if ok(last3 + c):
            res  = (res + dfs(cur + 1, last3[1:] + c)) % mod
    memo[cur][last3] = res
    return res
print(dfs(0,'TTT'))
