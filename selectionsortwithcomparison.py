# Selection Sort with Comparison Count in Python

def selection_sort(arr):
    comparisons = 0
    n = len(arr)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr, comparisons


a = [25, 5, 10, 4, 15, 20, 18, 12, 14, 7]

sorted_array, total_comparisons = selection_sort(a)

# Output
print("Sorted array:", sorted_array)
print("Total comparisons:", total_comparisons)
