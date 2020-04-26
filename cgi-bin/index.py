# https://atcoder.jp/contests/abc077/tasks/arc084_a
from bisect import bisect_left
n = int(input())
listtop = sorted(list(map(int, input().split())))
listmiddle = sorted(list(map(int, input().split())))
listbottom = sorted(list(map(int, input().split())))
sum = 0

# 最初0があるので注意
# 0~N個目に乗せられるパーツの合計（累積和）
listmiddlesum = [0]
for i in range(n):
    # ride:n個目に乗せられるlisttopのパーツの数
    ride = bisect_left(listtop, listmiddle[i])
    listmiddlesum.append(listmiddlesum[i] + ride)
for i in range(n):
    ridesum = bisect_left(listmiddle, listbottom[i])
    sum += listmiddlesum[ridesum]
print(sum)

"""
# 別解
# まずbを決める
# bより小さいaのパーツは全て置け、bより大きいcのパーツは下に敷くことができるので
# 任意のbについて（bより小さいaのパーツの数）*（bより大きいcのパーツ）
n = int(input())
Alist = list(map(int,input().split()))
Blist = list(map(int,input().split()))
Clist = list(map(int,input().split()))
Alist.sort()
Clist.sort()
retnum = 0
for i in Blist:
    Anum = bisect_left(Alist,i)
    # rightにする
    Cnum =  N - bisect_right(Clist,i)
    retnum +=(Anum * Cnum)
print(retnum)
"""
