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
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# AGC019 B - Reverse and Compare

"""
何通りあるか　comboかdp
nC2を選んで i == jは意味ない
1 2 aatt
1 3 taat
1 4 ttaa
2 3 atat
2 4 atta
3 4 aatt
無駄な動きはない？
全通り選んでダブったのを引くか、前からdpか、comboか

ataaの場合
2 3 aata
1 4 aata 同じ
a, s1, s2...sn, aの場合
a ~ aとs1 ~ s2は同じ
ペアが１つあれば１つダブりが生まれる
文字が同じ場所を探す
abracadabraの場合
2 10 と 1 11は同じだし、
2 3 と 1 4も同じ
"""

A = input()
N = len(A)
l = [0] * 26

for i in range(N):
    l[ord(A[i]) - ord('a')] += 1

ans = (N * (N - 1) // 2) + 1
for i in range(26):
    ans -= l[i] * (l[i] - 1) // 2
print(ans)

# C - Inserting 'x'
# 回文判定

S = input()
T = S[::-1]
a = b = ans = 0

# a, bの前半分を調べ終わるまで
while a + b < len(S):
    if S[a] == T[b]:
        a += 1
        b += 1
    # Tにxを一つ増やす　bは進まない
    elif S[a] == 'x':
        a += 1
        ans += 1
    # Sにxを一つ増やす aは進まない
    elif T[b] == 'x':
        b += 1
        ans += 1
    else:
        print(-1)
        exit()
print(ans)
