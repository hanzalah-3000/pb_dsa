def Merging(A,left,right):
    a,b,c=0,0,0

    while (a<len(left) and b<len(right)):
        if left[a]<right[b]:
            A[c]= left[a]
            a+=1
        else:
            A[c]= right[b]
            b+=1
        c+=1
    
    while (a<len(left)):
        A[c]= left[a]
        a+=1
        c+=1
    
    while (b<len(right)):
        A[c]= right[b]
        b+=1
        c+=1

    return A

def MergeSort(A):
    if(len(A)>1):
        mid= len(A)//2
        left= A[:mid]
        right= A[mid:]

        MergeSort(left)
        MergeSort(right)
        Merging(A,left,right)

l1= [9,3,5,8,3,11,19]
print(l1)
MergeSort(l1)
print(l1)