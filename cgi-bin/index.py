# count
import math
n = int(input())
bug = list(map(int, input().split()))
print(math.ceil(sum(bug)/(n - bug.count(0))))
