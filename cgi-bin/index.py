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
sys.setrecursionlimit(10000000)
inf = float('inf')
eps = 10 ** (-15)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

class Rational():
    def __init__(self, nume, deno):
        # 約分して格納
        self.n = self.reduction(nume, deno)

    # 約分
    def reduction(self, nume, deno):
        g = math.gcd(nume, deno)
        if deno < 0:
            return (-(nume // g), -(deno // g))
        else:
            return (nume // g, deno // g)

    # たす
    def __add__(self, other):
        nume = self.n[0] * other.n[1] + self.n[1] * other.n[0]
        deno = self.n[1] * other.n[1]
        return Rational(nume, deno)

    # ひく
    def __sub__(self, other):
        nume = self.n[0] * other.n[1] - self.n[1] * other.n[0]
        deno = self.n[1] * other.n[1]
        return Rational(nume, deno)

    # かける
    def __mul__(self, other):
        return Rational(self.n[0] * other.n[0], self.n[1] * other.n[1])

    # わる 「/」の方
    def __truediv__(self, other):
        return Rational(self.n[0] * other.n[1], self.n[1] * other.n[0])
