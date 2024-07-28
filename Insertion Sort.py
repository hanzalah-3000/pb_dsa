def InsertionSort(A):
    for i in range(len(A)):
        key = A[i] 
        j= i-1

        while j>=0 and key<A[j]:
            A[j+1]= A[j]
            j-=1
        
        A[j+1]= key
A=[3,2,1]
InsertionSort(A)