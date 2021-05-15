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

# 包除原理

"""
特性関数xa(x): x⊂Aなら1、そうじゃなければ0を返す　を考える
Uの全てについてxa(x)を求めた時の総和をn(A)とする
n(A): U内のAを満たすもの全体の集合のサイズ

A‾∩B‾∩C‾ = {x|(1 - xa(x))(1 - xb(x))(1 - xc(x)) = 1}
(1 - xa(x))(1 - xb(x))(1 - xc(x))を分解すると
(1 or - xa(x)) * (1 or -xb(x)) * (1 or -xb(x))になる

後ろの回数が偶数回の時は符号がプラス、奇数回の時はマイナスになる
A∪B∪Cを求めたい場合はそれの逆なので
後ろを取る回数が奇数回ならプラス、偶数回ならマイナスになる
n(A) ~ n(A∩B∩C)まで全てわかっていたらn(A‾∩B‾∩C‾)やn(A∪B∪C)が求められる

ABC172 E - NEQ
n(A‾∩B‾∩C‾)を求める問題
条件i: Ai = Bi
i = {1, 2}ならA1 = B1 かつ A2 = B2
この通りは
1, 2の数字を決めるMC2
(B1, B2については数字が確定する)
残りのAについて数字と場所を決める M-iPN-i
残りのBについて数字と場所を決める M-iPN-i

今回満たした条件は2つなのでプラスになる
という感じでn(A) ~ n(A∩B∩C)まで全てわかるのでn(A‾∩B‾∩C‾)は求められる
"""

N, M = getNM()
ans = 0
for i in range(N + 1):
    ans += (-1) ** (i % 2 == 1) * cmb(N, i) * factorial(M, i) * (factorial(M - i, N - i) ** 2)
print(ans % mod)
