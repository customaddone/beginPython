# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_f
n, k = map(int, input().split())
edges = [[] for i in range(n)]
cus = []

def dij(edges, num_v, start):
    dist = [float('inf')] * num_v
    dist[start] = 0
    q = [i for i in range(num_v)]

    while len(q) > 0:
        r = q[0]
        for i in q:
            if dist[i] < dist[r]:
                r = i
        u = q.pop(q.index(r))
        for i in edges[u]:
            if dist[i[0]] > dist[u] + i[1]:
                dist[i[0]] = dist[u] + i[1]
    return dist

for i in range(k):
    info = list(map(int, input().split()))
    if info[0] == 0:
        cus.append(dij(edges, n, info[1] - 1)[info[2] - 1])
    elif info[0] == 1:
        # 島は島0から始まるか島1から始まるかちゃんと見る
        # 来た情報の先頭が0なら今のedgesでダイクストラ実行
        edges[info[1] - 1].append([info[2] - 1, info[3]])
        edges[info[2] - 1].append([info[1] - 1, info[3]])

for i in cus:
    if i < 1000000000:
        print(i)
    else:
        print(-1)
