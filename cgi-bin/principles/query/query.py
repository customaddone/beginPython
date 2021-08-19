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

"""
まずは愚直に行ってみる→計算量が多くなる

クエリが１つの頂点に対する操作にできるorまとめて計算できる
現在の状態を記録しておいて、機会があれば集計する DigitalArts C - Chokutter
1操作ごとの差分を取って集計する F - Max Matrix

クエリが複数の頂点に対する操作の場合
平方分割ができるか試してみる
対象となる頂点が多くないのでは？　ABC213 E - Stronger Takahashi

頂点が切断されない場合
マージテクUFを使える F - Cofluence

クエリを処理する問題はクエリ先読みができるかを試してみる
頂点同士の関係が閉路グラフみたいになる場合
平方分割もできそう
最終での足し算引き算になる場合も
"""
