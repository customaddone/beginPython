#!/usr/bin/python
# coding: UTF-8
# これ使ってswitchみたいな条件分岐
import math

x = int(input())
def prime(num):
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

print(prime(x))
