#1
A = "a:b:c:d".split(":")
print("#".join(A))

#4
A = [20,55,67,82,45,33,90,87,100,25]
result=[a for a in A if a >= 50]
print(sum(result))

result=list(filter(lambda a: a >= 50,A))
print(sum(result))

#5
def fi_bo(n):
    a=0
    b=1
    new = a + b
    print(a,",",b,",",new,end='')
    for _ in range(n):
        a=b
        b=new
        new = a + b
        if new >= n:
            break
        else:
            print(",",new,end='')



n=int(input())
fi_bo(n)