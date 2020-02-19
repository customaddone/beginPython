#!/usr/bin/python
# coding: UTF-8
# これ使ってswitchみたいな条件分岐

n = int(input())
#パターン１
#list = [[list(map(int, input().split()))] for i in range(n)]


#パターン２
list = [[int(j) for j in input().split()] for i in range(n)]

#パターン３
#list = []
#for i in range(n):
#    list.append([int(i) for i in input().split()])

print(list)
