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
mod = 998244353

#############
# Main Code #
#############

# ABC098 D - Xor Sum 2
# 連続する区間の長さを答える　尺取り

N = getN()
A = getList()

r, tmp = 0, 0
# l:左端
cnt = 0
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
    else:
        tmp -= A[l]
print(cnt)

# ABC117 D - XXOR
N, K = getNM()
A = getList()

# 各X xor Aiについて
# 各桁について
# Xにフラグ立つ + Aiにフラグ立たない
# Xにフラグ立たない + Aiにフラグ立つ　の時 2 ** iだけxorの値が増える
# Aの各要素の2 ** iのフラグの合計がn本の時
# Xの2 ** iのフラグを立てるとN - n * 2 ** i、立てないとn * 2 ** i　f(x)の値が増える

# 各桁のフラグが合計何本あるか
flag = [0] * 61
def splitbit(n):
    for i in range(61):
        if n & (1 << i):
            flag[i] += 1
for i in range(N):
    splitbit(A[i])

x = 0
ans = 0
for i in range(60, -1, -1):
    # flag[i] < N - flag[i]ならフラグを立てるほうがお得
    # だがKの制限があり立てたくても立てられないことがある
    # Xの2 ** iのフラグを立ててもXがKを超えないか
    if flag[i] < N - flag[i] and x + 2 ** i <= K:
        # Xにフラグを立てる
        x += 2 ** i
        # f(x)の値が増える
        ans += 2 ** i * (N - flag[i])
    # flag[i] < N - flag[i]だがフラグを立てられない場合 +
    # flag[i] >= N - flag[i]の時
    else:
        ans += 2 ** i * flag[i]

print(ans)

# ABC121 D - XOR World
A, B = getNM()
# bit1桁目のフラグの個数
# 周期は2 ** 1
# 0と1が交互に
# bit2桁目のフラグの個数
# 周期は2 ** 2
flags1 = [0] * 61
flags2 = [0] * 61
# 1 ~ nまでに各桁のフラグが何本立つか計算する関数
def bitflag(n, flaglist):
    if n > 0:
        for i in range(1, 61):
            split = 2 ** i
            flag1 = (n // split) * (split // 2)
            flag2 = max(n % split + 1 - (split // 2), 0)
            flaglist[i] += flag1 + flag2
# 1 ~ A - 1について（Aは範囲に入っているため）
bitflag(A - 1, flags1)
bitflag(B, flags2)
for i in range(61):
    flags2[i] -= flags1[i]
ans = 0
# 奇数ならフラグが立つ
for i in range(61):
    if flags2[i] % 2 != 0:
        ans += 2 ** (i - 1)
print(ans)

# ABC126 F - XOR Matching
# d = 2 ** N - 1について
# 1 xor 2 xor... xor dは
# 各桁にフラグが2 * (N - 1)本ずつ立っている（つまり0になる）
# なのでXを抜くとXを構成する部分についてフラグが抜けてXができる

M, K = getNM()

if M == 0 and K == 0:
    print(0, 0)

elif M == 1 and K == 0:
    print(0, 0, 1, 1)

elif M >= 2 and K < 2 ** M:
    ans = []
    for n in range(2 ** M):
        if n != K:
            ans.append(n)
    print(*ans, K, *ans[::-1], K)

else:
    print(-1)

# ABC129 E - Sum Equals Xor
# 二進数表記なので桁dpやろ

# L = 01(2)の時
# l - 0の時
# a = 0, b = 0(a = 1, b = 1の時 a ^ b = 0になるが a + b > lなのでだめ)
# l = 1の時
# a, b = (0, 1), (1, 0)
# l = 2の時
# a, b = (0, 2), (2, 0) (a = 11, b = 01でも a ^ b = 10になるがa + b > l)
# lのi桁目が1の時、aのi桁目は0 or 1だが、lのi桁目が0の時aのi桁目は0のみ
L = input()

def digit_dp_2(n):
    l = len(n)

    dp = [[[0] * 2 for _ in range(2)] for i in range(l + 1)]
    dp[0][0][0] = 1

    for i in range(l):
        d = int(n[i])

        # Lになる可能性があるかないか
        for j in range(2):
            # 次の桁が0か1か
            for d_j in range(2 if j else d + 1):
                if d_j == 0:
                    dp[i + 1][j | (d_j < d)][d_j] += (dp[i][j][0] + dp[i][j][1])
                    dp[i + 1][j | (d_j < d)][d_j] %= mod
                else:
                    dp[i + 1][j | (d_j < d)][d_j] += 2 * (dp[i][j][0] + dp[i][j][1])
                    dp[i + 1][j | (d_j < d)][d_j] %= mod

    return sum(dp[-1][0]) + sum(dp[-1][1])

print(digit_dp_2(L) % mod)
