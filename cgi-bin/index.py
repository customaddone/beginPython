#!/usr/bin/python
# coding: UTF-8
# これ使ってswitchみたいな条件分岐
# https://atcoder.jp/contests/abc103/tasks/abc103_a
*a, = map(int, input().split())
print(a)
# max()で配列の中の最大の要素を、minで最小の要素をとる
print(max(a) - min(a))
