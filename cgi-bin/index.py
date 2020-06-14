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
from itertools import permutations
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7


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
