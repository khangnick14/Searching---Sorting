# Quick Sort Algorithm
# move smaller elements to left of a pivot. Recursively divide array in 2 partitions
# 1. Select the Pivot Element: the value of end index is pivot
# 2. Declare two pointer: first one at the start index, the second one at start - 1
# 3. Loop the first pointer to the end - 1
#       if element is less than pivot: move second pointer to that place: swap the value
# 4. Swap pivot with the value of the second pointer + 1
# 5. Now we have a pivot at the middle of array, divide array into 2 subarrays then recursive apply the quicksort again
# Time complexity: O(n*logn)
# Space complexity: O(logn)
# Link: https://www.programiz.com/dsa/quick-sort, https://www.youtube.com/watch?v=Vtckgz38QHs&list=PLZPZq0r_RZON1eaqfafTnEexRzuHbfZX8&index=17&ab_channel=BroCode

def quickSort(arr, start, end):
    if end <= start:
        return
    pivot = partition(arr, start, end)
    quickSort(arr, start, pivot - 1)
    quickSort(arr, pivot + 1, end)


def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[end] = arr[end], arr[i]
    return i


arr = [6, 7, 8, 10, 125, 2, 3, 1]
quickSort(arr, 0, len(arr)-1)
print(arr)
