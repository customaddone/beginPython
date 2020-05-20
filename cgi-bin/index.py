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
import fractions
import copy
from itertools import permutations
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

N, K = getNM()
S = [getN() for i in range(N)]

# 条件を満たす限り右端を進める
# 条件を満たさなくなったら左端を条件を満たすまで進める
# かける数に0が混じる
if 0 in S:
    print(N)
    exit()
else:
    # r:右端
    r, ans, tmp = 0, 0, 1
    # l:左端
    for l in range(N):
        while r < N and tmp * S[r] <= K:
            # 右端を伸ばす
            tmp *= S[r]
            r += 1
        # 最大まで伸ばしてところでジャッジ
        # ここで１回ループ　左端が1進む
        ans = max(ans, r - l)
        if l == r:
            r += 1
        else:
            # 左端が1進むと同時にtmpの左端の分を削る
            tmp //= S[l]
print(ans)
