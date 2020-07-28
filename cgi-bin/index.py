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
import heapq
import math
from fractions import gcd
import random
import string
import copy
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

N = 5
C = [2, 3, 2, 6, 12]

# 期待値　全ての通りについて考える
# C[i]について考えると、C[i]の倍数であるC[j]のみが作用の対象になる
# C[j]が表になる　↔︎　C[j]の左側にC[j]の約数が偶数個ある

# 期待値の求め方
# 並べ方S{a1, a2, a3...an}について左側の約数が偶数であるものの数を求める その数をf(S)とする
# 全ての{S1, S2...Sn}についてf(S)を求めて足し合わせ / N!

# 全ての状態{S1, S2... Sn}について{f(S1), f(S2)...}の総和を求めるみたいな問題は
# f(n)の構成要素について分解してそれぞれ総和して求めることができたりする → ABC170 D - Not Divisible
# f(S) = S[0]が表か裏か + S[1]が表か裏か + ....　
# 求めたい答え = C[0]が表である確率 + C[1]が表になる確率 + ...

# 必ずしも通りの数を求める必要はない
# 期待値　→　それぞれについて確率を求める問題
# C[i] + その約数のグループD内で何番目に来るか　→ 1番目、3番目...なら表
ans = 0

for i in C:
    lista = [j for j in C if i % j == 0]
    count = len(lista)
    ans += math.ceil(count / 2) / count
print(ans)
