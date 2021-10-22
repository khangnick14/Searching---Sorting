# Bubble Sort Algorithm

# Pairs of adjacent elemtns are compared
# The elements swapped if they are not in order
# Quadratic time complexity: O(n^2)
# O(1) space complexity
# Only good for small data set
# Link: https://www.youtube.com/watch?v=Dv4qLJcxus8&list=PLZPZq0r_RZON1eaqfafTnEexRzuHbfZX8&index=12&ab_channel=BroCode


def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]  # swap value
    return arr


arr = [6, 7, 8, 10, 125, 2, 3, 1]
print(bubbleSort(arr))
