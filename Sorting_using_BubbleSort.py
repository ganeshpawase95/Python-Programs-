def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

array = [10, 15, 1, 80, 45, 47, 5, 99]
bubble_sort(array)
print("After sorting element:",array)