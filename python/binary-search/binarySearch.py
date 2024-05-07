# Binary search algorithm
#
# Written by: Angelo Thys
#
# Binary search is a divide and conquer algorithm that returns the position
# of a target by dividing the array into two parts, recursively,
# until the target is found.
#
# Pseudo code:
#
# input: array, target
# output: position of target (index) or -1 if not found
#
# Obtain median of the array
# check if array length is more than 0
# if yes:
#     check if median is higher, lower or target
#         if lower, slice lower half,
#         if higher slice higher half,
#         if target, return index
# if no:
#    return -1

def binarySearch(list, target):
    lower = 0
    higher = len(list) - 1

    while lower <= higher:
        mid = (lower + higher) // 2
        if list[mid] < target:
            lower = mid + 1
        elif list[mid] > target:
            higher = mid - 1
        else:
            return mid

    return -1
