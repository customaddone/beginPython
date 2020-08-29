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
mod = 10 ** 9 + 7

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
