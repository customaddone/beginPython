n, t = map(int, input().split())
lowest = 1001
for i in range(n):
    c1, t1 = map(int, input().split())
    if t1<=t:lowest=min(lowest,c1)
print("TLE" if lowest==1001 else lowest)
