def BubbleSort(A):
  for i in range(len(A)):
    for j in range(len(A)-i-1):
      if A[j+1]<A[j]:
          temp= A[j]
          A[j]= A[j+1]
          A[j+1]=temp
A=[98,65,43,2]
BubbleSort(A)
print(A)
