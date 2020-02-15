#!/usr/bin/python
# coding: UTF-8
# math関数で色々な数式を扱える

S = "xxxxSPAMxxxxSPAMxxx"
where = S.find('SPAM')

S = S[:where] + 'EGGS' + S[where + 4:]
print(S)
