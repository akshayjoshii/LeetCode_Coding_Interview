# Kadane Algorithm / Largest Sum Contiguous Subarray:
# Write an efficient program to find the sum of contiguous subarray within 
# a one-dimensional array of numbers which has the largest sum.

# DP approach
# Time Complexity: O(n)

def maxSubArray(array):
    current = array[0]
    maxval = array[0]
    indice = []
    length = len(array)
    for i in range(1, length):
        current = max(array[i], current + array[i])
        if current > maxval:
            indice.append((array[i], i))
        maxval = max(maxval, current)
    return maxval, indice


if __name__== "__main__":
    # a = [-2, -3, 4, -1, -2, 1, 5, -3]
    b = [-10, 2, 4, 9, -2, -7, 1, 2, 6, -7]
    result, indices = maxSubArray(b)
    print(f"Largest Sum of a continous subarray is: {result}")
    print("The elements picked from the subarray are:")
    for value, index in indices:
        print(f"Value: {value} & it's index is: {index}")
        