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
def rand_N(ran1, ran2):
    return random.randint(ran1, ran2)
def rand_List(ran1, ran2, rantime):
    return [random.randint(ran1, ran2) for i in range(rantime)]
def rand_ints_nodup(ran1, ran2, rantime):
  ns = []
  while len(ns) < rantime:
    n = random.randint(ran1, ran2)
    if not n in ns:
      ns.append(n)
  return sorted(ns)

def rand_query(ran1, ran2, rantime):
  r_query = []
  while len(r_query) < rantime:
    n_q = rand_ints_nodup(ran1, ran2, 2)
    if not n_q in r_query:
      r_query.append(n_q)
  return sorted(r_query)

from collections import defaultdict, deque, Counter
from sys import exit
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 998244353

#############
# Main Code #
#############

def prime_factorize(n):
    divisors = []
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

# ABC052 C - Factors of Factorial
N = getN()

# N!の因数 = (2の因数) + (3の因数)...
# 約数の個数 = (因数の個数 + 1) * (因数の個数 + 1)...
mod = 10 ** 9 + 7
ans = 1
# それぞれの因数となる素数の数をセットする
dp = [0] * (N + 1)

for i in range(1, N + 1):
    for j in prime_factorize(i):
        if j[0] > 1:
            dp[j[0]] += j[1]
# 約数の数:それぞれの因数の(因数の数 + 1)を掛け合わせたもの
for i in dp:
    if i > 0:
        ans = (ans * (i + 1)) % mod
print(ans % mod)

# ABC090 D - Remainder Reminder
# 数え上げ
N, K = getNM()
sum = 0
for b in range(1, N + 1):
    opt1 = (N // b) * max(0, (b - K))
    if K == 0:
        opt2 = N % b
    else:
        opt2 = max(0, (N % b) - K + 1)
    sum += (opt1 + opt2)
print(sum)

# 094 D - Binomial Coefficients
# combはrを真ん中に設定すると大きくなる

N = getN()
A = getList()
A.sort()

max = max(A)
index = bisect_left(A, max / 2)
if abs((max / 2) - A[index]) < abs((max / 2) - A[index - 1]):
    ans = [max, A[index]]
else:
    ans = [max, A[index - 1]]
print(*ans)

# ABC096 D - Five, Five Everywhere
# 素数はmod nでグルーピングできる
N = getN()

# エラストテネスの篩
prime = [2]
max = 55555
limit = int(math.sqrt(max))
data = [i + 1 for i in range(2, max, 2)]

while limit > data[0]:
    prime.append(data[0])
    data = [j for j in data if j % data[0] != 0]
prime = prime + data

prime = sorted(prime)

prime = [i for i in prime if i % 5 == 1]
print(*prime[:N])

# ABC110 D - Factorization
# 長さNのaはいくつあるか
# N = 3, M = 6の時
# 1 | 1 | 1　があらかじめある
# 因数 2, 3についてどこの部屋に収納するか
N, M = getNM()

if M == 1:
    print(1)
    exit()

#  因数分解
num = prime_factorize(M)

ans = 1
for i in num:
    ans *= cmb_2(N + i[1] - 1, i[1])
    ans %= mod
print(ans)
