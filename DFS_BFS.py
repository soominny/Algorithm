""" < DFS와 BFS 유형 비교 >

- 그래프의 모든 정점을 방문 : DFS, BFS 둘중 아무거나 ok
- 경로의 특징을 저장해둬야 하는 문제 : DFS
  ( = 이동할때 마다 가중치가 붙어서 이동한다거나 이동과정에서 여러제약이 있는 경우)
- 가중치가 1인 최단거리 구해야하는 문제 : BFS

"""






# DFS : 스택 자료구조 이용
# 1. 탐색 시작 노드를 스택에 삽입하고 방문처리
# 2. 스택 최상단 노드에 방문하지 않은 인접노드가 있으면 스택에 넣고 방문처리
#    방문하지 않은 인접노드가 없으면 스택에서 최상단 노드 꺼내 pop()
# 3. 스택이 빌때까지 반복

def dfs(graph, v, visited) :
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
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

dfs(graph, 1, visited)



#  BFS: 큐 자료구조 이용
# 1. 탐색 시작 노드를 에 삽입하고 방문처리큐
# 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중 방문하지 않은 노드 모!두!를 큐에 삽입하고 방문처리
# 3. 큐가 빌때까지 반복
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


