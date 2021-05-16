""" BFS: 큐 자료구조 이용
1. 탐색 시작 노드를 에 삽입하고 방문처리큐
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중 방문하지 않은 노드 모!두!를 큐에 삽입하고 방문처리
3. 큐가 빌때까지 반복
"""

# >>> deque 라이브러리 이용

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start]=True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i]=True


# 사용예시
# 1) 인접리스트 (인덱스 0번은 비워두고 )
graph= [ [],
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]]

# 2) 방문 리스트 초기화
visited = [False] * 9

bfs(graph, 1, visited)
