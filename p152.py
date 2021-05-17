# 미로탈출

# 1. 탐색 시작 노드를 큐에 삽입하고 방문처리
# 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중 방문하지 않은 노드 모!두!를 큐에 삽입하고 방문처리
# 3. 큐가 빌때까지 반복


from collections import deque
n=5
m=6
graph=[[1,0,1,0,1,0],
       [1,1,1,1,1,1],
       [0,0,0,0,0,1],
       [1,1,1,1,1,1],
       [1,1,1,1,1,1]]

dx= [-1,1,0,0]
dy= [0,0,-1,1]

def bfs(x,y):
    result = 0
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()
        for i in range (4):
            nx= x + dx[i]
            ny= y + dy[i]

            if nx<0 or nx >=n or ny<0 or ny>=m :
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1

                queue.append((nx,ny))


    return graph[n-1][m-1]

print(bfs(0,0))

