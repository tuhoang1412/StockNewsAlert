import random

seq = random.sample(range(1, 100), 31)
print("Given: \n"+ str(seq))

"""
Time complexity for 3 cases: O(n^2). The minimum element is not known 
until the end of the array is not reached. Checking of all the elements is compulsory
Spce complexity: O(1) -> swapping
"""
#Selection sort: finding the min value and swap it back to the front
def sorting_selection(sequence):
    seq_len = len(seq)
    for i in range(seq_len):
        min_idx = i
        for j in range(i+1, seq_len):
            if sequence[min_idx] > sequence[j]:
                min_idx = j
        sequence[min_idx], sequence[i] = sequence[i], sequence[min_idx]
        
    print("Sorted: \n"+ str(sequence))


sorting_selection(seq)