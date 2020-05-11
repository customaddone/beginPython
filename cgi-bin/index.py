def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

from collections import defaultdict, deque
from sys import exit
import heapq
import math
import copy
from bisect import bisect_left, bisect_right

import sys
# sys.setrecursionlimit(1000000)
# list(map(int, input().split()))
mod = 10 ** 9 + 7

# K以上はそれ以降の何が足されようが同じ
# K以下とそれ以上にグルーピング
# ここまで足すとK以上になる点を求める→二分探索
N, K = getNM()
A = getList()

ans = 0
# 累積和
listalta = [0]
for i in range(N):
    # i個目まで足し合わせるとlistalta[i]になる
    # 累積和は最初何も足し合わせない時の値(0)が入る
    listalta.append(listalta[i] + A[i])
for i in range(N):
    # i + 1が連続部分列の起点
    # listalta[i]: i + 1以前（1 ~ iまで）を足した合計
    # index: i + 1からindexまで足し合わせるとギリギリK以上になる点
    index = bisect_left(listalta, K + listalta[i])
    if index <= K:
        ans += N - index + 1
print(ans)
