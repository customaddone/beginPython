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

# ABC043 D - アンバランス
# i文字目を見る場合
# i - 1文字目が同じ文字ならアウト
# i - 2文字目が同じでもアウト
S = input()
N = len(S)

ans = [-1, -1]
for i in range(1, N):
    if S[i] == S[i - 1]:
        ans = [i, i + 1]
        break
    if i > 1 and S[i] == S[i - 2]:
        ans = [i - 1, i + 1]
        break
print(*ans)

# ABC049 C - 白昼夢

S = input()

while len(S) >= 5:
    # Sを４つの単語で順に調べて刈っていく
    if len(S) >= 7 and S[-7:] == "dreamer":
        S = S[:-7]
        continue

    if len(S) >= 6 and S[-6:] == "eraser":
        S = S[:-6]
        continue

    elif S[-5:] == "dream" or S[-5:] == "erase":
        S = S[:-5]
        continue

    else:
        break

if len(S) == 0:
    print("YES")
else:
    print("NO")

# ARC019 B - こだわりの名前
S = input()
N = len(S)
bi = N // 2
str_f = []
for i in range(bi):
    str_f.append(S[i])
str_b = []
for i in range(bi):
    str_b.append(S[-i - 1])

cnt = 0
for i in range(bi):
    if str_f[i] != str_b[i]:
        cnt += 1

# 全て一致
if cnt == 0:
    # 真ん中以外は何に変えても回文にならない
    # 真ん中は何に変えても回文になる
    print(2 * bi * 25)
elif cnt == 1:
    if N % 2 == 0:
        print(25 * bi * 2 - 2)
    else:
        # 真ん中は何に変えても回文にならない
        print(25 * bi * 2 - 2 + 25)
else:
    print(25 * N)

# AGC048 A - atcoder < S

"""
スワップの最小回数は
１文字目 a
どこかにaより上がいたらそれをスワップして終了
aならそのまま
a以下なら？
counterする？
前から探索する
スワップしなくていいならスワップしない
target[i] > alta[i]の時スワップする
前のとスワップするかも
そもそもatcoderは6文字
スワップの最大回数は6回
次の文字にいくのはtarget[i] = alta[i]だった時のみ
target[i] < alta[i]: 終了
target[i] = alta[i]: 次に
target[i] > alta[i]: スワップ要
target'atcoder'が任意の文字(例:topcoder)、任意の二箇所（隣接しなくていい）をスワップできるなら
一文字目を見る
target[i] < alta[i]: 終了
target[i] = alta[i]: 次に
target[i] > alta[i]: スワップ要
その文字以降を探索 target[i]を上回るものがあればスワップ += 1終了
無い場合　target[i]と同じものが見つかればそのうち一番右のものとスワップ
　　　　　target[i]を下回るものしかなければ終了
たぶん
"""

T = getN()
S = [input() for i in range(T)]

for s in S:
    if s.count('a') == len(s):
        print(-1)
        continue

    if s > 'atcoder':
        print(0)
        continue

    n = len(s)
    for i in range(n):
        # aより上の要素をスワップを繰り返し運送する

        # i - 1回運送すると2番目の位置にくる
        # もしord('t') < ord(i)なら条件を満たし終了
        # そうでなければもう一つ前に運送する

        # i回運送すると１番目の位置に来る
        # ord('a') < ord(i)より条件を満たす
        if s[i] > 'a':
            if s[i] > 't':
                print(i - 1)
            else:
                print(i)
            break

# Code Formula 2014 予選B C - 仲良し文字列

"""
各文字が何文字違っていれば条件は成立するか
a, b, c, d, e, fの順列を調べてみる

a b c d e f
b a c d e f いける

a b c d e f
b a d c e f いけない

a b c d e f
e a b c d f はいけない

a b c d e f
f a b c d e は？

a b c d e f
a f b c d e
a e b c d f
a b e c d f いけない

スワップする回数は6C2 ** 3 でいいので全探索する
"""

A = list(input())
B = list(input())

diff = []
dupulicate_char_index = -1
appeared = set()
for i, (a, b) in enumerate(zip(A, B)):
    if a != b:
        diff.append(i)
    if a in appeared:
        dupulicate_char_index = i
    appeared.add(a)
if dupulicate_char_index != -1:
    diff += [dupulicate_char_index] * (6 - len(diff))

# 達成不可能
if len(diff) > 6:
    print('NO')
    exit()


def check(a, change_cnt):
    if (dupulicate_char_index != -1 or change_cnt == 3) and (a == B):
        print('YES')
        exit()


def dfs(a, depth):
    if depth == 3:
        return
    for i, j in combinations(diff, 2):
        a[i], a[j] = a[j], a[i]
        check(a, depth + 1)
        dfs(a, depth + 1)
        a[i], a[j] = a[j], a[i]

dfs(A, 0)
print('NO')
