""" 2가지 방식으로 구현한 팩토리얼 """

# 1 반복
def factorial_iter(n):
    result=1
    for i in range(1, n+1):
        result *= i
    return result

# 사용예시
fact=factorial_iter(5)
print(fact)


# 2 재귀
def factorial_recursive(n):
    if n<=1:
        return 1
    return n * factorial_recursive(n-1)

# 사용예시
fact2 = factorial_recursive(5)
print(fact2)