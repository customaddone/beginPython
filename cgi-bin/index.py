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
N <= 5000
1 ~ Nを空でない1 ~ K個のグループに分ける
O(NK)でやる
K個のグループに分ける場合、やり方はN^K通りから空のやつを引く　でできそう
N^K // fact(K)(グループを区別しない)
つまりN^K - N^(K - 1)(K - 1個のグループの作り方を引く)

mod M これとこれが同じグループに入っている　を引く
iとjが同じグループに入っている通り　(N - 2)^K通り
全てのcond1 & cond2... を求められればいける

n人を別々にk個のグループに分ける kPn
これを全てのグループ分やる

集合1が空でない & 集合2が空でない... =
not 集合1が空 or 集合2が空...
k - 空集合の個数 P n1 * k - 空 P n2...
条件をi個（空集合をi個選ぶ）選ぶ通りはkCi通り
"""
