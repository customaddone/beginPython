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
# treeの計算量
tree一回流すのは意外と計算量いる
10 ** 5のtreeをlogN回は流せない
10 ** 6だとせいぜい2, 3回

頂点0からuまできた時の現在の状態（0からの距離、通ったedgeの本数、edgeの色の種類等）はdfsで求められる
全て保存はできないのでクエリ先読みなどして必要な分だけとる

最小全域木にできるかどうか: ある点からいくつかの点を経由して全ての点に辿りつけるか

# 「どちらか一方を選ぶ場合」にはグラフで考えるのがいい
a, bについてどちらか一方が選べる
各カードが何を担当するか

色ごとにくくって考える
どちらか選択する問題はグラフに帰着できる
辺の両端のどちらかを獲得する

いくつか連結グラフのグループができるが
それが木になっている場合　木のサイズ - 1を獲得できる
木になっていない場合、橋ではない辺1つを消費して上では獲得できなかった頂点1つを獲得する
+ n - 1(上のと一緒)
"""
