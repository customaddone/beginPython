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
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# codeforces round704
# D. Genius's Gambit
# 二進数の繰り上がりについて

# a + b桁の二進数を探せ　一番上の桁は必ず1
# 両方にb個のフラグが立っている
# x - yするとその答えにフラグがk本　できるか

# まず1 - 1 = 0 繰り下がりが大変
# 100 - 1 = 11 1000 - 1 = 111

# 100
#-  1
#  11 のあと
#  110
#-   1
#  101 引き算をすると xの一番最後の1の位置が変更される
# 0 0 何も起らない
# 1 1 何も起らない　邪魔なフラグはこれで処理する
# 1 0 xの最後の1の位置が更新される kの本数が+1される
# 0 1 xの最後の1の位置が更新される kの本数が+(新しい位置 - 最後の位置 - 1)される

# 最大でa + b - 2本立てられる
# xとyのフラグを1対1対応させる
# |100|10|1000|
# |001|01|0001| みたいな感じで　この中に使われている0の個数がフラグの本数
# 結局のとこ最大本数を探す
# |100|                     |1|0|
# |001|　を一箇所作る　あとは   |1|0| で　

# 11111110
#-10111111
# 10111111 1のカウントを消費した場合でも1を作れる
# 10000
# 00001
# 01111 0の数だけ増えるが
# 1110000

# 11....0    10....0
# 01....1 or 0....01 このどちらか

# b = 1ならkの答えは0
# b >= 2の場合は 最大aの数だけ　最小0

# 1111110000000
# 1011110000001 という風にする A + B - 2個まで可能

# 1 11110000
# 1 11110000 0
# 1 01110001 7 ある位置の1か0かをスワップする

A, B, K = getNM()
if B == 1 or A == 0:
    if K == 0:
        print('Yes')
        print('1' * B + '0' * A)
        print('1' * B + '0' * A)
    else:
        print('No')
else:
    ans1, ans2 = ['1'] * B + ['0'] * A, ['1'] * B + ['0'] * A
    if K <= A: # 最後の1と0のどれかをスワップ
        ans2[B - 1], ans2[B - 1 + K] = ans2[B - 1 + K], ans2[B - 1]
    elif A < K <= A + B - 2: # 1のどこかと0の最後をスワップ
        ans2[-K - 1], ans2[-1] = ans2[-1], ans2[-K - 1]
    else:
        print('No')
        exit()

    print('Yes')
    ans1, ans2 = ''.join(ans1), ''.join(ans2)
    print(ans1)
    print(ans2)
    # print(bin(int(ans1, 2) - int(ans2, 2)))
