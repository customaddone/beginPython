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

# ABC006 D - トランプ挿入ソート
n = getN()
lista = [getList() for i in range(n)]

# 最長増加部分列問題 (LIS)の問題
def lis(A):
    L = [A[0]]
    for a in A[1:]:
        if a > L[-1]:
            L.append(a)
        # このelseに引っかかった時にトランプのソートが必要
        else:
            L[bisect_left(L, a)] = a
    return len(L)
print(n - lis(lista))

# Donutsプロコンチャレンジ2015 C - 行列のできるドーナツ屋
# LISの応用

N = getN()
H = getList()

# まあBITだろう
# 逆から置くBITではない？
# 累積和？
# 個数だけ求めればいい

# 地点iからは
# i - 1起点の単純増加列
# LIS？
ans = [0] * N
L = []
# 人0 ~ iまでがどのように見えるか これを人i + 1が見る
for i in range(N - 1):
    # もしLの一番小さいやつよりH[i]が大きければ
    while L and L[-1] < H[i]:
        L.pop()
    L.append(H[i])
    ans[i + 1] = len(L)

for i in ans:
    print(i)

# ABC134 E - Sequence Decomposing
N = getN()
A = getArray(N)

def lis(A):
    L = deque([A[0]])
    for a in A[1:]:
        # Lのどの数より小さくければ
        # 繋げられるものがない
        if a <= L[0]:
            L.appendleft(a)
        else:
            # L[bisect_left(L, a) - 1]
            # Lの中のa未満の数字のうちの最大値
            L[bisect_left(L, a) - 1] = a
    return len(L)

print(lis(A))

N = 10
A = [0, 6, 9, 9, 2, 3, 4, 5, 10, 3]

ans = deque([A[0]])
for i in range(1, N):
    # ans[index] A[i]が挟みこめる場所
    # A[0] <= A[i]なら0になる
    # ans[index - 1]: A[i]未満で一番大きい数字
    index = bisect_left(ans, A[i])
    if index == 0:
        ans.appendleft(A[i])
    else:
        # 同じ数が複数ある場合は一番最後の数字が更新される
        ans[index - 1] = A[i]
print(len(ans))

# ACLC1 A - Reachable Towns

N = getN()
Q = [getList() for i in range(N)]
que = deepcopy(Q)
que.sort(key = lambda i:i[1], reverse = True)
que.sort()

# xy座標が共に大きいもの
# 順列になっている？

"""
O(n**2)
U = UnionFind(N)
for i in range(N):
    for j in range(i + 1, N):
        if que[i][1] < que[j][1]:
            U.union(i, j)
for i in range(N):
    print(U.count(i))
"""
#　ソート方法はこれでOK
# やらなくていい探索がある　それを減らす
# 4 3
# 4 1
# 4 2
# 3 1
# 3 2
# 1 2 これだけいる

# 4 3 1 2でi < jになるものをペアに
# 1とペアにできるのは2, 3, 4
# 2とペアにできるのは3, 4
# 3は4
# それぞれ右側にあれば

# 6 7 5 3 2 4 1
# グループ１ 6 7
# グループ2 5
# グループ3 3 2 4
# グループ4 1
# どれか１つのグループに属する

U = UnionFind(N + 1)
group = []

for x, y in que:
    # １番目のものは必ずグループのリーダーになれる
    if not group:
        group.append(y)
        continue
    # リーダーが降順に並ぶように
    if y < group[-1]:
        group.append(y)
        continue
    opt = float('inf')
    # グループ再編成
    while group:
        # yより小さいものは全てyが所属するグループに入る
        if y > group[-1]:
            l = group.pop()
            U.union(l, y)
            opt = min(opt, l) # yが所属するグループの中のリーダー　一番最初のものが記録される
        else:
            break
    # リーダー変更
    group.append(opt)

for i in range(N):
    print(U.count(Q[i][1])) # yがiのもののサイズの大きさ　uf.funcはインデックスで呼ばなくてもいい
