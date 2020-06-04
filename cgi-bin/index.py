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

H, W, T = getNM()
s = [list(input()) for _ in range(H)]

minT = 0
maxT = 10 ** 9 + 1

start = []
goal = []
for i in range(H):
    for j in range(W):
        if s[i][j] == "S":
            start = [i,j]
        if s[i][j] == "G":
            goal = [i,j]

def comp_dist(x, s):
    return x if s == "#" else 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 二分探索 + ダイクストラ
while maxT - minT > 1:
    dis = minT + (maxT - minT) // 2
    dist = [[float("inf") for _ in range(W)] for _ in range(H)]
    dist[start[0]][start[1]]=0

    q = []
    q.append([0, start[0], start[1]])
    heapq.heapify(q)
    while len(q) > 0:
        distance, x, y = heapq.heappop(q)
        if dist[x][y] < distance:
            continue

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue

            nd = dist[x][y] + comp_dist(dis, s[nx][ny])
            if dist[nx][ny] > nd:
                dist[nx][ny] = nd
                heapq.heappush(q, [nd, nx, ny])

    if dist[goal[0]][goal[1]] > T:
        maxT = dis
    elif dist[goal[0]][goal[1]] <= T:
        minT = dis

print(minT)
