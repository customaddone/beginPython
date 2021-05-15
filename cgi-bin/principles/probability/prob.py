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
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

"""
全ての〜について条件を満たす通りの数を求める = 全ての通り * 条件を満たす確率
通りの数を求める問題は確率の問題に帰着できる

C - Ordinary Beauty
全ての通りがn^m通りあるが...
j番目の数字をiにした時、任意のi, jにおいて右隣には1 ~ Nが等確率で出ると考える
またj番目の数字をiにした時j + 1に何が出るかとj + 1番目の数字をiにした時j + 2に何が出るか
は互いに独立

ABC008 C - コイン
i番目が面か裏かはこれ以前のC[i]の約数が書かれているコインの枚数に依存する
偶数枚なら面
奇数枚なら裏

つまりC[i]とその約数が書かれているコインのみの並びを考える
その個数をk枚とすると
まずC[i]の場所をk通りから選ぶとすると
1, 3, 5...番目を選べば面になる
つまりi番目のコインが面になる確率は(k + 1) // 2 / kになる
"""
