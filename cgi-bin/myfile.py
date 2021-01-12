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

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

# 単純にswapできるか
come, w2 = carry[go]
if come == i and A[i] > w2 and A[go] > w1:
    ans += 1
    move.append([i + 1, go + 1])
    carry[i], carry[go] = carry[go], carry[i]
