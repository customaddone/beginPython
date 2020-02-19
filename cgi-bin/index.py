#!/usr/bin/python
# coding: UTF-8
# これ使ってswitchみたいな条件分岐

N, T = map(int, input().split())
m = 1001
for i in range(n):
    c, t = map(int, input().split())
    # 順繰りにこれまでで一番小さかったmと比べる
    if t <= T:m=min(m, c)
print("TLE" if m==1001 else m)
