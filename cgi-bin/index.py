#!/usr/bin/python
# coding: UTF-8
# これ使ってswitchみたいな条件分岐
import math

x = int(input())
for i in range(2, math.floor(math.sqrt(x)) + 1):
    if x % i == 0:
        print(x, 'has factor', i)
        break
    print(x, 'is prime')
