def linear_search(seq, f):

    seq_size = len(seq)

    for i in range(0, seq_size-1):

        if seq[i] == f:
            return "Founded value: "+ str(seq[i])

    return "There is no such value."

seq = [1,2,5,6,7,8,9,44,46,71,79,88]

f = int(input("Value to search: "))

print(linear_search(seq, f))

"""
Worst Case: O(n)

"""