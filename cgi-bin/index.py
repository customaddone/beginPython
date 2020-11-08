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

# C - String Coloring

"""
長さ2N
何通りありますか　comboかdp
Sの各文字を赤か青で塗る
2 ** 2Nあるがこれを2 ** Nに落としたい
2NからN個選ぶ
36C18 9,075,135,300通り
意外とでかいな　これを減らす

まず構成する数字の個数が一致してないと
4
cabaacba の場合
[[1, 3, 4, 7], [2, 6], [0, 5], [], [], [],
a * 2, b * 1, c * 1
indexの選び方は左右対象でなければならない
1選ぶと7も選ばれる
3を選ばない（相手側になる）と4も選ばれない（相手側になる）
aの場所の配分は
1, 3 + 4, 7でも1, 7 + 3, 4でもいい
他の文字との位置関係が大事

もちろん全通り出すのは無理
左から右に読んだ文字列と右から左に読んだ文字列が一致するとは
最終的には2 ** Nでいい
明らかダメそうなやつを削る
もちろん全ての文字を使わないといけない
掛け算する形になると思う

cabaacba で最初のcを選んだら最後のbaが青になるのは許されない
グループ１になる組み合わせとグループ２になる組み合わせの裏表
順番があるのでindexをとってうにうにはできない

各要素を赤か青か　これを2 ** 18
2 ** Nまでしかできない　2 ** Nを
fore = S[:N]
back = list(reversed(S[N:])) の両方でやってdict

やってることはただのbit全探索半分全列挙
"""

string = 'abcdefghijklmnopqrstuvwxyz'
N = getN()
S = list([ord(i) - ord('a') for i in input()])

fore = S[:N]
back = list(reversed(S[N:]))

# 26進数シリーズ
# アルファベット → 数値
def alpha2num(alpha):
    num=0
    for index, item in enumerate(list(alpha)):
        num += pow(26, len(alpha) - index - 1) * (ord(item) - ord('a') + 1)
    return num

# 数値 → アルファベット
def num2alpha(num):
    if num <= 26:
        return chr(96 + num)
    elif num % 26 == 0:
        return num2alpha(num // 26 - 1) + chr(122)
    else:
        return num2alpha(num // 26) + chr(96 + num % 26)

def array2num(array):
    num = 0
    for index, item in enumerate(array):
        num += pow(26, len(array) - index - 1) * (item + 1)
    return num

l = defaultdict(lambda: defaultdict(int))
for bit in range(1 << N):
    g1 = [] # 赤色
    g2 = [] # 青色
    for i in range(N):
        if bit & (1 << i):
            g1.append(fore[i])
        else:
            g2.append(fore[i])
    g1 = array2num(g1)
    g2 = array2num(g2)
    l[g1][g2] += 1

ans = 0
for bit in range(1 << N):
    g1 = [] # 赤色
    g2 = [] # 青色
    for i in range(N):
        if bit & (1 << i):
            g1.append(back[i])
        else:
            g2.append(back[i])

    g1 = array2num(g1)
    g2 = array2num(g2)
    ans += l[g1][g2]

print(ans)
