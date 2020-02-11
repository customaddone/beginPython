#!/usr/bin/python
# coding: UTF-8
# math関数で色々な数式を扱える
import re
match = re.match('Hello[ ]*(.*)world', 'Hello python world')
print match.group(1)
