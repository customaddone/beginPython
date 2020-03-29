#import fractionsしてgcd関数を呼び出す
#python3.4.3ではmathではなくfractionsに関数がある
import fractions
a, b = map(int, input().split())
print(int(a * b / fractions.gcd(a, b)))

#fractions使わない場合
#ユーグリッド互除法
def gcd(m, n):
    x = max(m, n)
    y = min(m, n)
    if x % y == 0:
        return y
    else:
        while x % y != 0:
            z = x % y
            x = y
            y = z
        else:
            return z
print(int(a * b) / gcd(a, b))
