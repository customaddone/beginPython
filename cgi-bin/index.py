# https://atcoder.jp/contests/abc145/tasks/abc145_d
m = 10 ** 9 + 7
def cmb(x,y):
    r = 1
    for i in range(1, y + 1):
        r = (r * (x - i + 1) * pow(i, m-2, m)) % m
    return r

x, y = map(int, input().split())

# a:(i + 1, j + 2), a:(i + 1, j + 2)してx, yに辿り着きたい
# a, bのそれぞれの回数は
# a + 2b = x 2a + b = yを因数分岐して求める
a = (2 * x - y) / 3
b = (2 * y - x) / 3
# あとはa, bをどの順番で配置するか → a + b C a
# aもbもマイナスになるパターンがある
if (x + y) % 3 == 0 and a >= 0 and b >= 0:
    print(cmb(int((x + y) / 3), int(a)))
else:
    print(0)
