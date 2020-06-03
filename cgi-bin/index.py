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

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7


#############
# Main Code #
#############

w = getN()
n,k = getNM()
A = []
B = []
for i in range(n):
    a_,b_ = getNM()
    A.append(a_)
    B.append(b_)
# dp[n][k][w] k個足してw以内で
dp = [[[0] * (w + 1) for i in range(k + 1)] for j in range(n + 1)]

for i in range(n):
    for j in range(k + 1):
        for l in range(w + 1):
            if l >= A[i] and j >= 1:
                dp[i + 1][j][l] = max(dp[i][j][l],dp[i][j - 1][l - A[i]] + B[i])
            else:
                dp[i + 1][j][l] = dp[i][j][l]
print(dp[n][k][w])
