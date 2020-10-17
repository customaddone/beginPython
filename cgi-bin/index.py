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

# ABC147 D - Xor Sum 4

N = getN()
A = getList()
# Aの各数字の（２進数における）各桁ごとに分解して排他的論理和を求める
# 例
# 3
# 1 2 3 →
# 1, 10, 11
# 2 ** 0の桁について(1 ^ 2) 1 ^ 0 = 1,(1 ^ 3) 1 ^ 1 = 0,(2 ^ 3) 0 ^ 1 = 1
# 2 ** 1の桁について 0(1の2 ** 1の桁は0) ^ 1 = 1, 0 ^ 1 = 1, 1 ^ 1 = 0
# 各桁について2 ** iの桁が1の数字の選び方 * 2 ** iの桁が0の数字の選び方 * 2 ** iを
# 足し合わせる
lista = [[0, 0] for i in range(61)]
# bitの各桁が１か０かをlistaに収納
def splitbit(n):
    for i in range(61):
        if n & (1 << i):
            lista[i][1] += 1
        else:
            lista[i][0] += 1
for i in A:
    splitbit(i)
ans = 0
for i in range(61):
    ans += ((lista[i][0] * lista[i][1]) * (2 ** i)) % mod
print(ans % mod)

# ARC021 B - Your Numbers are XORed...
L = getN()
B = getArray(L)
B_xor = B[0]
for i in range(1, L - 1):
    B_xor ^= B[i]

# B_xor ^ a1(aの最後) ^ a1 == Bの最後なら成立
# この時aがどんな値であろうと条件が成立する
if B_xor == B[-1]:
    now = 0
    print(now)
    # a2 = B1 ^ a1
    # a3 = B2 ^ a2
    for j in range(L - 1):
        now = B[j] ^ now
        print(now)
else:
    print(-1)
