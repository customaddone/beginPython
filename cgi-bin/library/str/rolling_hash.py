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

# ローリングハッシュ
# 文字Sのl ~ r文字目をハッシュ化する
# 順番を考慮するものとしないものがある

# ABC141 E - Who Says a Pun?
# 順番も考慮する

def check(n, s, k, base, alp):
    power = [1] * (N + 1)
    mo = 2 ** 61 - 1 # 最強のものを使用
    # 部分文字列を数字に
    # ハッシュ生成
    for i in range(1, N + 1):
        power[i] = power[i - 1] * base % mo

    res = 0
    # 頭m文字のハッシュ生成
    for i in range(k):
        res += s[i] * power[k - i - 1]
        res %= mo
    dic = {res: 0}
    for i in range(N - k):
        # ハッシュをローリングしていって次々m文字のハッシュを生成していく
        res = ((res - s[i] * power[k - 1]) * base + s[i + k]) % mo
        # もし既出なら
        if res in dic.keys():
            index = dic[res]
            if index + k <= i + 1: # 重ならないか
                return True
        else:
            dic[res] = i + 1 # i + 1:頭の位置を記録する

    return False

def rolling_hash(n, s, m):
    if n - m < m:
        return False
    s = list(map(ord, s)) # pythonは遅いので

    res = True
    # 原子根を適当に手動で乱択してね
    for base in [161971, 167329, 191911]:
        # アルファベットをランダムに並べた表でエンコード表を作る
        for alp in ['qwertyuioplkmnjhbvgfcdxsaz','qazxcsdwertfgvbnmhjyuioklp']:
            # これ一回の計算量はO(N)
            res &= check(n, s, m, base, alp)
    return res

N = getN()
S = input()

ok = 0
ng = N + 1
while ng - ok > 1:
    mid = (ok + ng) // 2

    if rolling_hash(N, S, mid):
        ok = mid
    else:
        ng = mid
print(ok)

# ARC024 だれじゃ
# 順番を考慮しないもの　種類だけ見るもの
# abc, bcd, cdb...を次々ハッシュ化していく
# 共通するものがあるか
# psが一つの場合はnoのものがyesになる場合があるのでたくさん用意する

N, K = 8, 3
S = 'abcdbcae'

if(K * 2 > N):
    print('NO')
    exit()

# ダブらない場所に長さKの同じ文字の種類と数で構成された部分があるか
def check(n, s, k, base, alp):
    # 各アルファベットをエンコード
    encode = {}
    for i, ch in enumerate(alp, 10001):
        # modは最強の2 ** 61 - 1を使う
        encode[ch] = pow(base, i, 2 ** 61 - 1)

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
        # 既出なら
        if res in dic.keys():
            # ダブってもいいなら以下はいらん
            index = dic[res]
            if index + k <= i + 1:# ダブって無いか
                return True
        else:
            dic[res] = i + 1

    return False

def rolling_hash(n, s, m):
    res = True
    # 原子根を適当に手動で乱択してね
    for base in [161971, 167329, 191911]:
        # アルファベットをランダムに並べた表でエンコード表を作る
        for alp in ['qwertyuioplkmnjhbvgfcdxsaz','qazxcsdwertfgvbnmhjyuioklp']:
            # これ一回の計算量はO(N)
            res &= check(n, s, m, base, alp)
    return res

if rolling_hash(N, S, K):
    print('YES')
else:
    print('NO')

# 天下一プログラマーコンテスト2014予選B B - エターナルスタティックファイナル

# ローリングハッシュ
# sの連続部分列とkがマッチした部分を全て記録する
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
