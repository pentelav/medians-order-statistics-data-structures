# Locates the k th smallest element in an array, based on the randomized Quickselect algorithm.
# An element is selected at random and the array is divided into parts that are less than the pivot, those that are greater than the pivot and those that are equal to the pivot.
# Recursion is applied to the relevant partition until the wished order statistic is discovered.

import random

def randomized_select(arr, k):
    # Base case: only one element in array
    if len(arr) == 1:
        return arr[0]

    # Randomly select pivot
    pivot = random.choice(arr)

    # Partition array into elements less than, greater than, and equal to pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    count = arr.count(pivot)

    # Determine which partition contains the k-th smallest element
    if k <= len(low):
        return randomized_select(low, k)
    elif k <= len(low) + count:
        return pivot
    else:
        return randomized_select(high, k - len(low) - count)

# Example usage
arr_example = [12, 3, 5, 7, 4, 19, 26, 1, 10]
k_example = 4
result = randomized_select(arr_example, k_example)
print(f"{k_example}-th smallest element (randomized): {result}")
