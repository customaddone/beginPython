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

# Rolling hash
N = getN()
S = list(map(ord, list(input())))
# 適当
base = 1007
# base = 1009
power = [1] * (N + 1)
# 部分文字列を数字に
# ハッシュ生成
for i in range(1, N + 1):
    power[i] = power[i - 1] * base % mod
print(power)

# 長さmの文字列がダブらずに存在するか
def check(m):
    if N - m < m:
        return False
    res = 0
    # 頭m文字のハッシュ生成
    for i in range(m):
        res += S[i] * power[m - i - 1]
        res %= mod
    dic = {res: 0}
    for i in range(N - m):
        # ハッシュをローリングしていって次々m文字のハッシュを生成していく
        res = ((res - S[i] * power[m - 1]) * base + S[i + m]) % mod
        # もし既出なら
        if res in dic.keys():
            index = dic[res]
            if index + m <= i + 1: # 重ならないか
                return True
        else:
            dic[res] = i + 1 # i + 1:頭の位置を記録する
        print(dic)
    return False

ok = 0
ng = N + 1
while ng - ok > 1:
    mid = (ok + ng) // 2

    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)

N, K = getNM()
S = input()
if(K * 2 > N):
    print('NO')
    exit()
def check(n, s, k, mod, alp):
    # 各アルファベットをエンコード
    encode = {}
    for i, ch in enumerate(alp, 10001):
        encode[ch] = pow(172603, i, mod)
    # 文字列の先頭からm文字、k文字目からm文字をハッシュしていく
    left = 0
    right = 0
    for i in range(k):
        left += encode[s[i]]
        left %= mod
        right += encode[s[i + k]]
        right %= mod
    words = set()
    # ローリングする
    for i in range(n):
        words.add(left)
        if (right in words):
            return True
        if (i + 2 * k >= n):
            break
        left += encode[s[i + k]] - encode[s[i]]
        left %= mod
        right += encode[s[i + k * 2]] - encode[s[i + k]]
        right %= mod
    return False
ans = True
ps = '9999217 9999221 9999233 9999271 9999277 9999289 9999299 9999317 9999337 9999347 9999397 9999401 9999419 9999433 9999463 9999469 9999481 9999511 9999533 9999593 9999601 9999637 9999653 9999659 9999667 9999677 9999713 9999739 9999749 9999761 9999823 9999863 9999877 9999883 9999889 9999901 9999907 9999929 9999931 9999937 9999943 9999971 9999973'
ps = list(map(int, ps.split(' ')))
ps.append(10 ** 9 + 7)
ps.append(3040409)
ps.append(10 ** 20 + 9)
# 各modについて
for p in ps:
    # アルファベットをランダムに並べた表でエンコード表を作る
    for alp in ['qwertyuioplkmnjhbvgfcdxsaz','qazxcsdwertfgvbnmhjyuioklp']:
        ans = (ans & check(N, S, K, p, alp))
if(ans):
    print('YES')
else:
    print('NO')

# ARC024 だれじゃ
N, K = getNM()
S = input()

if(K * 2 > N):
    print('NO')
    exit()

# ダブらない場所に長さKの同じ文字の種類と数で構成された部分があるか
def check(n, s, k, mod, alp):
    # 各アルファベットをエンコード
    encode = {}
    for i, ch in enumerate(alp, 10001):
        encode[ch] = pow(172603, i, mod)

    # 文字列の先頭からm文字、k文字目からm文字をハッシュしていく
    res = 0
    for i in range(k):
        res += encode[s[i]]
        res %= mod

    dic = {res: 0}
    # ローリングする
    for i in range(n - k):
        res += encode[s[i + k]] - encode[s[i]]
        res %= mod
        if res in dic.keys():
            index = dic[res]
            if index + k <= i + 1:# ダブって無いか
                return True
        else:
            dic[res] = i + 1

    return False

ans = True
ps = '9999217 9999221 9999233 9999271 9999277 9999289 9999299 9999317 9999337 9999347 9999397 9999401 9999419 9999433 9999463 9999469 9999481 9999511 9999533 9999593 9999601 9999637 9999653 9999659 9999667 9999677 9999713 9999739 9999749 9999761 9999823 9999863 9999877 9999883 9999889 9999901 9999907 9999929 9999931 9999937 9999943 9999971 9999973'
ps = list(map(int, ps.split(' ')))
ps.append(10 ** 9 + 7)
ps.append(3040409)
ps.append(10 ** 20 + 9)
# 各modについて
for p in ps:
    # アルファベットをランダムに並べた表でエンコード表を作る
    for alp in ['qwertyuioplkmnjhbvgfcdxsaz','qazxcsdwertfgvbnmhjyuioklp']:
        ans = (ans & check(N, S, K, p, alp))

if(ans):
    print('YES')
else:
    print('NO')

# 天下一プログラマーコンテスト2014予選B B - エターナルスタティックファイナル

# ローリングハッシュ
# sの連続部分列とkがマッチした部分s[i:j]についてのi, jを求める
# 文字列を数字に変換してから使おう
def check(stri, targ, base):
    s = list(map(ord, list(stri)))
    k = list(map(ord, list(targ)))
    n = len(s)
    m = len(k)
    if n - m < 0:
        return set()

    pm = 2 ** 61 - 1
    power = [1] * (n + 1)

    # 第i文字目のハッシュ生成
    for i in range(1, n + 1):
        power[i] = power[i - 1] * base % pm

    res = 0 # ハッシュを保存
    # sの頭m文字のハッシュ生成
    for i in range(m):
        res += s[i] * power[m - i - 1]
        res %= pm

    # kのハッシュを生成
    target = 0
    for i in range(m):
        target += k[i] * power[m - i - 1]
        target %= pm

    # sをローリングさせて調べる
    opt = set()
    for i in range(n - m):
        # マッチしたら
        # 半開区間で返す（変更可能）
        if res == target:
            opt.add((i, i + m))
        # 0 ~ m文字目, 1 ~ m+1文字目...を生成しkと比べる
        res = ((res - s[i] * power[m - 1]) * base + s[i + m]) % pm
    # 最後の1回
    if res == target:
        opt.add((n - m, n))

    return opt

def rolling_hash(s, t):
    # ほんとは原子根乱択がいい
    # 基数baseと法pmをたくさん用意しないとfalseのものがtrueになるため、
    # 全部trueのものだけを返す
    res = check(s, t, 161971)
    for base in [167329, 191911]: # 適当に手動で乱択してね
        # これ一回の計算量はO(N)
        res &= check(s, t, base)
    return res

N = getN()
S = input()
T = [input() for i in range(N)]

opt = []
for i in range(N):
    # ロリハするとO(S + T)になる（もともとはO(S * (T ** 2)))
    for j in list(rolling_hash(S, T[i])):
        opt.append(j)

dict = defaultdict(list)
for l, r in opt:
    dict[r].append(l)

# opt(ST)の大きさがネックになり、前進型貰うdpで計算量はO(ST)
# 合計で計算量はO(ST + T ** 2)(ロリハの部分)　なお定数倍
dp = [0] * (len(S) + 1)
dp[0] = 1
for i in range(len(S) + 1): # iが右端
    for l in dict[i]:
        dp[i] += dp[l]
    dp[i] %= mod

print(dp[-1] % mod)