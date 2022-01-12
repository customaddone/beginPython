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
def getListGraph():
    return list(map(lambda x:int(x) - 1, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353
# sys.setrecursionlimit(10000000)
inf = float('inf')
eps = 10 ** (-15)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

"""
F2空間上のrank, 単位行列を作るベクトルの組み合わせを教えてくれる
rankより向こうのinvはただの残骸
n = rankのとき
[1, 0, 0...]: A[P[j0]](j0はinv[0]のうちフラグが立っているindex)
[0, 1, 0...]: A[P[j1]](j1はinv[1]のうちフラグが立っているindex)
...

# is_extended 連立方程式を解くなど、最後の行を操作したくないときにFalseにする
"""

def gauss_jordan_mod2(array, is_extended = False):
    A = deepcopy(array)
    H = len(A) # 縦
    W = len(A[0]) # 横
    P = [i for i in range(H)] # 今どれがどこ？
    inv = [[0] * W for i in range(H)] # 逆行列
    rank = 0
    # 一つ目のベクトル、二つ目のベクトル...を見ていく
    for col in range(W):
        if is_extended and col == W - 1:
            break
        pivot = -1
        # 縦に見ていきcol個目のフラグが立っているベクトルが見つかれば
        for row in range(rank, H):
            if A[row][col]:
                pivot = row
                break
        # col列にフラグがなかったら飛ばす
        if pivot == -1:
            continue

        # 行を入れ替え
        A[pivot], A[rank] = A[rank], A[pivot]
        P[pivot], P[rank] = P[rank], P[pivot]
        inv[pivot], inv[rank] = inv[rank], inv[pivot]
        inv[rank][col] = 1 # 逆行列作成のため

        # 掃き出す　縦に動く
        for row in range(H):
            # 自分のとこ以外
            if row == rank:
                continue
            if A[row][col]:
                for col2 in range(W):
                    A[row][col2] ^= A[rank][col2]
                    inv[row][col2] ^= inv[rank][col2]

        rank += 1

    return A, rank, P, inv

# N行M列　最大rank Mの行列
N, M = 13, 6
A = \
[[1, 0, 1, 0, 1, 0],
[1, 0, 0, 1, 1, 0],
[0, 0, 1, 1, 1, 1],
[0, 1, 0, 0, 1, 0],
[1, 1, 1, 0, 1, 0],
[0, 0, 1, 1, 0, 1],
[0, 0, 0, 1, 1, 1],
[1, 1, 1, 1, 1, 1],
[1, 0, 1, 0, 1, 1],
[1, 1, 0, 1, 0, 0],
[1, 0, 0, 0, 1, 1],
[1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 1, 0]]

mat, rank, p, mat_inv = gauss_jordan_mod2(A)
psuedo = []

# 説明の通りに単位行列を作ってみる
# 作れるのはrank個だけ
for i in range(rank):
    vec = [0] * M
    use = []
    for j in range(M):
        # inv[i][j]にフラグが立っているならA[P[j]]をxorする
        if mat_inv[i][j]:
            use.append(p[j])
            for k in range(M):
                vec[k] ^= A[p[j]][k]

    print(use)
    print(vec)
