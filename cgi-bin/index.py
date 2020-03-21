#!/usr/bin/python
# coding: UTF-8
# int(i)<xを満たすものの個数

n, m, x = map(int, input().split())
s = sum(int(i)<x for i in input().split())
print(s)
