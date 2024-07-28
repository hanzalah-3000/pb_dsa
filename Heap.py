def maxHeap(A,n):
    temp=A[n]
    i= n
    while (i>1 and temp>A[i//2]):
        A[i]=A[i//2]
        i//=2
        A[i]= temp
        
def delHeap(A,n):
    i=1
    A[i]= A[n]
    A.pop()
    j=2*i
    while j<n-1:
        if A[j+1]>A[j]:
            j+=1
        if A[i]<A[j]:
            A[i],A[j]=A[j],A[i]
        i=j
        j=2*i

A=[0,30,15,20,5,10,40]
maxHeap(A,len(A)-1)           
print(A[1:])
delHeap(A,len(A)-1)
print(A[1:])
delHeap(A,len(A)-1)
print(A[1:])
delHeap(A,len(A)-1)
print(A[1:])
    
 
















