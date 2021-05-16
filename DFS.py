""" DFS : 스택 자료구조 이용
1. 탐색 시작 노드를 스택에 삽입하고 방문처리
2. 스택 최상단 노드에 방문하지 않은 인접노드가 있으면 스택에 넣고 방문처리
   방문하지 않은 인접노드가 없으면 스택에서 최상단 노드 꺼내 pop()
3. 스택이 빌때까지 반복
"""

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


