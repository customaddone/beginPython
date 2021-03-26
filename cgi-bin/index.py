from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import sys
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from bisect import bisect_left, bisect_right

def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# 日立製作所 社会システム事業部 プログラミングコンテスト2020
# C-ThREE

"""
構築問題？　都合のいいものから
距離が3離れてるものはすぐわかる？
2なら　子ノードの子ノードのうち自分以外の要素
3の倍数を使えば簡単　これはN / 3個使える
mod 0, mod1, mod2, mod1, mod0...という風に分配していけばいい
すぐに枯渇しそう
3の倍数以外で作ってみる
1, 2, 1, 2...って感じで置いていく
枯渇するけど倍数3を使えばいい

葉から順に赤、黒...と塗っていき
赤にmod1, 黒にmod2の数を入れる
なければmod 0の値を入れる

もう2つとも枯渇するパターン

赤黒木のバランスを元に場合分け
距離が３の頂点だけではなく、距離が奇数のものについても条件を達成できる
"""

N = getN()
E = [[] for i in range(N)]
for i in range(N - 1):
    a, b = getNM()
    E[a - 1].append(b - 1)
    E[b - 1].append(a - 1)

s = 0
for i in range(N):
    if len(E[i]) == 1:
        s = i
        break

one, two, thr = [], [], []
for i in range(1, N + 1):
    if i % 3 == 1:
        one.append(i)
    elif i % 3 == 2:
        two.append(i)
    else:
        thr.append(i)

ans = [-1] * N
color = [-1] * N
color[s] = 1
que = deque([s]) # 赤スタート

while que:
    u = que.popleft()
    for v in E[u]:
        if color[v] != -1:
            continue
        # 親のmodが1なら2を入れる
        if color[u] == 1:
            color[v] = 2
        else:
            color[v] = 1
        que.append(v)

# 1が極端に少ない場合
if color.count(1) <= len(thr):
    for i in range(N):
        if color[i] == 1:
            ans[i] = thr.pop()
    left = one + two + thr
    for i in range(N):
        if ans[i] == -1:
            ans[i] = left.pop()
    print(*ans)

elif color.count(2) <= len(thr):
    for i in range(N):
        if color[i] == 2:
            ans[i] = thr.pop()
    left = one + two + thr
    for i in range(N):
        if ans[i] == -1:
            ans[i] = left.pop()
    print(*ans)

# バランスがいい場合
else:
    for i in range(N):
        if color[i] == 1:
            if one:
                ans[i] = one.pop()
            else:
                ans[i] = thr.pop()
        else:
            if two:
                ans[i] = two.pop()
            else:
                ans[i] = thr.pop()
    print(*ans)
