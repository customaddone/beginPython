#!/usr/bin/python
# coding: UTF-8
# これ使ってswitchみたいな条件分岐

n = int(input())
town = []
people = []
for i in range(n):
    t, p = input().split()
    town.append(t)
    people.append(int(p))
# indexでpeopleの中での最大の数値のインデックスが取れる
if max(people)>sum(people)/2:print(town[people.index(max(people))])
else: print("atcoder")
