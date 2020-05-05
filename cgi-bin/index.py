# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A&lang=ja
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

n, m = map(int, input().split())
lista = [list(map(int, input().split())) for i in range(m)]
# UnionFind構築
U = UnionFind(n)
for query in lista:
    if query[0] == 0:
        U.union(query[1], query[2])
    else:
        print(1 if U.same(query[1], query[2]) else 0)
