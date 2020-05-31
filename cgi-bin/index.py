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
import copy
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

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
for i in range(1, N + 1):
    for j in prime_factorize(i):
        primli[j[0]] += j[1]
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
    # 後ろから順番に選ぶ
    ans += prim5 * (prim5 - 1) // 2 * (prim3 - 2)
if prim15 >= 1 and prim5 >= 1:
    ans += prim15 * (prim5 - 1)
if prim25 >= 1 and prim3 >= 1:
    ans += prim25 * (prim3 - 1)
if prim75 >= 1:
    ans += prim75
print(ans)
