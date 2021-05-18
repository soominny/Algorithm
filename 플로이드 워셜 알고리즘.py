# 플로이드 워셜 알고리즘

# n: 노드개수 m: 간선개수
n=4
m=7
INF = int(1e9)
graph= [[INF] * (n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    a,b,cost = map(int,input().split())
    graph[a][b]=cost

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

for a in range(1,n+1):
    for b in range(1, n+1):
        if graph[a][b]== INF:
            print("-",end=' ')
        else:
            print(graph[a][b],end=' ')
    print()