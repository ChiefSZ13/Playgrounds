import time
import random
import matplotlib.pyplot as plt

# Bubble Sort Implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Insertion Sort Implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Selection Sort Implementation
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Function to measure execution time of sorting algorithms
def measure_execution_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

# Generate arrays of different sizes and measure execution time
array_sizes = list(range(100, 1100, 100))
bubble_times = []
insertion_times = []
selection_times = []

for size in array_sizes:
    arr = [random.randint(1, 1000) for _ in range(size)]
    bubble_time = measure_execution_time(bubble_sort, arr.copy())
    insertion_time = measure_execution_time(insertion_sort, arr.copy())
    selection_time = measure_execution_time(selection_sort, arr.copy())
    bubble_times.append(bubble_time)
    insertion_times.append(insertion_time)
    selection_times.append(selection_time)

# Plotting results
plt.plot(array_sizes, bubble_times, label='Bubble Sort')
plt.plot(array_sizes, insertion_times, label='Insertion Sort')
plt.plot(array_sizes, selection_times, label='Selection Sort')
plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Sorting Algorithms Time Complexity Analysis')
plt.legend()
plt.grid(True)
plt.show()
