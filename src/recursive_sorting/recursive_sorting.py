# TO-DO: complete the helper function below to merge 2 sorted arrays
arrC = [1, 23, 85, 87]
arrD = [3, 4, 7, 9]
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0
    m = 0
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr[m] = arrA[a]
            a += 1
        else:
            merged_arr[m] = arrB[b]
            b +=1
        m += 1
    while a < len(arrA):
        merged_arr[m] = arrA[a]
        a += 1
        m += 1
    while b < len(arrB):
        merged_arr[m] = arrB[b]
        b += 1
        m += 1    
    return merged_arr
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[mid:] 
        left = merge_sort(left)
        right = arr[:mid]
        right = merge_sort(right)
        arr = merge(left,right)
    return arr
# print(merge(arrC,arrD))
tester = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    right_start = mid
    while start <= mid and right_start <= end:
        if arr[start] < arr[right_start]:
            start += 1
        else:
            value = arr[right_start]
            index = right_start
            while index != start:
                print('running with', value)
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value
            start += 1
            mid += 1
            right_start += 1
    return arr

def merge_sort_in_place(arr, l, r):
    if l < r:
        mid = (l + r)// 2
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid+1, r)
        merge_in_place(arr,l,mid+1,r)
    return arr

print(merge_sort_in_place(tester, 0, len(tester)-1))
# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
