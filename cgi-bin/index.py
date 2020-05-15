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

from collections import defaultdict, deque, Counter
from sys import exit
import heapq
import math
import copy
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

N = getN()
F = []
for i in range(N):
    # 各数字をstrに変換
    f = list(map(str, input().split()))
    # join
    falta = ''.join(f)
    # 二進数に変換
    F.append(int(falta, 2))
P = []
for i in range(N):
    p = getList()
    P.append(p)
# -10 ** 7ぐらいだとばか小さい数にならずWA
# ばかでかい数、ばか小さい数にするときは思いっきりばかでかく、小さくしよう
ans = -10 ** 24
# bit全探索するため状態を生成
# 0000000000はダメ（必ず店は開く）
for bit in range(1, 1 << 10):
    sum = 0
    # 各お店と照合
    for i in range(N):
        open = F[i] & bit
        # 二進数表記でのフラグの数をカウント
        index = str(bin(open)).count('1')
        sum += P[i][index]
    ans = max(ans, sum)
print(ans)
