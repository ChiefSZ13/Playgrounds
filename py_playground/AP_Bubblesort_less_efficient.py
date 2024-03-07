def bubble_sort_basic(arr):
    n = len(arr)
    for i in range(n):
        for j in range (0, n-i-1):
            print(j)
            if arr[j] > arr[i]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

array = [9, 2, 4, 5, 6]
print(bubble_sort_basic(array))