from itertools import permutations
N=int(input())

n=[1,2,3,4,5,6,7,8,9]
List=list(permutations(n,3))
for _ in range(N):
    answer, s, b = map(int,input().split())
    answer = list(str(answer))

    removed_count=0
    A = len(List)
    for i in range(A):
        strike = 0
        ball = 0
        i -= removed_count

        for j in range(3):
            answer[j] = int(answer[j])
            if answer[j] in List[i]:
                if j==List[i].index(answer[j]):
                    strike+=1
                else:
                    ball+=1

        if strike != s or ball != b:
            List.remove(List[i])
            removed_count+=1

print(len(List))

print(List)