import random

seq = random.sample(range(1, 100), 31)
print("Given: \n"+ str(seq))
"""
Time complexity: O(n^2) for average and worst case. O(n) for best case when the array is already
sorted. Worst case is when reversed order.
Space complexity: O(1) -> key
"""

#Insertion sort

def sorting_insertion(sequence):
    seq_len = len(seq)
    for idx in range(1, seq_len):
        key = sequence[idx]
        j = idx - 1
        while(j >= 0 and sequence[j] > key):
            sequence[j+1] = sequence[j]
            j = j - 1
        sequence[j+1] = key
    print("Sorted: \n"+ str(sequence))

sorting_insertion(seq)