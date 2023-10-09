'''

NOTE:  Please use 'python3' command when running this coe
AUTHOR: Rohan Rele

'''

import numpy as np
import time

def reverse_copy_selection_sort(A):

    neg_inf = -1000000 # negative infinity value for convenience
    B = [neg_inf]*len(A) # create integer array (list) of length(A)
    for i in range(len(A)): # n := len(A) runs of the outer loop
        max_dex = 0 # set max index to 0 position
        for j in range(len(A)): # n:= len(A) runs of the inner loop
            if A[j] > A[max_dex]: # if the pointer element is greater than the current max
                max_dex = j # set the new max index to that element

        B[len(A) - 1 - i] = A[max_dex] # set the (n-i)th element to be the (i+1)th greatest value in A
        A[max_dex] = neg_inf # to avoid repeats, "destroy" the original element in A

    return B # return sorted list

"""
def reverse_copy_insertion_sort(A):

    n = len(A)
    B = [-1 for i in range(n)]
    for i in range(n):
        j = i;
        swap_occurred = False
        while j > 0 and A[j-1] < A[j]:
            swap_occurred = True
            temp = A[j]
            A[j] = A[j-1]
            A[j-1] = temp
            j = j - 1

        B[n-1-i] = A[i]

    return B, A
"""

#A = [4,3,2,7,5]
# print(reverse_copy_insertion_sort(A))

"""
5.1 generate n random numbers between 0 and 999 and store these in array A
"""
size = 10 # input value n := size
A = np.random.randint(1000,size=size)
"""
5.2 implement sorting algorithm and use hte array generated in 5.1 as input
"""
print(reverse_copy_selection_sort(A))

"""
5.3 print execution time for the following input sizes
"""

sizes = [10,100,500,1000] #,10000]
for size in sizes:
    arr = np.random.randint(1000,size=size)
    '''
    arr.sort()
    arr = arr[::-1]
    if size == 10:
        print(arr)
    '''
    start_time = time.time()
    reverse_copy_selection_sort(arr)
    exec_time = time.time() - start_time
    print("Array of size",size,"took",exec_time, "s")
