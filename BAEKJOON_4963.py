import sys
sys.setrecursionlimit(9999999)
while True:
    w,h=map(int,input().split())

    if w==h==0:
        break

    graph=[]
    for _ in range(h):
        graph.append(list(map(int, input().split())))


    def DFS(x,y):
        if x<=-1 or x>=h or y<=-1 or y>=w :
            return False
        if graph[x][y]==1:
            graph[x][y]=0
            DFS(x-1,y)
            DFS(x+1,y)
            DFS(x,y-1)
            DFS(x,y+1)
            DFS(x-1,y-1)
            DFS(x-1,y+1)
            DFS(x+1,y-1)
            DFS(x+1,y+1)
            return True
        return False

    result=0
    for i in range(h):
        for j in range(w):
            if DFS(i,j)==True:
                result+=1

    print(result)