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

# 文字列を整数に変換
N = 26

def num2alpha(num):
    if num <= 26:
        return chr(96 + num)
    elif num % 26 == 0:
        return num2alpha(num // 26 - 1) + chr(122)
    else:
        return num2alpha(num // 26) + chr(96 + num % 26)

# z
print(num2alpha(N))

n = N
lista = []
digit = 26
i = 0

while n != 0:
    opt = n % digit
    lista.insert(0, opt)
    if n % digit == 0:
        n = n // digit - 1
    else:
        n = n // digit
    i += 1

str_list = 'abcdefghijklmnopqrstuvwxyz'
ans = ''
for i in range(len(lista)):
    ans += str_list[lista[i] - 1]

# z
print(ans)

#  最長共通部分列
s = 'pirikapirirara'
t = 'poporinapeperuto'

def dfs(s, ts):
    lens = len(s)
    lent = len(t)
    dp = [[0] * (lent + 1) for i in range(lens + 1)]
    dp[0][0] = 0

    for i in range(lens):
        for j in range(lent):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = max(dp[i][j] + 1, dp[i + 1][j], dp[i][j + 1])
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[lens][lent]
print(dfs(s, t))

# レーベンシュタイン距離
s = "pirikapirirara"
t = "poporinapeperuto"

def dfs(s, t):
    lens = len(s)
    lent = len(t)
    dp = [[float('inf')] * (lent + 1) for i in range(lens + 1)]
    dp[0][0] = 0

    for i in range(lens):
        for j in range(lent):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j] + 1, dp[i][j + 1] + 1)
            else:
                dp[i + 1][j + 1] = min(dp[i][j] + 1, dp[i + 1][j] + 1, dp[i][j + 1] + 1)
    return dp[lens][lent]
print(dfs(s, t))

# ABC009 C - 辞書式順序ふたたび

N,K = getNM()
S = list(input())
T = sorted(S)
diff = 0
ans = ""

for i in range(N):
    s = S[i]
    # 残りの文字を全ループさせる
    for t in T:
        # tを追加して良いか確かめる
        diff1 = diff + (s != t)
        count = Counter(T)
        count[t] -= 1
        diff2 = sum((Counter(S[i + 1:]) - count).values())
        # 追加していいなら
        if diff1 + diff2 <= K:
            diff = diff1
            ans += t
            T.remove(t)
            break
print(ans)

# ABC031 語呂合わせ

# 1 ~ Kまでの数字がどの単語に当てはまるか
# 1 ~ Kに対し文字の候補は26 ** 3通り?

# 文字列は総文字数、アルファベットの種類（２６種類、定数倍）で捉えられる

N, M = getNM()
que = []
for i in range(M):
    v, w = input().split()
    que.append([v, w])
root = 3

def judge(array):
    # 1 ~ Kに割り当てた文字数が正しいか
    for v, w in que:
        cnt = 0
        for i in range(len(v)):
            cnt += array[int(v[i]) - 1]
        if cnt != len(w):
            return
    # 文字数が適合するなら
    str_list = [''] * N
    for v, w in que:
        cnt = 0
        # 文字を区切っていく
        for i in range(len(v)):
            str_len = array[int(v[i]) - 1]
            opt = w[cnt: cnt + str_len]
            if str_list[int(v[i]) - 1] == '':
                str_list[int(v[i]) - 1] = opt
            else:
                if str_list[int(v[i]) - 1] != opt:
                    return
            cnt += str_len

    # 全て適合するなら
    for i in str_list:
        print(i)
    exit()

# 1 ~ Kの文字数が何文字かについて3 ** Kを全探索
def four_pow(i, array):
    global cnt
    if i == N:
        judge(array)
        return
    for j in range(1, root + 1):
        new_array = array + [j]
        four_pow(i + 1, new_array)
four_pow(0, [])

K, N = getNM()
G = []
for i in range(N):
    v, w = map(str, input().split())
    # 桁ごとに数字を分ける
    v = list(v)
    v = [int(d) - 1 for d in v]
    G.append((v, w))

# それぞれの語呂数に対して長さ1 ~ 3を割り当てる
for p in product(range(1, 4), repeat = K):
    S = [[] for _ in range(K)]
    for v, w in G:
        c = 0
        # 長さが正しいか判定するパート
        for d in v:
            # 使われた語呂数の長さを足し合わせる
            c += p[d]
        if c != len(w):
            break
        # 文字列を割り当てるパート
        else:
            cur = 0
            for d in v:
                # 長さごとに文字列を切っていく
                S[d].append(w[cur: cur + p[d]])
                cur += p[d]
    # 長さが整合したものが見つかれば
    else:
        for i in range(K):
            # 任意の語呂数に対する文字列が一意に定まらなければ
            # 112: abcで 1 = a, 1 = B, 2 = cになるみたいなケース
            if len(set(S[i])) != 1:
                break
        else:
            for i in range(K):
                print(S[i][0])
            exit()
