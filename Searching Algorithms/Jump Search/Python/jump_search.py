import math
def jump_searc(seq, f):

    seq_size = len(seq)
    jump_value = round(math.sqrt(seq_size))

    last_index = 0
    while seq[min(jump_value, seq_size)-1] < f: 
        
        last_index = jump_value 
        jump_value += round(math.sqrt(seq_size)) 
        if last_index >= seq_size: 
            return -1
      

    while seq[last_index] < f: 
        last_index += 1
 
        if last_index == min(jump_value, seq_size): 
            return -1

    if seq[last_index] == f: 
        return last_index 
    
    return -1

seq = [1,2,5,6,7,8,9,44,46,71,79,88]
f = int(input("Value to search: "))
print("Number" , f, "is at index" ,"%.0f"%jump_searc(seq, f)) 

"""
Time Complexity : O(√n)

"""
