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

"""
Nちいさ　半分全列挙すらできる
ナップサックでいいじゃ
枝借りする
relistの部分

ソートがなければ
"""

N, T = getNM()
A = getList()

# ソートでNlogN
def relist(array):
    fore_list = []
    for bit in range(1 << len(array)):
        time = 0
        for i in range(1 << len(array)):
            if bit & (1 << i):
                time += array[i]
        if time <= T:
            fore_list.append(time)
    fore_list.sort()

    return fore_list

F = relist(A[:N // 2])
B = relist(A[N // 2:])

ans = 0
# NlogN
r = 0
for f in F:
    if f > T:
        break
    index = bisect_right(B, T - f)
    if index > 0:
        opt = f + B[index - 1]
        ans = max(ans, opt)

print(ans)
