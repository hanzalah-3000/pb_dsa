def selectionSorting(A):
    for i in range(len(A)):
        min= i
        for j in range(i+1,len(A)):
            if A[min]>A[j]:
                min=j
        A[i],A[min] = A[min],A[i]
    print(A)   
array= [15,9,3,16,100,30]
print(array)
selectionSorting(array)
