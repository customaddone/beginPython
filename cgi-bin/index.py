from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right

import sys
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

mod = 10 ** 9 + 7
MOD = 998244353
sys.setrecursionlimit(1000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# 第二回日本最強プログラマー学生選手権 F - Max Matrix
# 差分をとって数えあげ

"""
2列の配列をいじいじする
N * M個について、max値の合計は？

0 0
0 0
各gridの持つ値は
0 0
0 0

10 0
 0 0

20 0
 0 0

10 0
20 0

10 0
40 0
[1][0]の値が増える
20 * (自分より小さなAの値のかず) - 現在の値　だけ増える
AはBにoverallするものとする
Aは元の数より大きい~自分以下の数の個数について
Bは元の数以上の~自分未満の数の個数について
マイナスは
A: Bの元の値以上~次の値未満の値について
B: Aの元の値より大きな~次の値以下の
"""

N, M, Q = getList()
que = [getList() for i in range(Q)]
# 座圧
code = sorted(list(set([0] + [i[2] for i in que])))
code = {code[i]: i + 1 for i in range(len(code))}

A = [0] * (N + 1)
B = [0] * (M + 1)
a_cnt, b_cnt = BIT(len(code)), BIT(len(code))
a_sum, b_sum = BIT(len(code)), BIT(len(code))
# 初期設定
a_cnt.add(code[0], N)
b_cnt.add(code[0], M)

ans = 0
for t, x, y in que:
    # a_cntが増える b_cntを見る
    if t == 1:
        # 変更前
        bef_ind = code[A[x]]
        a_cnt.add(bef_ind, -1)
        a_sum.add(bef_ind, -A[x])
        bef_p = A[x] * b_cnt.get(bef_ind + 1)
        # 変更
        A[x] = y
        aft_ind = code[A[x]]
        a_cnt.add(aft_ind, 1)
        a_sum.add(aft_ind, A[x])
        aft_p = A[x] * b_cnt.get(aft_ind + 1)
        # ふえる処理
        ans += aft_p - bef_p
        # へる処理
        ans -= b_sum.get(aft_ind + 1) - b_sum.get(bef_ind + 1)
    else:
        # 変更前
        bef_ind = code[B[x]]
        b_cnt.add(bef_ind, -1)
        b_sum.add(bef_ind, -B[x])
        bef_p = B[x] * a_cnt.get(bef_ind)
        # 変更
        B[x] = y
        aft_ind = code[B[x]]
        b_cnt.add(aft_ind, 1)
        b_sum.add(aft_ind, B[x])
        aft_p = B[x] * a_cnt.get(aft_ind)
        # ふえる処理
        ans += aft_p - bef_p
        # 減る処理
        ans -= a_sum.get(aft_ind) - a_sum.get(bef_ind)
    print(ans)

# DigitalArts プログラミングコンテスト2012 C - Chokutter

"""
クエリを先読みしそう
関係があるのは自分とその子要素だけ

つぶやくたびに自身とフォロー先のつぶやきが1増える
これを高速に計算　二分探索とかしたい

その人がk以上呟いてるか
それ以後全てのツイートに反応する

クエリの数に限りがあるのでクエリ基準で二分探索で数えあげすればいい
区間和は尺取りまたは二分探索を考える
"""

N, M, K = getNM()
tw = [[] for i in range(N + 1)]
q = []
d = defaultdict(list)
cnt = [0] * (N + 1)

for i in range(M):
    s = list(input().split())
    if s[0] == 't':
        tw[int(s[1])].append(i)
        cnt[int(s[1])] += 1
    else:
        n1, n2 = int(s[1]), int(s[2])
        if n1 > n2:
            n1, n2 = n2, n1
        if s[0] == 'f':
            d[(n1, n2)].append(i)
        else:
            d[(n1, n2)].append(i) # すでにフォロー関係にあるのはフォローできないので

# n1とn2の関係について調べる
for (n1, n2), l in d.items():
    l.append(inf)
    # 奇数個目がスタート、偶数個目がゴール
    for i in range(0, len(l), 2):
        if l[i] == inf:
            continue
        # n1の発言により増えるn2の分
        cnt[n2] += bisect_left(tw[n1], l[i + 1]) - bisect_left(tw[n1], l[i])
        # n2の発言により増えるn1の分
        cnt[n1] += bisect_left(tw[n2], l[i + 1]) - bisect_left(tw[n2], l[i])

cnt.sort(reverse = True)
print(cnt[K - 1])
