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


T = getN()
"""
通りの数を求める問題 dp?数え上げcombo?
白い正方形の中に赤い正方形と青い正方形を置く通りが何通りあるか答える
T個 <= 10 ** 5のqueryに答える
各queryにO(1)で

赤い正方形の左上の座標を全部探索
重ならないようにとは?
comboっぽい
重なる通りを控除する？
赤を置く通りは(N - A + 1) ** 2通り
青を置く通りは(N - B + 1) ** 2通り
赤が端っこにある時、真ん中にある時、重なるパターンは？
青の左端 < 赤の右端かつ青の上側 < 赤の下側 または
赤の左端 < 青の右端かつ赤の上側 < 青の下側 または
赤の右端はA,A + 1...N
赤の下側はA,A + 1...N
そのそれぞれについて

対照性があるからO(1)でいけるはず
部分的に入っている,　完全に入っている
"""


for i in range(T):
    n, a, b = getNM()
    opt = abs(n - a - b + 1)
    print(((4 * (n - a + 1) * (n - b + 1)) - ((opt ** 2) * 4)) % mod)
