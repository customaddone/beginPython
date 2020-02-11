#!/usr/bin/python
# coding: UTF-8
# math関数で色々な数式を扱える

D = { 'a': 1, 'b': 2, 'c': 3}

# さっきのがこれで一発でできる
for key in sorted(D): print key, '=>', D[key]

# 文字列もソートできる
string = 'spam'
for case in sorted(string): print case.upper()
