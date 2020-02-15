#!/usr/bin/python
# coding: UTF-8
# math関数で色々な数式を扱える

while True:
    reply = input('Enter text:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad'* 8)
    else:
        num = int(reply)
        if num < 20:
            print('row')
        else:
            print(num ** 2)
print('Bye')
