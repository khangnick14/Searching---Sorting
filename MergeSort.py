# Merge Sort Algorithm:
# Principle: Divide & Conquer
# Two types: Top-Down MG & Bottom-Up MG
# Top-Down MG: use Recursion mechanism
#   + Divide: divide the initial array into subarray until it only contains 1 element (base case)
#   + Conquer: sort the subarray
#   + Combine each subarray:
#   Have we reached the end of any of the arrays?
#       No:
#           Compare current elements of both arrays
#           Copy smaller element into sorted array
#           Move pointer of element containing smaller element
#       Yes:
#           Copy all remaining elements of non-empty array
# Time Complexity: O(logn*n)
# Space Complexity: O(n)
# Link: https://www.programiz.com/dsa/merge-sort, https://www.youtube.com/watch?v=3j0SWDX4AtU&list=PLZPZq0r_RZON1eaqfafTnEexRzuHbfZX8&index=16&ab_channel=BroCode


def mergeSort(arr):
    length = len(arr)
    if (length <= 1):
        return  # base case

    mid = length//2

    leftArr = arr[:mid]
    rightArr = arr[mid:]

    # recursion each array
    mergeSort(leftArr)
    mergeSort(rightArr)

    # combine two array again
    merge(leftArr, rightArr, arr)


# merge step
def merge(leftArr, rightArr, arr):
    leftSize = len(arr)//2
    rightSize = len(arr) - leftSize
    l = r = i = 0

    while(l < leftSize and r < rightSize):
        if(leftArr[l] < rightArr[r]):
            arr[i] = leftArr[l]
            l += 1
        else:
            arr[i] = rightArr[r]
            r += 1
        i += 1

    while (l < leftSize):
        arr[i] = leftArr[l]
        i += 1
        l += 1
    while (r < rightSize):
        arr[i] = rightArr[r]
        i += 1
        r += 1


arr = [6, 7, 8, 10, 125, 2, 3, 1]
mergeSort(arr)
print(arr)
