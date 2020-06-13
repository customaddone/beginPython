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

H, W = getNM()
maze = []
for i in range(H):
    m = list(input())
    maze.append(m)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

memo = [[-1] * W for i in range(H)]

def counter(sx, sy):
    black_cnt = 0
    white_cnt = 0

    memo[sy][sx] = 1
    if maze[sy][sx] == "#":
        black_cnt += 1
    else:
        white_cnt += 1

    pos = deque([[sx, sy]])

    while len(pos) > 0:
        x, y = pos.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < W and 0 <= ny < H and maze[ny][nx] != maze[y][x] and memo[ny][nx] == -1:
                memo[ny][nx] = 1
                pos.append([nx, ny])
                if maze[ny][nx] == "#":
                    black_cnt += 1
                else:
                    white_cnt += 1
    return black_cnt * white_cnt

ans = 0
for i in range(H):
    for j in range(W):
        ans += counter(j, i)
print(ans)
