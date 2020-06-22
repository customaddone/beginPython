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
import heapq
import math
from fractions import gcd
import random
import string
import copy
from itertools import combinations, permutations, product
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7


#############
# Main Code #
#############

N = 26

def num2alpha(num):
    if num <= 26:
        return chr(96 + num)
    elif num % 26 == 0:
        return num2alpha(num // 26 - 1) + chr(122)
    else:
        return num2alpha(num // 26) + chr(96 + num % 26)

# z
print(num2alpha(N))

n = N
lista = []
digit = 26
i = 0

while n != 0:
    opt = n % digit
    lista.insert(0, opt)
    if n % digit == 0:
        n = n // digit - 1
    else:
        n = n // digit
    i += 1

str_list = 'abcdefghijklmnopqrstuvwxyz'
ans = ''
for i in range(len(lista)):
    ans += str_list[lista[i] - 1]

# z
print(ans)
