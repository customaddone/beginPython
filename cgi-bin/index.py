V, E = map(int, input().split())
edges = []
for i in range(E):
    # sからtまでコストwで
    s, t, w = map(int, input().split())
    edges.append((w, s - 1, t - 1))
# コスト順に並べる
edges.sort()

def kruskal(n, edges):
    U = UnionFind(n)
    res = 0
    for e in edges:
        w, s, t = e
        if not U.same(s, t):
            res += w
            U.unite(s, t)
    return res
print(kruskal(V, edges))
