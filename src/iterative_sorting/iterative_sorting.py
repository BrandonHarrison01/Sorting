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
        print('==========')
        print('for loop', j)
        print('==========')
        while arr[j] > arr[j + 1]:
            print('==========')
            print('while loop')
            print(arr)
            print('==========')

            for i in range(1, len(arr)):
                current = arr[i - 1]
                compare = arr[i]

                print(current, 'current')
                print(compare, 'compare')
                print('----------')

                if current > compare:
                    arr[i] = current
                    arr[i - 1] = compare

    return arr

# print(bubble_sort([1, 2, 9, 8, 0, 4, 10, 3, 7, 18, 5, 15]))
print(bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr