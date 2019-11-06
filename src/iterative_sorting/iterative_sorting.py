# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(1, len(arr)):
        cur_index = arr[i]
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        while smallest_index > 0 and cur_index < arr[smallest_index - 1]:
            arr[smallest_index] = arr[smallest_index - 1]
            smallest_index -= 1

        # TO-DO: swap

        arr[smallest_index] = cur_index


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    for j in range(0, len(arr) - 1):
        print(j)

        for i in range(1, len(arr)):
            current = arr[i - 1]
            compare = arr[i]

            if current > compare:
                arr[i] = current
                arr[i - 1] = compare

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr