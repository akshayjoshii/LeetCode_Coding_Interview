import numpy as np
import timeit

#O(n^2) - Simple solution
def pos_neg_simple(arr):
    t = []
    #2 for loops
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if(abs(arr[i]) == abs(arr[j])):
                t.append(abs(arr[i]))
    if(len(t)==0):
        return "No Positive/Negative pairs found"

    t.sort()
    for k in range(len(t)):
        print("\nThe pairs are {} & {}".format(t[k], -t[k]))


# O(n) - Optimised solution with Hash table
def pos_neg_hash(arr):
    t = {}
    v = []
    #Single for loop
    for i in range(len(arr)):
        if not abs(arr[i]) == t:
            t = arr[i]
        else:
            v.append(abs(arr[i]))
    
    if len(v) == 0:
        return "No match"
    
    v.sort()
    v = np.array(v)
    #v[:] = map(lambda x: -x, v)))
    print(v, -v)

if __name__ == "__main__":
    ar = input().split(' ')
    ar = [int(num) for num in ar]
    print(pos_neg_simple(ar))