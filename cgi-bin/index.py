#!/usr/bin/python
# coding: UTF-8
# これ使ってswitchみたいな条件分岐

n = [int(input()) for _ in range(int(input()))]
# sumで配列内の数字を全て足す
# intで整数にしよう
print(sum(n) - int(max(n)/2))
