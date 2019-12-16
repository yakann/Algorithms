seq = [5,2,7,44,9,6,88,8]

for i in range(len(seq)):

    for j in range (0,len(seq)-i-1):

        if seq[j] > seq[j+1]:
            seq[j], seq[j+1] = seq[j+1], seq[j]

print("Sequence: ", seq)
"""
Worst Case: O(n^2)
Best Case: O(n)

"""