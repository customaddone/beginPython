#!/usr/bin/python
# coding: UTF-8
# これ使ってswitchみたいな条件分岐
# https://atcoder.jp/contests/abc069/tasks/abc069_b
s = input()
print(s[0] + str(len(s[1:-1])) + s[-1])

a, *b, c = input()
print(a + str(len(b)) + c)
