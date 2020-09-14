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

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

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
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7


#############
# Main Code #
#############
K = getN()
S = input()
N = len(S)

# 多分dp
# できる文字列の数
# アルファベットa~z26個をK回挿入すると？
# 一回目a 二回目aだとaaであり、順番逆でも同じ
# 文字数 * どこに挿入するか
# oの右にoを置いてもoの左にoを置いても同じ

# 最終的には長さN + Kの文字ができる
# ???o?of? ?はオールマイティ

# 前から順にdpしていく?
# i文字目にS[j]を使うか?を使うか

### ????????のうちo, o, fを使う文字列の種類は? ###
# o, o, fの場所を決めて?にa~zを入れる？
# ?でoを使ってもo, o, fのうちのoを使っても同じ

A = 'abcdefghijklmnopqrstuvwxyz'
S = [A.index(S[i]) for i in range(N)]
print(S)

dp = [[0] * 26 for i in range(N + K + 1)]
dp[0][0] = 1

for i in range(1, N + K + 1):
    for j in range(26):
        if j == S[i]:
