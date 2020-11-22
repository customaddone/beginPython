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

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

"""
連結無向グラフ
多重辺はあるかも 1 - 2 1 - 2 みたいな
良い書き込みかたがあるかどうか

それぞれの頂点に整数を書き込む 同じ数字でもいい
辺の両端に書かれた整数をx、yとするとx, yのどちらか一方のみがcと一致しないと辺が落ちる
連結でいられるか
連結である条件
"""
