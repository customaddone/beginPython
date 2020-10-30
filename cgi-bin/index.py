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

# AGC022 B - GCD Sequence

"""
Aの各要素は全て異なる
どのaiについても
gcd(ai, sum(A) - ai)が1ではない
aiとsum(A) - aiが共通因数をもつ

aiとsum(A)が共通因数を持つ

Aの全ての要素を同じ因数を持つものに変えれば簡単
全ての要素の最大公約数が1である　の場合は？
互いに素なものが１つでもあればOK

1 2 3 は条件を満たす　完全数なら話は早い　早くない　1に何してもgcdは1

N <= 10000より　1 * n, 2 * n, 3 * n...とするのは諦める
ターゲットとなるgcdの数は小さくないと間に合わない
2と3で統一してみれば
3の
3の倍数を偶数個足すと偶数になる
でも偶数と3の倍数である奇数のgcdは1
要素は3万以下であることに注意

2 ~ 30000までの偶数(15000個)
3 ~ 30000までの3の倍数かつ奇数の数(5000個) できる！！！

偶数の個数は
N % 3 == 0の時 6の倍数を先頭に
30000 + 29997, 29991
N % 3 == 1の時
2, 4 + 3, 9 逆から
N % 3 == 2の時
2, 4, 6 + 3, 9 楽

制限ないと楽だけど
限界まで2の倍数を並べればいい
N % 3 == 0　2の倍数N - 2個
N % 3 == 1  2の倍数N - 2個
N % 3 == 2  2の倍数N - 2個

N = 3の時は注意

上限を15000にすると3の個数が変動する
"""

N = getN()

def cnter(ans):
    two = 0
    three = 0
    tw_l = 0
    th_l = 0
    for i in ans:
        if i % 2 == 0:
            two += 1
            tw_l += i
        elif i % 3 == 0:
            three += 1
            th_l += i

    return tw_l % 3, th_l % 2, two, three, max(ans), min(ans)

if N == 3:
    print(2, 5, 63)
    exit()

if N % 3 == 0:
    even = min(N - 2, 15000) # 偶数の個数
    three = N - even # 基本的には2 これは偶数個でないといけない

    caution = False
    if three % 2 != 0: # even == 15000 でthreeの個数が奇数になった場合　調整1
        caution = True
        three += 1

    ans = [i * 2 for i in range(15000, 15000 - even, -1)]
    if caution: # 調整2 even -= 1
        ans.pop(0) # 30000を抜き取る

    for i in range(three):
        ans.append(i * 6 + 3)

    print(*ans)

else: # 2と3が絶対に並ぶのでgcd = 1
    even = min(N - 2, 15000) # 偶数の個数
    three = N - even

    caution = False
    if three % 2 != 0: # even == 15000 でthreeの個数が奇数になった場合　調整1
        caution = True
        three += 1

    ans = [i * 2 for i in range(1, even + 1)]
    if caution: # 調整2
        ans.pop() # 30000を抜き取る

    for i in range(three):
        ans.append(i * 6 + 3)

    print(*ans)
