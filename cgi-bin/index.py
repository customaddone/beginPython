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

# 3 2 2 1 5
#     2　を消すと
# 3 2 1 5
# 最小回数を探す
# O(n^2)でやれ dpできる
# 前から単調増加でk個指定する
# それが目標達成できるように
# dpだろう　ここまで進んだ時にいくつクリアしているか
# セグ木使ってもいい
# 消す
# 消さずに指定する　消さず指定しない

# n回消しで行けるか
# ? 2 3 ? 5　みたいな感じで　まず連続するn個を探す
# 次にどこについて　なんでもいい　にするか

T = getN()
for _ in range(T):
    N, K = getNM()
    A = [0] + getList()

    # 現在までにj個消した時の最大適合
    prev = [0] * (N + 1)

    # i個目まで進んだ
    for i in range(1, N + 1):
        next = [0] * (N + 1)
        # 前回までにi個まで消した
        for j in range(i):
            # i個目を削除する場合
            next[j + 1] = max(next[j + 1], prev[j])
            # 削除しない場合　適合するかチェック
            # 今回のはi - j個目　これがA[i]と一致するかチェック
            next[j] = max(next[j], prev[j] + ((i - j) == A[i]))

        prev = next

    for i in range(N + 1):
        if prev[i] >= K:
            print(i)
            break
    else:
        print(-1)
