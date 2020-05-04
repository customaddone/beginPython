# https://www.ioi-jp.org/camp/2010/2010-sp-tasks/2010-sp-day3_22.pdf
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

n,m,k = map(int,input().split())
lines = [tuple(map(int,input().split())) for _ in range(m)]
lines = sorted(lines, key = lambda x: x[2])

uf = UnionFind(n)

ans = 0
tree_num = n
for line in lines:
    if(tree_num == k):
        break

    a,b,c = line
    a,b = a - 1,b - 1
    if(uf.same(a, b)):
        continue
    uf.union(a, b)
    ans += c
    tree_num -= 1

print(ans)

'''
方針
N個の都市を、木がK個の森にする。
最小全域木と同じようなアルゴリズムで、木がK個になったタイミングで打ち切ればOK。
その時に採用された通路のコスト合計が答え。
'''
