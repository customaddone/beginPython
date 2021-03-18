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

# ABC195 F. Coprime Present

"""
A以上B以下　幅は72以下
A, Bがでかい
連続する数　ここポイント
連続する数は互いに素

Q:どの数とどの数をペアにしてはいけないか
偶数は一緒にしてはいけない　偶数のどれか1つ or 全くない
奇数はどんな感じ
3の倍数の場合は6つ前、6つ後ろと一緒になってはいけない
5の倍数は10こ前、10こ後ろと一緒になってはいけない...
2の倍数が入る通り、3の倍数が入る通り...をdp
bit dpすれば
2 4
0b1 2は3の倍数
0b10 3は3の倍数
0b1 4は2の倍数
"""

A, B = getNM()
# 72までに素数が20個あります
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
N = [i for i in range(A, B + 1)]
L = len(N)

# 各数字をbit棒に変換する
for i in range(L):
    # なんの約数かをbit形式で記録
    opt = 0
    for j in range(20):
        if N[i] % prime[j] == 0:
            opt += (1 << j)
    N[i] = opt

prev = [0] * (1 << 20)
prev[0] = 1 # 空集合が1
for i in range(L):
    next = [0] * (1 << 20)
    # 配るdpで
    for bit in range(1 << 20):
        next[bit] += prev[bit] # 何も足さない場合
        if not bit & N[i]: # 共通の約数がなければ
            next[bit | N[i]] += prev[bit]
    prev = next

print(sum(prev))
