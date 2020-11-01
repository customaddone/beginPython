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

# ARC027 B - 大事な数なのでZ回書きまLた。

"""
N桁の数字を覚えて置きたい
大文字アルファベットがそれぞれ0 ~ 9のうちのどれかの数字に対応している

Unionfindとか最大流とか
N <= 18 bit　dpまで狙える

覚えておく数字について何通り考えられるか
10 ** 18通りの数字があるがその中で？
ただし制約がある
候補を絞って全探索

アルファベットと各数字を対応させる通りは10 ** 26通り
4
1XYX
1Z48 の場合
X - Zは同じ
Y - 4は同じ
X - 8は同じ
なのでZ - 8
S1とS2に出てくる文字がどの数字と対応しているかを求めればいい

6
PRBLMB
ARC027 の時

P - A
B - C
L - 0
M - 2
B - 7
B - 7よりC - B - 7
P - AグループとRに対応する数字を求めればいい

UnionFindする
出現した文字のリスト
出現した文字が何の数字か
"""

N = getN()
S1 = input()
S2 = input()
str_c = [0] * 26 # 文字が出現したか
number = [-1] * 26 # どの文字が割り当てられているか
ascii_uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

U = UnionFind(26)
# 通りが0の場合もあるが
for i in range(N):
    # 両方文字ならグループ化
    if (S1[i] in ascii_uppercase) and (S2[i] in ascii_uppercase):
        str_c[ord(S1[i]) - ord('A')] = 1
        str_c[ord(S2[i]) - ord('A')] = 1
        U.union(ord(S1[i]) - ord('A'), ord(S2[i]) - ord('A'))
    if not (S1[i] in ascii_uppercase) and not (S2[i] in ascii_uppercase):
        if int(S1[i]) != int(S2[i]): # そもそも数字同士が違う
            print(0)
            exit()

# グループ化し終わったら数字を対応させる
# あるグループにアクセスするときはU.find(i)でアクセスする
# するとグループの代表者が出てきてくれる
# そのグループの代表者にどの文字と対応しているか、先頭の文字かを尋ねる
for i in range(N):
    if (S1[i] in ascii_uppercase) and not (S2[i] in ascii_uppercase): # S1が文字
        str_c[ord(S1[i]) - ord('A')] = 1
        if number[U.find(ord(S1[i]) - ord('A'))] == -1: # 未登録
            number[U.find(ord(S1[i]) - ord('A'))] = int(S2[i])
        else:
            if number[U.find(ord(S1[i]) - ord('A'))] != int(S2[i]): # 矛盾する
                print(0)
                exit()

    if not (S1[i] in ascii_uppercase) and (S2[i] in ascii_uppercase): # S2が文字
        str_c[ord(S2[i]) - ord('A')] = 1
        if number[U.find(ord(S2[i]) - ord('A'))] == -1:
            number[U.find(ord(S2[i]) - ord('A'))] = int(S1[i])
        else:
            if number[U.find(ord(S2[i]) - ord('A'))] != int(S1[i]):
                print(0)
                exit()

first = [0] * 26 # 一番前の数字か
if (S1[0] in ascii_uppercase):
    first[U.find(ord(S1[0]) - ord('A'))] = 1
    if number[U.find(ord(S1[0]) - ord('A'))] == 0: # 一番最初の文字に0が登録されていたら
        print(0)
        exit()

if (S2[0] in ascii_uppercase):
    first[U.find(ord(S2[0]) - ord('A'))] = 1
    if number[U.find(ord(S2[0]) - ord('A'))] == 0:
        print(0)
        exit()

ans = 1
# 未登録の数字については0 ~ 9または1 ~ 9になる可能性がある
for i in range(26):
    if str_c[i] and number[U.find(i)] == -1: # 未登録なら
        if first[U.find(i)]:
            ans *= 9 # 1 ~ 9
            number[U.find(i)] = 10
        else:
            ans *= 10
            number[U.find(i)] = 11

print(ans)

# AtCoder Petrozavodsk Contest 001 D - Forest

"""
森です Unionfind?
森を連結にする最小コスト
制約的に最大流無理

Impossibleの条件
一つ繋ぐごとに頂点が２つ減り、森が一つ減る
森が2個以上でもう繋げなくなったらimpossible

小さい例から考える
7 5
1 2 3 4 5 6 7
3 0
4 0
1 2
1 3
5 6　の時

1 - 2 - 3 - 4 - 5
6 - 7

1と6を繋げばいい
1 - 2
3 - 4 - 5
6 - 7
の場合
motherを一つ決める(例えば1 - 2)
childは3 - 4 - 5, 6 - 7
motherの一番小さい奴とchildの一番小さい奴を消費して連結する
グループ分けする
[1, 2]
[3, 4, 5]
[6, 7] 全部ヒープキュー
小さい2つを消費(ansに加える)
併合

motherは一番でかい奴から！！！
ゆとりのある順に並べる

motherは慎重に決めないといけない
各グループの先頭列をみる
小さい順に使いたい
各グループの先頭は必ず使う
合計で2 * (g_n - 1)頂点いる
g_n - 1については各グループの先頭にしないといけない　他のは？
あとは自分以外のところから自由に　全てmotherの所有物
足すのはg_n - 1回だけでいい

groupの隣同士を併合するだけでいい
要素にグループ番号をつけて前から並べる
unionしてなかったら
motherは決めない

先頭の奴は絶対に使う
あとは小さい順から　自分以外のとこの適当なグループの先頭に繋げてやればよい

UnionFindの問題は先頭とそれ以外　という考え方をする
"""

N, M = getNM()
A = getList()
que = [getList() for i in range(M)]

# グループ分け
U = UnionFind(N)
for a, b in que:
    U.union(a, b)

group = [[] for i in range(N)]
for i in range(N):
    group[U.find(i)].append(A[i])
group = [sorted(i) for i in group if len(i) > 0]

if len(group) == 1:
    print(0)
    exit()

g_n = len(group)

ans = 0
l = []

# 先頭の絶対使う奴と二番手以降の遊撃隊に分ける
for i in range(g_n):
    ans += group[i][0]
    while len(group[i]) > 1:
        u = group[i].pop()
        l.append(u)

l.sort(reverse = True)

# 残りの頂点は小さい順
for i in range(g_n - 2):
    if l:
        u = l.pop()
        ans += u
    else:
        print('Impossible')
        exit()
print(ans)
