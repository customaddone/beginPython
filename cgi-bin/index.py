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

# ARC021 B - Your Numbers are XORed...

"""
2 010 + 4 100 = 6 110
3 0011 + 12 1100 = 15 1111

元のA:{A1, A2...}を知りたい
Bi = Ai xor Ai+1
Bi+1 = Ai+1 xor Ai+2
Bi xor Bi+1 = Ai xor Ai+1 xor Ai+1 xor Ai+2
B1 xor B2 xor...Bn-1 = Ai xor An ?
Bn = An xor A1

B1 xor B2 xor...Bn = A1 xor A1 = 0 ?
該当する数列が存在するならこれは成立つ
B1 ^ A1 = A2
B2 ^ A2 = B2 ^ (B1 ^ A1) = A3
"""

L = getN()
B = getArray(L)

now = B[0]
for i in range(1, L):
    now ^= B[i]

if not now:
    # A1は辞書順最小なので0に
    a = 0
    for i in range(L):
        print(a)
        a ^= B[i]
else:
    print(-1)

# ABC098 D - Xor Sum 2
# 連続する区間の長さを答える　尺取り

N = getN()
A = getList()

l, ans, xo, total = 0, 0, 0, 0

for r in range(N):
    xo ^= A[r]
    total += A[r]

    # xo == totalになるまでA[l]で引き続ける
    while xo < total:
        xo ^= A[l]
        total -= A[l]
        l += 1

    ans += r - l + 1

print(ans)

# 第五回ドワンゴからの挑戦状 B - Sum AND Subarrays

"""
N <= 1000
連続部分列は全て取り出せる
どうやってK個を選ぶか

optを達成できるか
bit数が大きい方が絶対正義
とにかく大きいbitを立てる
"""

N, K = getNM()
A = getList()

l = []
for i in range(N):
    now = 0
    for j in range(i, N):
        now += A[j]
        l.append(now)

flag = 0 # フラグを強化していく

# フラグiが建っているものを集める
for i in range(60, -1, -1):
    opt = flag | (1 << i)
    cnt = 0
    for j in range(len(l)):
        if l[j] & opt == opt:
            cnt += 1
    if cnt >= K:
        flag |= (1 << i)

print(flag)


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

# Tenka1 Programmer Contest D - IntegerotS

"""
Aのbitの総和がK以下になるように整数を集める
ナップサック問題っぽいがAもBもおおきい
貪欲に行く
Kを超えた場合でも、他のでフラグを消せればいい

まず全部足し、フラグを抜いていく？
dpっぽいが2 ** 30の30を使う？
フラグの数が奇数か偶数か

bitwise or どちらかのビットが1なら1、そうでなければ0
一度立てたフラグは消えない

Kの各bitについて
フラグを立てるか立てないか
0 のbitlengthは0
1 のbitlengthは1 (右から1番目に最初のフラグが立っている)
2 のbitlengthは2
3 のbitlengthは2

[0, 0, 8, 4, 0, 0, 0,
むやみにフラグを立てないように

K = 101にどう従っていくか
1本目を1にするなら それ以降の条件にも従ってもらう

Kと比べた時に何本目まで従っているか
K = 101
a = 10の場合左から2番目が従えてない
[[3, 3, 1], [4, 4, -1], [2, 5, 1]]

別に30回回していい
一本目のKについて
立てるなら
Kにフラグが立ってなかったら
立ててはいけない

K以下の値の2進数換算は
Kのi番目の1のフラグを1 → 0にし、それ以下を自由にしたもの　である
フラグの数が多い方がいいので
整数を集めてできる数をXとすると
K = 11010の場合は
X = 01111, 10111, 11001 を見ていけばいい
足してXになる数を求めればいい

K以下の〜について
最も有利な条件を並べてそれぞれで計算
"""

N, K = getNM()
que = [getList() for i in range(N)]

ans = 0
# 足すとKのフラグになる
opt = 0
for a, b in que:
    if K | a == K:
        opt += b
ans = max(ans, opt)

# 足すとXのフラグになる
for i in range(31, 0, -1):
    opt = 0
    if K & (1 << i): # フラグが立っていれば
        X = (K ^ (1 << i)) | ((2 ** i) - 1) # 1 << iのフラグを消す + それ以下を全て1に
        for a, b in que:
            if X | a == X: # フラグの本数が変わらなければ
                opt += b

        ans = max(ans, opt)

print(ans)
