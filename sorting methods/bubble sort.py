import random

seq = random.sample(range(1, 100), 31)
sorted_seq = [2, 3, 5, 7, 8, 13, 14, 16, 21, 32, 33, 34, 38, 43, 54, 56, 59, 61, 
            63, 72, 73, 74, 78, 79, 84, 85, 86, 87, 93, 94, 96]

print("Given: \n"+ str(seq))

#Bubble sort: move the largest number to the top
"""
Best case: O(n) comparisons when the array is already sorted
Same amount of comparisons O(n^2) for the other 2:
Average case: O(n^2) swaps, actually half of the worst case
Worst case: O(n^2) swaps when the array is in reversed order
Space complexity: O(1) -> swapping
"""

#Original method
def Orgn(sequence):
    seq_len = len(sequence)
    for i in range(seq_len):
        for j in range(seq_len - i - 1):
            if sequence[j] > sequence [j+1]:
                sequence[j], sequence [j+1] = sequence [j+1], sequence [j]
                
    print("Sorted: \n"+ str(sequence))


#Optimized method
def Optm(sequence):
    itr_len = len(sequence)
    while (itr_len > 0):
        last_swap = 0
        for i in range(itr_len - 1):            
            if sequence[i] > sequence [i+1]:
                sequence[i], sequence [i+1] = sequence [i+1], sequence [i]
                last_swap = i + 1
        itr_len = last_swap
        
    print("Sorted: \n"+ str(sequence))



Optm(sorted_seq)

