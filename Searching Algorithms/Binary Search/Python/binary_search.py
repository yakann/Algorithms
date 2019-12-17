def binarySearch(seq,f):
    left = 0
    right = len(seq)-1
    
    while left <= right:
        mid = round((left + right)/2)

        if seq[mid] == f:
            return seq[mid]
        elif seq[mid] < f:
            left = mid + 1
        else:
            right = mid - 1

seq = [1,2,5,6,7,8,9,44,46,71,79,88]

print("Searched number: 88")
print("Result: ",binarySearch(seq,88))

"""
Worst Case: O(Logn)
Best Case: O(1)

Time Complexity: T(n) = T(n/2) + c 
"""