from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right

import sys
def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getListGraph():
    return list(map(lambda x:int(x) - 1, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353
# sys.setrecursionlimit(1000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# ABC023 C - 収集王
# 経路圧縮

R, C, K = getNM()
N = getN()
query = [getList() for i in range(N)]

# 縦hに行くとi個飴がもらえる
h_list = defaultdict(int)
w_list = defaultdict(int)
h_len = set()
w_len = set()

for h, w in query:
    h -= 1
    w -= 1
    h_list[h] += 1
    w_list[w] += 1
    h_len.add(h)
    w_len.add(w)

# 飴がj個もらえる行はどこか
candy_h = defaultdict(list)
candy_w = defaultdict(list)

for i in h_list.items():
    candy_h[i[1]].append(i[0])
for i in w_list.items():
    candy_w[i[1]].append(i[0])

# 縦のキャンディの個数が1 ~ K - 1の行それぞれについて
# 横のキャンディの個数がK - 1 ~ 1の列を調べて掛け合わせ
cnt = 0
for i in candy_h.items():
    if K - i[0] >= 1:
        cnt += len(i[1]) * len(candy_w[K - i[0]])

# 縦が0個
cnt += (R - len(h_len)) * len(candy_w[K])
# 縦がN個
cnt += (C - len(w_len)) * len(candy_h[K])

# 足しすぎたもの、足していないものを修正
for r, c in query:
    r -= 1
    c -= 1
    if h_list[r] + w_list[c] == K:
        cnt -= 1
    elif h_list[r] + w_list[c] == K + 1:
        cnt += 1

print(cnt)

# Educational Codeforces Round 76 (Rated for Div. 2)
# D. Yet Another Monster Killing Problem

"""
攻撃p 体力s
モンスターの強さ以上の強さがあれば倒せる
1日にs体以上のモンスターを倒せない
ヒーローは何回でも使える
最短日数を答える
貪欲にいくか　そのつど最大モンスターを倒せる勇者を探す

強さp以上で耐久s以上の勇者が存在するかどうか
強さpでのsの最大値は？

前から何体倒せるかを貪欲に　強さpの区間の最大はいくらかを求めればいい
"""

T = getN()
for _ in range(T):
    N = getN()
    Mon = getList()
    H = getN()
    Her = [getList() for i in range(H)]
    Her.sort()

    comp = sorted(list(set(Mon)))
    d = {}
    endu = 0
    for m in comp[::-1]:
        while Her and Her[-1][0] >= m:
            endu = max(endu, Her.pop()[1])
        d[m] = endu

    now, day, pow = 0, 1, 0
    for i in range(N):
        pow = max(pow, Mon[i])
        if d[pow] == 0:
            print(-1)
            break
        # daybreak
        if d[pow] < i - now + 1:
            pow = Mon[i]
            day += 1
            now = i
    else:
        print(day)
