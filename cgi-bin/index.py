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
sys.setrecursionlimit(1000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

"""
2nの長さの棒がある　n個のペアに分ける
前からdpしてみる？
現在のポイントから適当な場所に繋いだ場合にその内側と外側で何種類できるか
2i個目の頂点から繋げる頂点は必ず奇数個目の頂点になる
長さが2iの時の繋ぎ方の個数は一定
inside条件とsame条件がある same条件の場合求めるのが簡単
same条件を満たしたものをencloseしてもいい
same条件はiの約数の数だけ

inside条件をする
何重かencloseしていい
sameが1, sameが2...
連続するi個をとるとsameがiのグループを作れる　combination
same1のみでやると？
encloseは外側にのみ

内側と外側で考える
長さiの内側の作り方、i-1の作り方...　これは約数の個数　外側を
外側左右に1個ずつ置く
外側なし　iの約数の個数だけ
外側あり　内側のsize一つにつき外側の結び方が1つある
"""

N = getN()
same = [0] * (N + 1)
for i in range(1, N + 1):
    for j in range(i, N + 1, i):
        same[j] += 1
dp = [0] * (N + 1)
acc = [0] * (N + 1)

for i in range(1, N + 1):
    dp[i] = same[i] + acc[i - 1]
    dp[i] %= MOD
    acc[i] = dp[i] + acc[i - 1]
    acc[i] %= MOD
print(dp[N])
