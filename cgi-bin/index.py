from collections import Counter, deque
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**8)

N,M = map(int,input().split())
G = [dict() for i in range(N)]
RG = [dict() for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    #a -= 1; b -= 1
    G[a][b] = 1
    RG[b][a] = 1

def SCC(G, RG): # O(V+E)
    N = len(G)
    euler = []
    table = [None]*N
    visited = [False]*N
    def dfs(s): # 前処理
        visited[s] = True
        for t in G[s]:
            if not visited[t]:
                dfs(t)
        euler.append(s) # 一番奥から順番を振る

    """
    def EulerTour(G,start): # 有向グラフ上のEulerTour
        stack = [start]
        visited[start] = True
        while stack:
            u = stack.pop()
            if u >= 0:
                stack.append(~u)
                for v in G[u]:
                    if visited[v]:
                        continue
                    visited[v] = True
                    stack.append(v)
            else:
                u = ~u
                euler.append(u)
    """
    """
    def rdfs(start, label):
        stack = [start]
        visited[start] = True
        table[start] = label
        while stack:
            u = stack.pop()
            for v in RG[u]:
                if visited[v]:
                    continue
                visited[v] = True
                table[v] = label
                stack.append(v)
    """
    def rdfs(s, name): # 強連結成分を求める
        Gtable[s] = name # sのグループはname(int)
        visited[s] = 1
        for t in RG[s]: # Gの辺を全て逆転させてある
            if not visited[t]: # 逆転させてもなお到達可能なら同じグループ
                rdfs(t, name)


    for i in range(N):
        if not visited[i]:
            #EulerTour(G, i)
            dfs(i)

    visited = [False]*N
    label = 0
    for s in reversed(euler):
        if not visited[s]:
            rdfs(s, label)
            label += 1

    # 縮約後のDAGを構築
    n = label
    DAG = [dict() for i in range(n)]
    equivs = [[] for i in range(n)] # equivs[i]:DAG上のノードiに属するG上のノードたち
    for u in range(N):
        lu = table[u]
        equivs[lu].append(u)
        for v in G[u]:
            lv = table[v]
            if lu == lv:
                continue
            DAG[lu][lv] = 1
    return DAG, equivs # DAG:List[Dict[int,int]], equivs:List[List[int]]



DAG, equivs = SCC(G,RG)

n = len(DAG)
indegree = [0]*n # 各頂点の入次数
for i in range(n):
    for j in DAG[i]:
        indegree[j] += 1

# トポロジカルソート:O(V+E)
topo_sorted = []
q = deque([i for i in range(n) if indegree[i]==0]) # 入次数が0の頂点たち
while q:
    u = q.popleft()
    topo_sorted.append(u)
    for v in DAG[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)
print(n)
for i in topo_sorted:
    ans = [len(equivs[i])]+equivs[i]
    print(*ans)
