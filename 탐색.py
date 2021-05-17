# 순차탐색 메소드

 # n: array의 원소의 개수
 # target: 찾을 데이터

def sequential_search(n, target, array):
     for i in range(n) :
         if array[i]==target :
             return (i+1)







# 이진탐색 메소드

def binary_search(array,target,start,end):
    while start <= end:
        mid= (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid]> target:
            end= mid-1
        else:
            start= mid+1

    return None

