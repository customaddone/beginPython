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
# sys.setrecursionlimit(1000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# edufo 109 C - Robot Collisions

"""
スピード1で右か左かに移動
整数上で出会わなければ何も起こらない

まずロボット2つで考える
ロボット2つの差が偶数で、互いに近づくなら消滅する
差が偶数であればいずれぶつかる
なので場所の偶奇でグループ分け

グループ内だと全てのロボットは互いにぶつかりあう　ロボットが奇数個だと1つ残るが
ペアを組んで行ってどのペアが一番衝突が早いか　それを取り除く
・互いに向かい合う
・互いに背を向ける
・同じ方向

互いに向かい合う　一番近いのと一番最初にぶつかる　距離 // 2
互いに背を向ける　一番遠いのと一番最初にぶつかる　(2N - 距離) // 2
同じ方向　端までの距離が短い方 + 距離 // 2　= 端までの距離の平均

互いに背を向ける　が一番遅い
・互いに向かい合う R と L
・同じ方向 R同士L同士
の2つをまず考える
同じ方向　の一番距離が短いのはすぐわかる　一番右にある2つと一番左にある2つ
互いに向かい合う　はO(N)かければ何とか... Rについて一番近いLを探す
互いに独立となる消し方を考える　順番は関係内容な
それぞれのRについて互いに向かい合う　の最小値を求めておく　heapに入れる
最小のものから取り出す　それがRR,LLより小さければ消す
RRが小さい, LLが小さい　は消して記録しておく
RRが消えている　探索は行わない
LLが消えている　

まず・互いに向かい合う R と Lから消えていく
"""

T = getN()
for _ in range(T):
    N, M = getNM()
    odd_r, even_r = [], []
    odd_l, even_l = [], []
    R = []
    P = getList()
    D = input().split()
    for i in range(N):
        R.append([P[i], D[i], i])

    for p, d, ind in R:
        if p % 2 == 0:
            if d == 'R':
                even_r.append([p, ind, 0])
            else:
                even_l.append([p, ind, 1])
        else:
            if d == 'R':
                odd_r.append([p, ind, 0])
            else:
                odd_l.append([p, ind, 1])

    ans = [-1] * N
    def calc(R, L):
        all = sorted(R + L)
        r_o, l_o = [], deque([])
        for p, ind, d in all:
            # right
            if d == 0:
                r_o.append([p, ind])
            else:
                if r_o:
                    p_e, ind_e = r_o.pop()
                    ans[ind] = ans[ind_e] = abs(p - p_e) // 2
                else:
                    l_o.append([p, ind])

        # 同じ向き
        while len(r_o) > 1:
            p1, i1 = r_o.pop()
            p2, i2 = r_o.pop()
            ans[i1] = ans[i2] = M - (p1 + p2) // 2

        while len(l_o) > 1:
            p1, i1 = l_o.popleft()
            p2, i2 = l_o.popleft()
            ans[i1] = ans[i2] = (p1 + p2) // 2

        # 背を向け
        if r_o and l_o:
            p1, i1 = r_o.pop()
            p2, i2 = l_o.popleft()
            ans[i1] = ans[i2] = M - abs(p1 - p2) // 2

    calc(even_r, even_l)
    calc(odd_r, odd_l)
    print(*ans)
