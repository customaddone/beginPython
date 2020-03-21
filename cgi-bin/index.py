#nが人数、mが商品の種類
n, m = map(int, input().split())
counter = [0] * m
for i in range(n):
    a, *b, = map(int, input().split())
    for i in b:
        counter[i - 1] += 1
print(sum([i == n for i in counter]))

#模範解答
n,m=map(int,input().split())
S=set(range(1,m+1))
for i in range(n):
    K,*A=map(int,input().split())
    S&=set(A)
print(len(S))
