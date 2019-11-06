# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    merged_arr = []
    # TO-DO

    i = 0
    j = 0
    k = 0

    if arrA[i] < arrB[j]:
       merged_arr[k] = arrA[i]
       i = i + 1
    else:
       merged_arr[k] = arrB[j]
       j = j + 1
    k = k + 1

    return merged_arr

# print(merge([1,3,5,7], [2,4,6,8]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # print("Splitting ",arr)

    if len(arr)>1:
       mid = len(arr)//2
       left = arr[:mid]
       right = arr[mid:]

       #recursion
       merge_sort(left)
       merge_sort(right)

       i = 0
       j = 0
       k = 0

       while i < len(left) and j < len(right):
           if left[i] < right[j]:
               arr[k] = left[i]
               i = i + 1
           else:
               arr[k] = right[j]
               j = j + 1
           k = k + 1

       while i < len(left):
           arr[k] = left[i]
           i = i + 1
           k = k + 1

       while j < len(right):
           arr[k] = right[j]
           j = j + 1
           k = k + 1

    return arr

arr = [54,26,93,17,77,31,44,55,20]

print(merge_sort(arr))



# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
