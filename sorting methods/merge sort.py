sequence = [20, 5, 3, 7, 8, 11,15, 1, 22, 44, 4, 18, 34, 3, 25, 28, 31]
print("Given: \n"+ str(sequence))


"""
Divide and conquer, stable.
Merge Sort is useful for sorting linked lists in O(nLogn) time.
Time complexity: θ(nLogn) in all 3 cases: worst, average and best as merge sort always divides 
the array into two halves and takes linear time to merge two halves.
It is used for External sorting, inversion count problem.
Space complexity: O(n)
"""

def sorting_merge(array):
    if len(array) > 1:
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]
        sorting_merge(left)
        sorting_merge(right)

        i = j = k = 0
        # Re-arranging the partitional array
        while (i < len(left)) and (j < len(right)):
            if(left[i] < right[j]):
                array[k] = left[i]
                i += 1
            else: 
                array[k] = right[j]
                j +=1
            k+=1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    
    
sorting_merge(sequence)
print("Sorted: \n"+ str(sequence))