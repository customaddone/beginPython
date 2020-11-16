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
MOD = 10 ** 9 + 7

#############
# Main Code #
#############

# ABC025 C - 双子と○×ゲーム
# ゲーム木

b1 = getList()
b2 = getList()
c1 = getList() + [0]
c2 = getList() + [0]
c3 = getList() + [0]
b = b1 + b2
c = c1 + c2 + c3
S = sum(b) + sum(c)

def counter(array):
    male = 0
    for i in range(9):
        # bの得点
        if i <= 5:
            if array[i] == array[i + 3]:
                male += b[i]
        # cの得点
        if i % 3 == 0 or i % 3 == 1:
            if array[i] == array[i + 1]:
                male += c[i]
    return male

memo = {}

def solve(array):
    # メモ呼び出し
    if str(array) in memo:
        return memo[str(array)]
    # ターンの計算
    turn = 1
    for i in array:
        if i == 0 or i == 1:
            turn += 1
    if turn == 10:
        return counter(array)

    if turn % 2 == 0:
        point = S
    else:
        point = -S

    # i番目に駒を置いた時の全通りを探索して最善の手を呼び出す
    # 今の盤面 + αを置いた時の点数が全て帰ってくる その中で
    # turn % 2 == 0なら最小値、turn % 2 != 0 なら最大値を選ぶ
    for i in range(9):
        if array[i] == -1:
            new = copy.deepcopy(array)
            if turn % 2 == 0:
                new[i] = 1
                point = min(point, solve(new))
            else:
                new[i] = 0
                point = max(point, solve(new))
    memo[str(array)] = point
    return point

opt = [-1] * 9
ans = solve(opt)
print(ans)
print(S - ans)

# Indeedなう（予選A）D - パズル

"""
最小回数を求めよ
3 3
1 0 2
4 5 3
7 8 6 なら

1 2 0
4 5 3
7 8 6

1 2 3
4 5 0
7 8 6

1 2 3
4 5 6
7 8 0 で3回

全ての数字が所定の場所にいる
回数無視でまずはどうすれば行けるか
任意の回数行えるなら、各数字は好きな場所に行ける

1 3
2 0 の場合

1 0
2 3

0 1
2 3

2 1
0 3

2 1
3 0

3 2 1がぐるぐる回るだけだから永遠に無理
最小操作数が24回以内なので絶対に成功するケースのみ出る

全探索4 * 24　無理
戻る必要はないので3 ** 24
多分全探索なんだろう
一つの行動で最大1合わせることができる
枝刈りする

ngはマンハッタン距離で持つ
"""

H, W = getNM()
C = [getList() for i in range(H)]

def manh(point):
    ny = (point - 1) // W
    nx = (point - 1) % W
    return ny, nx

ng = 0
sta = [0, 0]
for i in range(H):
    for j in range(W):
        if C[i][j] == 0:
            sta = [i, j]
            continue
        ny, nx = manh(C[i][j])
        ng += abs(ny - i) + abs(nx - j)

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

memo = {}
ans = float('inf')

def dfs(turn, array, y, x, direct, ng):
    global ans
    if str(array) in memo and memo[str(array)] <= turn:
        return

    if ng == 0:
        ans = min(ans, turn)
        return

    if turn > 24 - ng or ans <= turn:
        return

    for i in range(4):
        if i == (direct + 2) % 4:
            continue
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < H and 0 <= nx < W:
            new_array = deepcopy(array)
            new_ng = ng
            # 0と入れ替える数字について
            my, mx = manh(array[ny][nx])
            new_ng -= (abs(my - ny) + abs(mx - nx))
            new_ng += (abs(my - y) + abs(mx - x))

            new_array[ny][nx] = array[y][x] # 0
            new_array[y][x] = array[ny][nx]
            dfs(turn + 1, new_array, ny, nx, i, new_ng)

    memo[str(array)] = turn

dfs(0, C, sta[0], sta[1], float('inf'), ng)
print(ans)
