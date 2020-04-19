n = int(input())
a = list(map(int, input().split()))

b = [0]*n

# リスト作成するとO(n)で解ける
for i in a:
    b[i-1] += 1

for i in b:
    print(i)
