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

N, Q = getNM()
sec = [getList() for i in range(N)]
section = []
for i in range(N):
    s, t, x = sec[i]
    section.append([s - x, t - x])
query = getArray(Q)

# 各queryがどのsectionの開区間[s, t)内にあるか
def event_sort(section, query):
    s_n = len(section)
    q_n = len(query)
    task = []
    for i in range(s_n):
        s, t = section[i]
        task.append((s, 0, i))
        task.append((t, 1, i))
    for i in range(q_n):
        task.append((query[i], 2, i))
    task.sort()

    se = set()

    ### この問題専用 ###
    res = [-1] * q_n # 答え
    ignore = [-1] * s_n # まだ区間が生きているか
    se_hp = [] # ignoreを元にまだ生きている区間の中でのxの最小値を求める
    heapify(se_hp)
    ##################

    for a, b, c in task:
        if b == 1:
            se.remove(c)
            ignore[c] = 1 # これは無視していい
        elif b == 0:
            se.add(c)
            heappush(se_hp, (sec[c][2], c)) # xの値をsecから引っ張る
        else:
            # 小さい順から抜け殻を捨てて回る
            while se_hp and ignore[se_hp[0][1]] == 1:
                heappop(se_hp)
            if se_hp:
                res[c] = se_hp[0][0]
            else:
                res[c] = -1
    return res

for i in event_sort(section, query):
    print(i)

section = [
[-3, 3],
[-1, 1],
[5, 7],
[1, 2],
]

query = [0, 1, 2, 3]

def event_sort(section, query):
    s = len(section)
    q = len(query)
    # イベント生成
    task = []
    for i in range(s):
        s, t = section[i]
        task.append((s, 0, i))
        task.append((t, 1, i))
    for i in range(q):
        task.append((query[i], 2, i))
    task.sort()

    # 引っかかってる場所の管理
    se = set()
    res = []

    for a, b, c in task:
        # ゴールが来ると削除
        if b == 1:
            se.remove(c)
        # スタートが来ると追加
        elif b == 0:
            se.add(c)
        # queについてなら
        else:
            res.append(deepcopy(se))

    return res

# query内の点iがどのsection内の点j内にあるか
# [{0, 1}, {0, 3}, {0}, set()]
print(event_sort(section, query))
