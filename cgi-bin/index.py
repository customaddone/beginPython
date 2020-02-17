#!/usr/bin/python
# coding: UTF-8
# これ使ってswitchみたいな条件分岐
x = 10
while x:
    # continueの前にxの増減を書かないと無限ループ
    x -= 1
    if x % 2 == 0:
        continue
    print(x)
