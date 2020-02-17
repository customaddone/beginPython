#!/usr/bin/python
# coding: UTF-8
# これ使ってswitchみたいな条件分岐
# https://atcoder.jp/contests/abc085/tasks/abc085_b

n = int(input())
list = [int(input()) for i in range(n)]
# setで重複したものを消す
print(len(set(list)))
