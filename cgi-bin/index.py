# https://atcoder.jp/contests/abc008/tasks/abc008_3
import math
n = int(input())
c = [int(input()) for i in range(n)]
sumans = 0

for i in c:
    lista = [j for j in c if i % j == 0]
    count = len(lista)
    # iが面になる通り
    # math.factorial（全通り） * iの約数を一列に並べた中でiが奇数個目にある確率
    sumans += math.ceil(count / 2) / count
print(sumans)
