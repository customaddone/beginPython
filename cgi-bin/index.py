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
INF = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

"""
期待値を求める　線型性
S <= 50 ?

文字sがリストの中にない
適当に押して発見する
1文字わからない場合　合計6文字見えない場合
1回目でわかる 1/6
2回目でわかる 1/6...
2文字わからない
2回目までにわかる 1/15
3回目までにわかる 3/15
4回目までにわかる 6/15
5回目までにわかる 10/15
6回目までにわかる 15/15

合計でi文字見えない
j文字わからない場合の期待値は求められる
最初にわからないのを全て出力するか

わからないもののとこで一旦止まる
その文字が出た時点で次に進む

完全にわかっているもの、何文字見えているか
現在まで文字sが確定で見えていて、さらにj文字わかっている
j: すでにわかってるもので対応 left - j: また探す

確定　にあった　j, leftは変化しない
未確定　にあった jが一個減る leftが一個減る
なかった jを探索する　増える
leftは今回　確定ではないものであれば減る
"""

S = input()
K = input()
n_s = len(S)
n_k = len(K)
l = set()

for i in range(n_k):
    l.add(K[i])
left = 0

prev = [-1] * 37
prev[0] = 0

for i in range(n_s - 1, -1, -1):
    next = [0] * 37
    # 探索するかしないか
    flag = False
    if S[i] in l:
        flag = True

    for j in range(left + 1):
        if prev[j] < 0:
            continue
        # 確定
        if flag:
            next[j] += (prev[j] + 1)
        # 確定ではない
        else:
            # 遷移先 left通りある
            for k in range(left):
                # 未確定の中にあった j個
                if k < j:
                    next[j - 1] += (prev[j] + 1) / left
                # なかった left - j個
                else:
                    next[k] += (prev[j] + 1 + 2 * (k - j)) / left

    if not flag:
        left += 1
        (S[i])

    print(prev, next)
    prev = [i if i > 0 else -1 for i in next]
