#!/usr/bin/python
# coding: UTF-8

# https://atcoder.jp/contests/abc042/tasks/abc042_b
# いろはちゃんは 長さLの文字列を個持っており、それぞれS1,S2,Nです。
# それらの文字列を好きな順番で全て結合してできる文字列のうち、もっとも辞書順で小さいものを求めてください。
a, b = map(int,input().split())
s = sorted([input() for i in range(b)])
# joinで配列の中に入っている文字列を全て結合
print("".join(s))
