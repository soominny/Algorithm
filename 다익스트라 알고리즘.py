# 다익스트라 알고리즘 소스코드

import heapq
import sys

def dijkstra(start,graph):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist :
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost< distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))



INF= int(1e9)

# n:노드의 개수, m:간선의 개수
n=6
m=11

G=[[] for _ in range(n+1)]
distance= [INF] * (n+1)

for i in range(m):
    a,b,c = map(int,input().split())
    G[a].append((b,c))

dijkstra(1,G)

for i in range(1,n+1):
    if distance[i] == INF:
        print("-")
    else:
        print(distance[i])

