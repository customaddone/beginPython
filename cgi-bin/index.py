# 3進数に変換
n = int(input())
result = ''

def tenary(n):
    if n == 0:
        return '3'
    elif n == 1:
        return '5'
    else:
        return '7'
while n >= 3:
    # １桁目、２桁目...
    result = str(n % 3) + result
    n = n // 3
result = str(n) +result
