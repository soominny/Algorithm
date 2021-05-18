# 신장트리 : 모든 노드를 포함하면서 사이클을 존재하지 않는 부분 그래프
# 크루스칼 알고리즘: 최소한의 비용으로 신장 트리를 찾아야 할때 사용

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a= find_parent(parent,a)
    b= find_parent(parent,b)
    if a<b:
        parent[b]=a
    else: parent[a]=b

v=7
e=9
parent=[i for i in range(v+1)]

edge_queue=[]
tree_list=[]
tree_cost=0

for i in range(e):
    a,b,cost= map(int,input().split())
    edge_queue.append((cost,a,b))

edge_queue=sorted(edge_queue)

for edge in edge_queue:
    cost,a,b=edge
    if find_parent(parent,a) != find_parent(parent,b) :
        union_parent(parent,a,b)
        tree_list.append((a,b))

        tree_cost += cost

print(tree_list)
print(tree_cost)