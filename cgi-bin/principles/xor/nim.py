from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product, combinations_with_replacement


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

 # nim

"""
nimの勝敗判定はXOR SUMが0でなければ先手の勝ち　0なら後手の勝ち

山の数が2, 2, 2...で何個かの山からとっても各山一枚ずつしか取れないのであれば、先手の取ったものと同じものを取れば後手は勝てる
これと同じ状況を作れる
3(011), 4(100), 6(110)なら　XOR sumは1(001)
先手はどれかから1枚取ることでXOR sumを000にでき勝てる

grandy数が0じゃなければ先手の勝ち
0なら後手の勝ち

g[i] = 前の状態についてのmex 山が1つの場合
1: 次の遷移は0(g[0] = 0)より{0} g[1] = 1
2: 次の遷移は0, 1より{0, 1} g[2] = 2...
g[i] > 0であれば次の遷移にg[0]があるため先手勝利
g[i]は前の状態についてのmexなので0 ~ g[i] - 1のどこにでも遷移できる
つまりgrandy数はnimにおけるコインの枚数と考えればいい

山の数がn個ある場合
grandy数のXOR SUMが0でなければ先手の勝ち　0なら後手の勝ち

勝利条件が逆のnim
XOR sumが0(通常の逆) + 全てのコインが1枚以下でXOR sumが1(各山1枚ずつしか取れないので奇数番の人が勝つ)

x ^ x = 0 よって相手のコインと同じ枚数のコインを出せばnimを0にできる
現在のXORがこれから足される数字より大きい場合はXOR sumは0にはならない
(ARC105 D - Let's Play Nim)
"""
