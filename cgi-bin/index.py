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

# 天下一プログラマーコンテスト2013予選B B - 天下一後入れ先出しデータ構造

Q, L = getNM()
query = [input().split() for i in range(Q)]
s = [] # 配列の中身
l = 0 # 配列の大きさ

for q in query:
    if q[0] == "Push":
        s.append([int(q[1]), int(q[2])])
        l += int(q[1])
    if l > L:
        print("FULL")
        exit()

    elif q[0] == "Pop":
        x = int(q[1])
        l -= x
        while s: # sが空になるまで xがゼロになるとbreakで抜ける
            c, y = s[-1]
            if x >= c:
                x -= c
                s.pop() # 抜く
            else:
                s[-1][0] -= x # 引くだけで抜かない
                x = 0
                break
        if x:
            print("EMPTY")
            exit()

    elif q[0] == "Size":
        print(l)

    elif q[0] == "Top":
        if s:
            print(s[-1][1])
        else:
            print("EMPTY")
            exit()

print("SAFE")
