from collections import defaultdict, deque, Counter
import sys
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce, lru_cache
from bisect import bisect_left, bisect_right

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

N, K = getNM()
S = input()

if(K * 2 > N):
    print('NO')
    exit()

# ダブらない場所に長さKの同じ文字の種類と数で構成された部分があるか
def check(n, s, k, base, alp):
    # 各アルファベットをエンコード
    encode = {}
    for i, ch in enumerate(alp, 10001):
        # modは最強の2 ** 61 - 1を使う
        encode[ch] = pow(base, i, 2 ** 61 - 1)

    # 文字列の先頭からm文字、k文字目からm文字をハッシュしていく
    res = 0
    for i in range(k):
        res += encode[s[i]]
        res %= mod

    dic = {res: 0}
    # ローリングする
    for i in range(n - k):
        res += encode[s[i + k]] - encode[s[i]]
        res %= mod
        # 既出なら
        if res in dic.keys():
            # ダブってもいいなら以下はいらん
            index = dic[res]
            if index + k <= i + 1:# ダブって無いか
                return True
        else:
            dic[res] = i + 1

    return False

def rolling_hash(n, s, m):
    res = True
    # 原子根を適当に手動で乱択してね
    for base in [161971, 167329, 191911]:
        # アルファベットをランダムに並べた表でエンコード表を作る
        for alp in ['qwertyuioplkmnjhbvgfcdxsaz','qazxcsdwertfgvbnmhjyuioklp']:
            # これ一回の計算量はO(N)
            res &= check(n, s, m, base, alp)
    return res

if rolling_hash(N, S, K):
    print('YES')
else:
    print('NO')
