def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
    
array = [10, 15, 1, 80, 45, 47, 5, 99]
target = 80
result = linear_search(array, target)
print("The element found at index:", result)