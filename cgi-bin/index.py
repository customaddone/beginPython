#!/usr/bin/python
# coding: UTF-8
# これ使ってswitchみたいな条件分岐

# 「以上」の書き方を覚えよう
a, b = map(int, input().split())
n = [int(input()) for i in range(int(input()))]
for i in n:
    print(a - i if i < a else 0 if a <= i <= b else -1)
