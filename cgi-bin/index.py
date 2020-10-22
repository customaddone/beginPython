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

# キーエンス プログラミング コンテスト 2019 D - Double Landscape

"""
1 ~ N * M の整数を書き込む
i行目の数字の最大の数字はA
j行目の数字の最大の数字はB

反転数の数を求める時は列ごと入れ替え、列内入れ替えを行った
書き込みの個数を求めよ dpかcombo?

条件の満たし方を考える
まず条件を満たすものを一つ出す
Aiがn　i行目にはnとn以下の数字しか書かれていない

AとB両方に登場するとは限らない
ある数について指定の場所に置かないといけない
あとは自由 comboで求める
3 3
5 9 7
3 6 9
  5 9 7
3
6
9

9を置く
  5 9 7
3
6
9   9
8を置く　置けない！

二次元累積和？
N * M ~ 1まで１つずつ数を置いていく
iがAにある and Bにある
・解放する部分
今まで解放された部分と今回解放する部分の交わるとこ + 今回解放されるとこのクロス
・置けるとこ
1箇所　今回解放されるとこのクロス

iがAにある ^ Bにある
・解放する部分
今まで解放された部分と今回解放する部分の交わるとこ
・置けるとこ
今回解放されたとこのいずれかに置く

A,Bにない
現在解放されているマスのどこにでも置ける
"""

N, M = getNM()
A = set(getList())
B = set(getList())
if len(A) < N or len(B) < M: # A,B内で数字がダブってたら0
    print(0)
    exit()

ans = 1
opened = 0 # 解放されたマス
a_allowed = 0 # 解放された行
b_allowed = 0 # 解放された列

for i in range(N * M, 0, -1):
    if (i in A) and (i in B):
        # 解放はできる
        opened += (a_allowed + b_allowed) + 1 # 今まで解放された部分と今回解放する部分の交わるとこ + 今回解放されるとこのクロス
        a_allowed += 1
        b_allowed += 1
        opened -= 1 # 解放されたマスに置く
        # ans *= 1 # 置けるのは1箇所　今回解放されるとこのクロス
    elif (i in A):
        opened += b_allowed # 解放する行 * 解放されている列
        a_allowed += 1
        ans *= b_allowed # 今回解放された行のいずれかに置く
        opened -= 1
    elif (i in B):
        opened += a_allowed
        b_allowed += 1
        ans *= a_allowed
        opened -= 1
    else:
        ans *= opened # 解放されている部分のどこに置いても良い
        opened -= 1

    ans %= mod

print(ans)
