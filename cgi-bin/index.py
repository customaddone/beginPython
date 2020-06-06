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

"""
# 飛ばし累積和
N = 10
num = [i for i in range(1, N + 1)]
D = 2
lista = [0] * N
for i in range(D):
    for j in range(i, N, D):
        if j == i:
            lista[j] = num[j]
        else:
            lista[j] = num[j] + lista[j - D]
# [1, 2, 4, 6, 9, 12, 16, 20, 25, 30]
print(lista)
# 9番目までの奇数の数字の合計 - 1番目までの奇数の数字の合計
# 3 + 5 + 7 + 9
print(lista[8] - lista[0])
"""

# Dかそれぞれのqueryで固定なのでこの問題は解ける
H, W, D = getNM()
maze = []
for i in range(H):
    a = getList()
    maze.append(a)
Q = getN()
# piece[0]からpiece[1]まで
# 4 → 6　→ 8
piece = []
for i in range(Q):
    l, r = getNM()
    piece.append([l, r])

place_list = [[-1, -1] for i in range(H * W)]

for y in range(H):
    for x in range(W):
        place_list[maze[y][x] - 1] = [x, y]

# 飛ばし累積和
x_plus = [0] * (H * W)
y_plus = [0] * (H * W)
for i in range(D):
    for j in range(i, H * W, D):
        if j == i:
            opt_x = 0
            opt_y = 0
        else:
            opt_x = abs(place_list[j][0] - place_list[j - D][0])
            opt_y = abs(place_list[j][1] - place_list[j - D][1])
            x_plus[j] = opt_x + x_plus[j - D]
            y_plus[j] = opt_y + y_plus[j - D]

def past_exam(piece_query):
    start = piece_query[0]
    goal = piece_query[1]

    x_point = x_plus[goal - 1] - x_plus[start - 1]
    y_point = y_plus[goal - 1] - y_plus[start - 1]
    return x_point + y_point

for i in range(Q):
    print(past_exam(piece[i]))
