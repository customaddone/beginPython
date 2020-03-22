n = int(input())
an = 0
a3, a2, a1 = 0, 0, 1

for _ in range(n - 3):
    an = a3 + a2 + a1
    a3, a2, a1 = a2, a1, an
print(an % 10007)

# 模範解答 for文の中で10007の余りを求めとく
n=int(input())
a,b,c=0,0,1
for i in range(n-1):
    a,b,c=b,c,(a+b+c)%10007
print(a)
