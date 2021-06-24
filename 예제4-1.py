# 책버전
n=int(input())
plans=input().split()
x=y=1

for plan in plans:
    if plan == 'L':
        if x-1 >= 1:
            x-=1
    elif plan =='R':
        if x+1 <= n:
            x+=1

    elif plan =='U':
        if y-1 >= 1:
            y-=1

    elif plan =='D':
        if y+1<=n:
            y+=1
print(y,x)

# 프로그래머스 버전
n=5
plans=['R','R','R','U','D','D']

def solution(n,plans):
    x=1
    y=1
    for plan in plans :
        if plan == 'L':
            y=left(y)
        elif plan =='R':
            y=right(y)
        elif plan=='U':
            x=up(x)
        elif plan=='D':
            x=down(x)


    print(x,y)
    return 0

def left(y):
    if y-1 >= 1:
        y=y-1
    return y

def right(y):
    if y+1 <= n:
        y+=1
    return y

def up(x):
    if x-1 >=1:
        x-=1
    return x

def down(x):
    if x+1 <=n :
        x+=1
    return x

solution(n,plans)