# 서로소 집합

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent,a,b):
    a= find_parent(parent,a)
    b= find_parent(parent,b)
    if a<b:
        parent[b] = a
    else :
        parent[a] = b
v=6
e=4

parent = [ i for i in range(v+1) ]

for i in range(1,v+1):
    parent[i]=i


cycle = False

for i in range(e):
    a,b=map(int,input().split())
    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        break
    else:
        union_parent(parent,a,b)

print('각 원소의 부모테이블 ', end=' ')
for i in range(1,v+1):
    print(parent[i], end=' ')

print()
print('각 원소의 루트노드 ', end=' ')
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ')

print()
print('사이클 발생 여부 :', end=' ')
if cycle:
    print('사이클 발생')
else:
    print('사이클 발생 X')