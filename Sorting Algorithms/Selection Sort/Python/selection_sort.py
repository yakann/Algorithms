import sys

seq = [5,2,7,44,9,6,88,8]
print("Sequence: ", seq)

for i in range(0, len(seq)):

    min_value = i
    for j in range(i+1, len(seq)):
        if seq[min_value] > seq[j]:
            min_value = j

    seq[i],seq[min_value] = seq[min_value],seq[i]

print("Sequence: ", seq)

"""
Worst Case : O(n^2),
Best Case : O(n^2)

These two are the same. Because it always has to go into both cycles.

"""