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

N, K = 7, 6
S = [4, 3, 1, 1, 2, 10, 2]

# 左を伸ばしていく
# その部分列に含まれる全ての要素の値の積は「K以下」である。
# lはrをオーバーすることもある

if 0 in S:
    print(N)
    exit()
else:
    l, ans, total = 0, 0, 1
    for r in range(N):
        total *= S[r]
        while total > K and l <= r:
            total //= S[l]
            l += 1
        ans = max(ans, r - l + 1)
print(ans)

# (条件) 連続部分列に含まれる全ての要素の値の和は、「K以上」である。
N, K = 4, 10
A = [6, 1, 2, 7]

left = 0
total = 0
ans = 0

for right in range(0, N):
    total += A[right]
    while total >= K:
        ans += N - right
        total -= A[left]
        left += 1
print(ans)

N = 10
S = 15
A = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]
right = 0
total = 0
ans = 0
# S以上を求める場合にはこの形で
for left in range(N):
    while right < N and total < S:
        total += A[right]
        right += 1
    if total < S:
        break
    if left == right:
        right += 1
    total -= A[left]

# 要素の種類についての問題
# 全ての要素を含む
P = 5
A = [1, 8, 8, 8, 1]
dict = {}
for i in A:
    dict[i] = 0
# 要素の種類数
V = len(dict.items())

# 事象の数をカウント
cnt = 0
right = 0
# １つ目から全ての事象をカバーするまでrightを進める
while right < P:
    if dict[A[right]] == 0:
        cnt += 1
    dict[A[right]] += 1

    if cnt == len(dict.items()):
        break

    right += 1
print(l, r)

l = 0
# 右を一つ進めて左をできる限り進める
for r in range(right + 1, P):
    # 新しく一つ加える
    dict[A[r]] += 1
    while True:
        # もし要素が一つしか無かったら削れない
        if dict[A[l]] == 1:
            break
        dict[A[l]] -= 1
        l += 1
    print(l, r)

# 各要素にダブりがない範囲
N = 6
A = [1, 2, 2, 3, 4, 4]

dict = defaultdict(int)
l = 0
for r in range(N):
    while dict[A[r]] == 1:
        dict[A[l]] -= 1
        l += 1
    print(l, r)
    dict[A[r]] += 1

# ARC022 B - 細長いお菓子
N = getN()
A = [i - 1 for i in getList()]

r = 0
kind = [0] * (10 ** 5 + 7) # 常に1種類につき一つに限られるよう
ans = 0
for l in range(N):
    # 半開区間で持つ方がいい
    while r < N and kind[A[r]] == 0:
        kind[A[r]] += 1
        r += 1
    ans = max(ans, r - l)
    kind[A[l]] -= 1

print(ans)

N = 4
A = 2, 5, 4, 6

r, tmp = 0, 0
# l:左端
cnt = 0
# 一つオーバーさせる
for l in range(N):
    while r < N and tmp ^ A[r] == tmp + A[r]:
        # 右端を伸ばす
        tmp += A[r]
        r += 1
    # 計算
    # r を一個進めて条件を満たさなくなった時点でループを終了しているので
    # (r - l + 1) - 1
    cnt += r - l

    if l == r:
        r += 1
    tmp -= A[l]
print(cnt)

N, K = 10, 4
A = [100, 300, 600, 700, 800, 400, 500, 800, 900, 900]

right, ans = 0, 0
for left in range(N):
    # 単調増加するとこまでもしくは長さKになるまで
    while right < N - 1 and A[right] < A[right + 1] and right - left < K - 1:
        right += 1
    # もし長さKまで伸ばせたらans += 1
    if right - left == K - 1:
        ans += 1
    # 前に進めないならright += 1
    if left == right and right < N:
        right += 1
print(ans)

# 第5回 ドワンゴからの挑戦状 予選 C - k-DMC

"""
Q <= 75?
文字列 dpか
k-DMCを求めよ
整数の組の個数 dp or combo
D, M, Cの順で並んでおり、文字の長さがk以下である
文字の長さを伸ばしていく
k = 1, 2... Qについて k - DMC数の数は？
累積の数を求める

長さがiのものをレコードしていく
文字の長さはaとcのみに依存する

A = []
B = []
C = []
for i in range(N):
    if S[i] == 'D':
        A.append(i)
    if S[i] == 'M':
        B.append(i)
    if S[i] == 'C':
        C.append(i)
これだとO(N ** 2)

a ~ c間にあるbの個数を累積和で求める
あるaについて対応するcが何個あるかは二分探索で求められる
間のbについては0 ~ cまで - 0 ~ aまで

二重累積和 + 計算量logNの改善
累積二分探索は尺取り法使える
"""

N = getN()
S = list(input())
Q = getN()
K = getList()

for k in K:
    ans = 0
    d_cnt = 0 # dの数
    m_cnt = 0 # mの数
    dm_cnt = 0 # dとmの組み合わせの数
    for i in range(N):
        # 上限超えたので捨てる
        if i - k >= 0:
            if S[i - k] == "D":
                d_cnt -= 1 # dを一つ捨て
                dm_cnt -= m_cnt # 捨てたdはmを現在ホールドしてる個数持っているので（dが左端にあるから）
            elif S[i - k] == "M":
                m_cnt -= 1 # mを捨てる

        if S[i] == "D":
            d_cnt += 1
        elif S[i] == "M":
            m_cnt += 1
            dm_cnt += d_cnt # 現在のd * 新しく入ったm(1つ)
        elif S[i] == "C":
            ans += dm_cnt # dm_cntの数 * 新しく入ったc(1つ)
