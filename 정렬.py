
# 선택정렬
# : 가장 작은 데이터를 선택해 가장 앞에 있는 데이터와 바꿈
def selection_sort(array):

    for i in range(len(array)) :
        min_index= i
        for j in range(i+1,len(array)):
            if array[min_index] > array[j]:
                min_index=j

        array[i], array[min_index] = array[min_index],array[i]
    return array

A= [7,5,9,0,3,1,6,2,4,8]
print(selection_sort(A))



# 삽입정렬
def insertion_sort(array):
    for i in range(1,len(array)):
        for j in range(i,0,-1):
            if array[j]<array[j-1]:
                array[j],array[j-1]=array[j-1],array[j]
            else:
                break
    return array

B= [7,5,9,0,3,1,6,2,4,8]
print(insertion_sort(B))




# 퀵정렬
def quick_sort(array):
    if len(array) < 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x<= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side)+[pivot]+quick_sort(right_side)


C = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(quick_sort(C))



# 계수정렬

array=[7,5,9,0,3,1,6,2,9,1,4,0,5,2]
count=[0]*(max(array)-min(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')