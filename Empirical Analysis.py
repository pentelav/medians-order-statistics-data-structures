# Comparisons of deterministic versus randomized (Quickselect) selection algorithms, based on the time required to locate the median in different-size arrays.
# They are randomly generated arrays, and the time taken by each algorithm is documented to give empirical analysis on the performance of the algorithm.

import time
import random
import numpy as np

# Deterministic Selection (Median of Medians)
def deterministic_select(arr, k):
    # Base case: array small enough to sort directly
    if len(arr) <= 5:
        return sorted(arr)[k-1]

    # Divide array into groups of 5
    groups = [arr[i:i+5] for i in range(0, len(arr), 5)]
    # Find median of each group
    medians = [sorted(group)[len(group)//2] for group in groups]

    # Recursively find pivot as median of medians
    pivot = deterministic_select(medians, (len(medians)+1)//2)

    # Partition array around pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    count = arr.count(pivot)

    # Determine k-th smallest element position
    if k <= len(low):
        return deterministic_select(low, k)
    elif k <= len(low) + count:
        return pivot
    else:
        return deterministic_select(high, k - len(low) - count)

# 🔹 Randomized Selection (Quickselect)
def randomized_select(arr, k):
    # ⚡ Base case: only one element
    if len(arr) == 1:
        return arr[0]

    # Pick a random pivot
    pivot = random.choice(arr)
    # 🔹 Partition array around pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    count = arr.count(pivot)

    # Determine k-th smallest element position
    if k <= len(low):
        return randomized_select(low, k)
    elif k <= len(low) + count:
        return pivot
    else:
        return randomized_select(high, k - len(low) - count)

# Empirical Analysis
array_sizes = [1000, 5000, 10000, 20000]  # Array sizes to test
det_times = []  # Store deterministic times
rand_times = []  # Store randomized times

for n in array_sizes:
    # Generate random array
    arr = np.random.randint(0, 1000000, size=n).tolist()
    k = n // 2  # Median position

    # Measure deterministic selection time
    start_time = time.time()
    det_median = deterministic_select(arr, k)
    dt_time = time.time() - start_time
    det_times.append(dt_time)

    # Measure randomized selection time
    start_time = time.time()
    rand_median = randomized_select(arr, k)
    rt_time = time.time() - start_time
    rand_times.append(rt_time)

    # Print results
    print(f"Array size: {n}")
    print(f"Deterministic median: {det_median}, Time: {dt_time:.6f}s")
    print(f"Randomized median: {rand_median}, Time: {rt_time:.6f}s\n")
