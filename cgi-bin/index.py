# if文の条件ををwhileの後ろにつける
input()
a = list(map(int, input().split()))
counter = 0
while all([(i % 2 == 0) for i in a]):
    a = [int(i / 2) for i in a]
    counter += 1
print(counter)
