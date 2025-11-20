# The deterministic Median of Medians algorithm is a method of finding the kth smallest element in an array.
# The array is partitioned into five groups, medians in each of them are calculated, and median of medians is utilized as a pivot.
# Recursion will keep on until the required order statistic is located.

def deterministic_select(arr, k):
    # Base case: small array, sort directly
    if len(arr) <= 5:
        return sorted(arr)[k-1]

    # Divide array into groups of 5 elements
    groups = [arr[i:i+5] for i in range(0, len(arr), 5)]
    # Find median of each group
    medians = [sorted(group)[len(group)//2] for group in groups]

    # Recursively find pivot as median of medians
    pivot = deterministic_select(medians, (len(medians)+1)//2)

    # Partition array around pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    count = arr.count(pivot)

    # Determine position of k-th smallest element
    if k <= len(low):
        return deterministic_select(low, k)
    elif k <= len(low) + count:
        return pivot
    else:
        return deterministic_select(high, k - len(low) - count)

# Example usage
arr_example = [12, 3, 5, 7, 4, 19, 26, 1, 10]
k_example = 4
result = deterministic_select(arr_example, k_example)
print(f"{k_example}-th smallest element (deterministic): {result}")
