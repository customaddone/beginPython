#!/usr/bin/python
# coding: UTF-8

# すぬけ君は、AtCoder s Contestという名前のコンテストを開こうとしています。ここで、sは長さ
# １以上の文字列であり、１文字目は英大文字、２文字目以降は英語小文字です
# すぬけ君は、このコンテストの略称を A x C に決めました。 ここで、x  は s  の先頭の英大文字です。
# コンテストの名前が与えられるので、コンテストの略称を出力してください。

list = input().split()
abbr = ""
for str in list:
    abbr += str[0].upper()
print(abbr)
