from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
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

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# ユークリッド距離を求める
def euc(px1, py1, px2, py2):
    return math.sqrt((px2 - px1) ** 2 + (py2 - py1) ** 2)

# 交点がない場合は使えないよ
def cross(x1, y1, x2, y2, r1, r2):

    # cosθを求める
    d = euc(x1, y1, x2, y2)
    cos = (r1 ** 2 + d ** 2 - r2 ** 2) / (2 * r1 * d)
    # |P1H|
    d1 = r1 * cos

    # |AH|
    d3 = math.sqrt(r1 ** 2 - d1 ** 2)
    # P1 ~ Hのベクトル
    e = (x2 - x1, y2 - y1)
    e1 = (e[0] * d1 / d, e[1] * d1 / d)
    # A ~ Hのベクトル
    # eを90度回転させたものにd3 / dをかける
    e2u, e2d = ((e[1] * (-1)) * d3 / d, e[0] * d3 / d), (e[1] * d3 / d, (e[0] * (-1)) * d3 / d)

    return (x1 + e1[0] + e2u[0], y1 + e1[1] + e2u[1]), (x1 + e1[0] + e2d[0], y1 + e1[1] + e2d[1])

"""
二分探索　っぽいが
半径をrに設定した時にクリアできるか

幅200の道がある
釘がある
釘をうまく避けてゴールに行けるか

釘が少ないケース、釘が一直線なケースを考える
釘が1本なら
上下どちらかの幅が大きい方が答え
釘2本　真上にできる場合は
3つある幅のうち一番大きいやつ
真左にある場合は上下どちらかの幅が大きい方
左上にある場合は
点ABとの距離、上下の幅のうち大きいやつ
釘3本
ルートによって無視していい釘が出てくる
平面走査するか x = iを突破できるか

上下xだけ内側に線を引く
各釘から半径xの円を描く
隙間は残っているか
隙間がなくなるケース
どうやって判定する
円と円の間を通過するか確かめるか
考えるのは2点間
x1 ~ x2を通過できるか
釘によって三角形ができるけど、その三角形に入れるかどうか

接触するなら円弧の反対側まで被害が広がる
まず2つの円が交わる点を計算する
ひし形になる
二つの円の中心から垂直に

接する　場合は通れる　誤差はちょっとであればOKぽいので
"""

# print(cross(0, 0, 1, -1, 3, 2))
# 2つの円の中心、円の大きさから禁止地点を割り出す
def forbit(x1, y1, x2, y2, rad):
    r = rad + 10 ** -12
    if euc(x1, y1, x2, y2) > 2 * r:
        return []
    p1, p2 = cross(x1, y1, x2, y2, r, r)
    print(p1, p2)
    # そのxについて禁止区間は
    def y_calc(y1, y2):
        return [min(y1, y1 - 2 * (y1 - y2)), max(y1, y1 - 2 * (y1 - y2))]

    res = []
    res.append([p1[0]] + y_calc(p1[1], y1))
    res.append([p1[0]] + y_calc(p2[1], y1))
    res.append([p2[0]] + y_calc(p1[1], y2))
    res.append([p2[0]] + y_calc(p2[1], y2))

    return res

N = getN()
P = [getList() for i in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        print(forbit(P[i][0], P[i][1], P[j][0], P[j][1], 50))
