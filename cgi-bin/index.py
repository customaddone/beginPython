#!/usr/bin/python
# coding: UTF-8
# math関数で色々な数式を扱える

# 0はfalseになる

def intersect(sec1, sec2):
    res = []
    for x in sec1:
        if x in sec2:
            res.append(x)
    return res

sec1 = 'apple'
sec2 = 'melon'
print(intersect(sec1, sec2))
