# Selection Sort Algorithm

# Search through an array and keep track of minimum value during each iteration
# At the end of each iteration, do the swap
# Quadratic time complexity: O(n^2)
# O(1) space complexity
# Only good for small data set

def selectionSort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i + 1, len(arr)):
            if(arr[min] > arr[j]):
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return arr


arr = [6, 7, 8, 10, 125, 2, 3, 1]
print(selectionSort(arr))
