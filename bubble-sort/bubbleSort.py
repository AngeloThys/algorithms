# Bubble sorting algorithm
#
# Bubble sort consists in sorting an array by comparing x and x+1 elements,
# and swapping x with x+1 if x is larger. This causes the highest numbers
# to "bubble" to the top of the array, i.e. to be sorted first.
#
# Author: Angelo Thys

# Pseudo code
#
# input: unsorted array
# output: sorted array
#
# we loop over the array len(arr) times,
# we loop over the array len(arr - i) times,
# we compare arr[i] with arr[i - 1],
# if arr[i] is larger, we swap both.

def bubbleSort(arr):
    arr_len = len(arr)

    for i in range(arr_len):
        for j in range(1, arr_len - i):
            if arr[j - 1] > arr[j]:
                [arr[j - 1], arr[j]] = [arr[j], arr[j - 1]]

    return arr
