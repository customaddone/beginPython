from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import sys
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from bisect import bisect_left, bisect_right

def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

"""
期待値を求める問題
すべての場合が2^N通りある
それぞれについての穴の数がHi個ある
その総和をHとすると、答えはH / 2^N個
答えは逆元をかける

黒い頂点を全て繋ぐと求める部分木ができる
頂点iが穴あきになる場合の数
頂点iが穴あき = パス上に頂点iがある黒い点Bi, Bjがある
頂点iの子要素のうちどれか2つ以上が黒い木

子要素のうち２つ以上を選ぶ
子要素がc個あったら全てについて選ぶ/選ばないが2^C通りあるが、
一個しか選ばないor一個も選ばないを引く

黒い木である場合 2^c1 - 1
白い木である場合 1
すべての通り　2^(N - 1)
白い木しかない 1
黒い木が1つ (2^c1 - 1) + (2^c2 - 1) +...

= 2^(N - 1) - 1 - ((2^c1 - 1) + (2^c2 - 1)...)
= 2^(N - 1) - 1 - (2^(ciの大きさ)の合計) + 部分木の数
これをすべての点でやる

子要素の部分木の大きさがわかればOK
自身のサイズを返すdfs
def dfs(u, par):
    res = 1
    for v in E[u]:
        if v != par:
            res += dfs(v, u)
    return res
"""

# ABC149 F - Surrounded Nodes
# 特殊なmodでの出力方法

N = getN()
E = [[] for i in range(N)]
for i in range(N - 1):
    s, t = getNM()
    E[s - 1].append(t - 1)
    E[t - 1].append(s - 1)

ans = 0

# 2^(N - 1) - 1 - (2^(ciの大きさ) - 1の合計)
# を求めていく
def dfs(u, par):
    global ans
    res = 1
    add = pow(2, N - 1, mod) - 1
    for v in E[u]:
        if v != par:
            size_c = dfs(v, u)
            # 2^(ciの大きさ) - 1
            add -= (pow(2, size_c, mod) - 1)
            add %= mod
            res += size_c
    # 最後に親方向に行く部分木の分を引く
    add -= (pow(2, N - res, mod) - 1)
    add %= mod
    ans += add
    ans %= mod

    return res

dfs(0, -1) # 実行
deno = pow(2, N, mod)
# denoの逆元のやり方（pythonでしかできません）
# xz ≡ y(mod 10 ** 9 + 7)を満たすような　の問題で使う
print((ans * pow(deno, -1, mod)) % mod)
