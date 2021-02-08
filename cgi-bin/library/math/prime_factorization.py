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

# 素因数分解
def prime_factorize(n):
    divisors = []
    # 27(2 * 2 * 7)の7を出すためにtemp使う
    temp = n
    for i in range(2, int(math.sqrt(n)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                # 素因数を見つけるたびにtempを割っていく
                temp //= i
            divisors.append([i, cnt])
    if temp != 1:
        divisors.append([temp, 1])
    if divisors == []:
        divisors.append([n, 1])

    return divisors

# [[2, 3], [3, 1]]
print(prime_factorize(12))

# エラストテネスの篩
prime = [2]
max = 12
limit = int(math.sqrt(max))
data = [i + 1 for i in range(2, max, 2)]

while limit > data[0]:
    prime.append(data[0])
    data = [j for j in data if j % data[0] != 0]
prime = prime + data

# [2, 3, 5, 7, 9, 11]
print(prime)

# 調和級数
# ABC170 D - Not Divisible
# A内の全てが素数ならエラストテネスにO(N ** 2)かかる

# Amaxが小さいなぁ...
# Amaxが小さいので、長さAmax + 1のテーブルを用意し、Aを小さい順に
# A1の倍数を消す、A2の倍数を消す...を繰り返す
# 実はそんなに計算量は増えない（調和級数) AmaxlogAmax程度
# AのソートにNlogNかかるので合計AmaxlogAmax + NlogN

N = 10
A = [33,18, 45, 28, 8, 19, 89, 86, 2, 4] # [2, 19, 33, 45, 89]

# array内に自分以外の自分の約数がないものを出す
def not_divisible(array):
    limit = max(array)
    table = [0] * (limit + 1) # Aiの倍数を書き込むテーブル
    double = [0] * (limit + 1) # Aiに何が何回出たかを書き込むテーブル
    array.sort()
    for a in array:
        double[a] += 1
        # すでにaの約数が出ている場合は飛ばす
        if table[a] > 0:
            continue
        # aの倍数2a, 3a, 4a...を書き込む
        for j in range(a * 2, limit + 1, a):
            table[j] = 1

    # 集計
    res = []
    for i in range(1, limit + 1):
        if table[i] == 0 and double[i] == 1:
            res.append(i)

    return res

print(not_divisible(A))

N = 3
A = [6, 10, 15]
# 全てのAiの要素について互いに素か
def co_prime(array):
    limit = max(array)
    table = [0] * (limit + 1) # Aに何の要素が何個あるか
    prime = [0] * (limit + 1) # 素数だけを取り出すためのテーブル
    for a in array:
        table[a] += 1
    # iで割り切れるAの要素は何個あるか
    for i in range(2, limit + 1):
        cnt = 0
        # 素数のみを探索する
        if prime[i] == 1:
            continue
        for j in range(i, limit + 1, i):
            cnt += table[j] # iの倍数であるAの要素は何個あるか調べる
            prime[j] = 1

        if cnt > 1:
            return False

    return True

print(co_prime(A))

# osk_k法
# 範囲内の数字nについて高速で素因数分解するよ
# 計算量
# 前処理: NloglogN
# 素因数分解: logN
class Osa_k():
    def __init__(self, n):
        self.sieve = list(range(n + 1))
        self.sieve[0] = 1 #素数でない
        self.sieve[1] = 1 #素数でない
        m = int(math.sqrt(n))
        for i in range(2, m + 1):
            if self.sieve[i] < i:
                continue
            for j in range(i * i, n + 1, i):
                if self.sieve[j] == j:
                    self.sieve[j] = i

    def factorize(self, n):
        prime = defaultdict(int)
        if n == 0 or n == 1:
            return (n, 1)
        opt = n
        while opt > 1:
            prime[self.sieve[opt]] += 1
            opt //= self.sieve[opt]
        return sorted(prime.items())

N = 1000
O = Osa_k(10 ** 6 + 1)

prime = defaultdict(int)
for i in range(2, N + 1):
    for j in O.factorize(i):
        prime[j[0]] += j[1]

ans = 1
for i in prime.items():
    ans *= i[1] + 1
    ans %= mod
print(ans)
