def merge(L, R):
    print(L)
    print(R)
    L_i, R_i = 0, 0
    temp = []
    
    while (L_i < len(L)) and (R_i < len(R)):
        if (L[L_i] < R[R_i]):
            temp.append(L[L_i])
            L_i = L_i + 1
        else:
            temp.append(R[R_i])
            R_i = R_i + 1
            
    if L_i == len(L):
        temp.extend(R[R_i:])
    elif R_i == len(R):
        temp.extend(L[L_i:])
    print(temp)
        
    return temp

def mergesort(A):
    
    if (len(A) <= 1):
        return A
    
    mid_point = len(A)//2
    left_side = A[:mid_point]
    right_side = A[mid_point:]
    print("A is:", A)
    left_side = mergesort(left_side)
    right_side = mergesort(right_side)
    
    print("MERGING")
    return merge(left_side, right_side)

def in_place_merge(A, left_start, left_end, right_start, right_end):
    print("left indices:", left_start, left_end)
    print("right indices:", right_start, right_end)
    L_i, R_i = left_start, right_start
    
    while (L_i <= left_end) and (R_i <= right_end):
        if (A[L_i] < A[R_i]):
            R_i = R_i + 1
        else:
            swap(A, L_i, R_i)
            L_i = L_i + 1

def in_place_mergesort(A, left_pt, right_pt):
    
    if ((right_pt-left_pt) <= 1):
        return
    
    mid_point = ((right_pt - left_pt) // 2) + left_pt
    in_place_mergesort(A, left_pt, mid_point)
    in_place_mergesort(A, mid_point, right_pt)
    
    print("MERGING")
    in_place_merge(A, left_pt, mid_point-1, mid_point, right_pt-1)
    print(A)

def swap(A, index_1, index_2):
    temp = A[index_1]
    A[index_1] = A[index_2]
    A[index_2] = temp

def partition(A, p):
    i, j = 0, len(A)-1
    while (i < j):
        while (A[i] < p):
            i = i+1
        while (A[j] > p):
            j = j-1
        swap(A, i, j)

def quicksort(A):
    print("A is:", A)
    
    if (len(A) <= 1):
        return A
    
    mid_index = len(A)//2
    print("mid_index is:", mid_index)
    pivot = A[mid_index]
    print("pivot is:", pivot)
    partition(A, pivot)
    print("Post-Partition:", A)
    left_side = A[:mid_index]
    right_side = A[mid_index:]
    left_side = quicksort(left_side)
    right_side = quicksort(right_side)
    print(left_side, right_side)
    return left_side+right_side

def in_place_partition(A, pivot, left_start, right_end):
    while (left_start < right_end):
        while (A[left_start] <= pivot) and (left_start < right_end):
            left_start = left_start + 1
        while (A[right_end] > pivot) and (right_end > left_start):
            right_end = right_end - 1
        swap(A, left_start, right_end)

def in_place_quicksort(A, left_pt, right_pt):
    print("Array is:", A)
    
    if (right_pt-left_pt <= 1):
        return
    
    mid_index = (left_pt + right_pt)//2
    pivot = A[mid_index]
    print("Pivot is:", pivot, "at index:", mid_index)
    in_place_partition(A, pivot, left_pt, right_pt)
    print("Post-partition:", A)
    in_place_quicksort(A, left_pt, mid_index)
    in_place_quicksort(A, mid_index, right_pt)
    
    return

def complete_heapify(A, left_pt, right_pt):
    for i in range (left_pt+1, right_pt):
        bubble_up(A, i, (i-1)//2)

def bubble_up(A, i, j):
    if A[i] > A[j]:
        swap(A, i, j)
        bubble_up(A, j, j//2)
    return


def sink_down(A, i, working_range):
    left_child_index = (i*2) + 1
    right_child_index = (i*2) + 2
    
    #make sure you are within the working range
    if (left_child_index > working_range):
        return
    elif (right_child_index > working_range):
        swap_index = left_child_index
    elif (A[left_child_index] > A[right_child_index]):
        swap_index = left_child_index
    else:
        swap_index = right_child_index
    
    if (A[i] < A[swap_index]):
        swap(A, i, swap_index)
        sink_down(A, swap_index, working_range)
    else:
        return

def heapsort(A):
    print("Initiating heapify")
    complete_heapify(A, 0, len(A))
    print("Heapify complete. Result is:", A)
    print(" ")
    for i in range(len(A)-1):
        print("Swapping", A[0], "and", A[len(A)-(i+1)])
        swap(A, 0, len(A)-(i+1))
        print("Swap complete. Result is", A)
        print("Beginning sink")
        sink_down(A, 0, len(A)-(i+2))
        print("Sink Complete. Result is:", A)
        print(" ")
        
A = [ 1, -1, 4, 16, 3, 7, 0, -4]
in_place_mergesort(A, 0, len(A))
print(A)
