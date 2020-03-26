a = int(input())
b = int(input())
c = int(input())
x = int(input())
counter = 0
for l in range(a + 1):
    for m in range(b + 1):
        if 500 * l + 100 * m > x:
            break
        if 500 * l + 100 * m + 50 * c >= x:
            counter += 1
print(counter)
