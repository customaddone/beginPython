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

# ABC114 C - 755
N = getN()
rength = len(str(N))
numlist = [3, 5, 7]
cnt = 0

def sevfivthr(i, strint):
    global cnt
    if i == rength:
        return
    else:
        for num in numlist:
            newstr = strint + str(num)
            if ('3' in newstr) and ('5' in newstr) and ('7' in newstr):
                if int(newstr) <= N:
                    cnt += 1
            sevfivthr(i + 1, newstr)
for i in numlist:
    sevfivthr(1, str(i))
print(cnt)

# ABC115 D - Christmas
# レベルNバーガーの下からX層目まで
N, X = getNM()

# レベルNバーガーの中間地点、全体のサイズ
cnt_burger = [[0 for i in range(2)] for i in range(51)]
cnt_burger[0] = [1, 1]
for i in range(1, 51):
    cnt_burger[i][0] = 1 + cnt_burger[i - 1][1] + 1
    cnt_burger[i][1] = cnt_burger[i][0] + cnt_burger[i - 1][1] + 1

# レベルNバーガーにパティが何枚含まれる？
cnt_patty = [0] * 51
cnt_patty[0] = 1
for i in range(1, 51):
    cnt_patty[i] = 2 * cnt_patty[i - 1] + 1

# レベルNの下からX番目までにパティが何枚含まれるか
# xが大きいのでdpはできない
def count(n, x):
    # レベル0バーガーの場合
    if n == 0 and x == 1:
        return 1

    # バーガーの一番下のパンのみ食べる場合
    if x == 1:
        return 0

    # 中間地点以前のどこかまで食べる場合
    elif 1 < x < cnt_burger[n][0]:
        # レベルn - 1バーガーの下からx - 1層目まで
        return count(n - 1, x - 1)

    # 中間地点まで食べる
    elif x == cnt_burger[n][0]:
        return cnt_patty[n - 1] + 1

    # 中間地点 ~ 最後以前のうちのどこか
    elif cnt_burger[n][0] < x < cnt_burger[n][1]:
        return cnt_patty[n - 1] + 1 + count(n - 1, x - cnt_burger[n][0])

    # 最後
    else:
         return 2 * cnt_patty[n - 1] + 1

print(count(N, X))

# ABC122 D - We Like AGC
N = getN()
# 文字の個数を求める
# 755を思い出す
# dfsする

memo = [{} for i in range(N + 1)]

# 判定用
def ok(last4):
    # 1234, 2134, 1324, 1243を調べる
    for i in range(4):
        t = list(last4)
        if i >= 1:
            t[i - 1], t[i] = t[i], t[i - 1]
        if ''.join(t).count('AGC') >= 1:
            return False
    return True

# 文字を伸ばしていく
# memo[cur][last3]:cur文字目まで決定しており、そのラスト3文字がlast3のもの
# 判定に必要なのは後ろ3文字 + ['A', 'G', 'C', 'T']
def dfs(cur, last3):
    if last3 in memo[cur]:
        return memo[cur][last3]
    # 全部決定したら
    if cur == N:
        return 1

    res = 0
    # last3に['A', 'G', 'C', 'T']をくっつけてみる
    for s in 'AGCT':
        if ok(last3 + s):
            res = (res + dfs(cur + 1, last3[1:] + s)) % mod
    memo[cur][last3] = res
    return res

print(dfs(0, 'TTT'))

# AGC009 B - Tournament

N = getN()
A = [-1, -1] + getArray(N - 1)

"""
トーナメントの深さの最小値を求めよ
何もなければbitの長さになる
a2...anは人aiとの試合で負けた

A = [1, 1, 2, 4]の場合
1が優勝（デフォルト）
2は1との試合で負けました
3は1との試合で負けました
4は2との試合で負けました
5は4との試合で負けました
1は2, 3と戦った 2, 3に勝った
2は1, 4と戦った 4に勝った
3は1と戦った
4は2, 5と戦った 5に勝った
5は4と戦った

4がネックになりそう
4をいい感じに配置して

1から辿る
1は3に勝った 深さは

各頂点をrootとした部分木のサイズを求める
A = [1, 2, 1, 3, 1, 4]の場合
1の相手は2, 4, 6 部分木の深さは4

葉から求める
5の部分木のサイズは1(葉なので)
7の部分木のサイズは1(葉なので)

3の部分木のサイズは最小で子要素の数n + 1(自分)
①3の子要素を逆順にソートする
②子要素の深さはn, n-1...1まで許容される　越えたら求める部分木のサイズが大きくなる

選手iの各相手(子要素)が[r1, r2, r3...]だとする
これらを選手iが戦った試合だけを見たトーナメント表上に配置する
深さの最小mi_resは子要素の数n + 1(自分)
ただし1回戦で戦った相手の部分木の深さがn1ならmi_res = min(mi_res, n1 - 1)
     2回戦で戦った相手の部分木の深さがn2ならmi_res = min(mi_res, n2 - 2)
     ...
と更新されていく
つまり深さが深い相手を後ろの方に配置した方がお得
"""

dist = [[] for i in range(N + 1)]
for i in range(2, N + 1):
    dist[A[i]].append(i)

def depth_cnt(x):
    l = []
    for i in dist[x]:
        l.append(depth_cnt(i))
    l.sort(reverse = True) # xが最後に勝った相手に深さが一番深いやつを持ってくるとお得
    mi_depth = len(l)
    res = mi_depth
    for i in range(mi_depth):
        # xが最後に勝った相手、xが最後から2番目に勝った相手...
        # 今回は逆にやる
        res = max(res, l[i] + i)
    return res + 1 # 部分木のサイズは最小で子要素の数n + 1(自分)

print(depth_cnt(1) - 1)
