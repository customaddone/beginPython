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


# 0でわるな
def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)

N = getN()
dot = [getList() for i in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            dis12 = distance(dot[i], dot[j])
            dis13 = distance(dot[i], dot[k])
            dis23 = distance(dot[j], dot[k])
            if (dis12 + dis13 == dis23) or (dis12 + dis23 == dis13) or (dis13 + dis23 == dis12):
                print('Yes')
                exit()

print('No')
