#!/usr/bin/python
# coding: UTF-8
from functools import reduce

# https://atcoder.jp/contests/tenka1-2019-beginner/tasks/tenka1_2019_b
# 英小文字からなる長さNの文字列Sと整数Kが与えられます。
# SのK番目の文字と異なる文字全てを * で置き換えてできる文字列を出力してください。

input()
S = input()
k = int(input())
# endのおかげで横並びになる
for s in S:print(s if s == S[k - 1] else "*", end="")
