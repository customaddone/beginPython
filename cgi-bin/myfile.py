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
任意の順番で　効率のいい方法
隣同士を入れ替える　全探索無理
1, 2, 3...Nの順番にする ヒストグラムか
"""

N = getN()
T = input()

if N == 1:
    if T == '1':
        print(20000000000)
        exit()
    elif T == '0':
        print(10000000000)
        exit()
    else:
        print(0)

if T[0] == '1' and T[1] == '1':
    c =

c = (N // 3) + 1
ene = '110' * c
cnt = 0
for i in range(3):
    if ene[i:i+N] == T:
        cnt += 1
if cnt >= 1:
    cnt = cnt * 10 ** 10 - c + 1
if N % 3 == 0:
    if '110' * (N // 3) == T:
        cnt += 1
print(cnt)
