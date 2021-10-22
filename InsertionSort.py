# Insertion Sort Algorithm:

# Loop i from 1 to the end of array: set value of each iter to temp variable
# Set j equal to i - 1
# While j >=0 and value at index j is larger than temp, shift each value to the right
# Assign value of temp to the index j + 1
# Quadratic time complexity: O(n^2)
# O(1) space complexity
# Only good for small data set
# Link: https://www.youtube.com/watch?v=8mJ-OhcfpYg&list=PLZPZq0r_RZON1eaqfafTnEexRzuHbfZX8&index=14&ab_channel=BroCode


def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while(j >= 0 and arr[j] > temp):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr


arr = [6, 7, 8, 10, 125, 2, 3, 1]
print(insertionSort(arr))
