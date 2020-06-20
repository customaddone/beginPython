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

N = 2
L = [1, 1]
root = 4

# root ** Nでループ
def four_pow(i, array):
    global cnt
    if i == N:
        print(array)
        return
    for j in range(root):
        new_array = array + [j]
        four_pow(i + 1, new_array)
four_pow(0, [])

# 組み合わせ
def comb_pow(i, array):
    global cnt
    if i == N:
        print(array)
        return
    # ここの4を変えてrootを変更
    last = 0
    if len(array) > 0:
        last = array[-1]

    for j in range(last + 1, root):
        new_array = array + [j]
        comb_pow(i + 1, new_array)
comb_pow(0, [])

# 重複組み合わせ
def rep_comb_pow(i, array):
    global cnt
    if i == N:
        print(array)
        return
    # ここの4を変えてrootを変更
    last = 0
    if len(array) > 0:
        last = array[-1]

    for j in range(last, root):
        new_array = array + [j]
        rep_comb_pow(i + 1, new_array)
rep_comb_pow(0, [])
