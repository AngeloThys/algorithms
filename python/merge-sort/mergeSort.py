# Merge Sort Algorithm
#
# Written by Angelo Thys
#
# Created on 2024-05-10
#
# Description:
#
# A sorting algorithm that divides the array in two parts,
# up till the smallest possible part, and then sorts each part,
# recursively merging the sorted parts until the entire array is sorted.
#
# Pseudo code:
#
# 1. We need to split the array in two parts, left and right
# 2. on each part, we check if the length is 1, if so we return the array
# 3. if not, we split the array in two parts, left and right
#   comparing values of both arrays and adding the smallest value to the result

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    li = 0
    ri = 0
    result = []

    while len(left) > li and len(right) > ri:
        if left[li] < right[ri]:
            result.append(left[li])
            li += 1
        else:
            result.append(right[ri])
            ri += 1

    result += left[li:]
    result += right[ri:]

    return result
