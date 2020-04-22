m = 10 ** 9 + 7
def cmb(x,y):
    r = 1
    for i in range(1, y + 1):
        r = (r * (x - i + 1) * pow(i, m-2, m)) % m
    return r

x, y = map(int, input().split())

a = (2 * x - y) / 3
b = (2 * y - x) / 3
if (x + y) % 3 == 0 and a >= 0 and b >= 0:
    print(cmb(int((x + y) / 3), int(a)))
else:
    print(0)
