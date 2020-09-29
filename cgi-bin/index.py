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

# ABC114 D - 756
N = getN()

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
    if divisors == [] and n != 1:
        divisors.append([n, 1])

    return divisors

primli = [0] * 101
# N! の因数を計算する
for i in range(1, N + 1):
    for j in prime_factorize(i):
        primli[j[0]] += j[1]
# 約数を75個持つとは(因数 + 1)をかけ合わせると75になるということ
# 75 = 3 * 3 * 5なので例えば
# (因数aが2個 + 1) * (因数bが2個 + 1) * (因数cが4個 + 1)なら約数が75個になる
alta = []
for i in primli:
    if i != 0:
        alta.append(i + 1)

prim3 = 0
prim5 = 0
prim15 = 0
prim25 = 0
prim75 = 0
for i in alta:
    if i >= 75:
        prim75 += 1
    if i >= 25:
        prim25 += 1
    if i >= 15:
        prim15 += 1
    if i >= 5:
        prim5 += 1
    if i >= 3:
        prim3 += 1

ans = 0
if prim3 >= 1 and prim5 >= 2:
    # prim5 C 2
    ans += prim5 * (prim5 - 1) // 2 * (prim3 - 2)
if prim15 >= 1 and prim5 >= 1:
    ans += prim15 * (prim5 - 1)
if prim25 >= 1 and prim3 >= 1:
    ans += prim25 * (prim3 - 1)
if prim75 >= 1:
    ans += prim75
print(ans)

N, M = getNM()
A = [int(i) // 2 for i in input().split()]

# 4と8の場合
# 2 6 10 14 18...
# 4 12 20 28... これを２で割ると

# 1 3 5 7 9...
# 2 4 10 14... 起点が偶数と奇数なため永遠に一致しない

# 4と12なら
# 2 6 10 14 18...
# 6 18 30 42... これを２で割ると
# 1 3 5 7 9...
# 3 9 15 21...　になり、起点が奇数と奇数になるためどこかで一致する

# Aの各要素がどれも2でn回ちょうど割れる必要がある
def div_2(n):
    cnt = n
    res = 0
    while cnt > 0:
        if cnt % 2 == 0:
            cnt //= 2
            res += 1
        else:
            return res

def lcm(x, y):
    return x * (y // gcd(x, y))

judge = [div_2(i) for i in A]

if min(judge) != max(judge):
    print(0)
    exit()
L = 1
for i in range(N):
    L = lcm(L, A[i])

# Ai * 0.5, Ai * 1, Ai * 1.5...の個数 - Ai * 1, Ai * 2...の個数
print(M // L - M // (2 * L))

# ABC152 E - Flatten
# 大きい数は因数で持つ
N = getN()
A = getList()
prime_list = defaultdict(int)

for i in range(N):
    prime = prime_factorize(A[i])
    for j in prime:
        prime_list[j[0]] = max(prime_list[j[0]], j[1])

num = 1
for key, value in prime_list.items():
    num *= key ** value
    num %= mod

# 1/A[i]のmod
lim = 10 ** 6 + 1
fact = [1, 1]
inv = [0, 1]

for i in range(2, lim + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)

ans = 0
for i in A:
    opt = (num * inv[i]) % mod
    ans += opt
    ans %= mod
print(ans % mod)
