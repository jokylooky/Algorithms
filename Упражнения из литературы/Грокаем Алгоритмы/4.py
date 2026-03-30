import random


# 4.1
def summ(arr):
    summa = 0
    for i in arr:
        summa += i

    return summa

# 4.2
def elemNums(arr):
    if arr == []:
        return 0

    return 1 + elemNums(arr[1:])

# 4.3
def recMax(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]

    if arr[0] > recMax(arr[1:]):
        return arr[0]
    else:
        return recMax(arr[1:])

# 4.4
def binarySearchRec(arr, num):
    mid = len(arr) // 2

    if arr[mid] == num:
        return arr[mid]
    elif arr[mid] < num:
        return binarySearchRec(arr[mid:], num)
    elif arr[mid] > num:
        return binarySearchRec(arr[:mid], num)
    
# quickSort - O(log n)
def quickSort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]

    left = [i for i in arr[1:] if i <= pivot]
    right = [i for i in arr[1:] if i > pivot]

    return quickSort(left) + [pivot] + quickSort(right)


a = [2,4,3,2,14,25,5]

print('quickSort: ', quickSort(a))

print(summ(a)) # 4.1
print(elemNums(a)) # 4.2
print(recMax(a)) # 4.3

sorted(a) # 4.4
print(binarySearchRec(a, 14))
