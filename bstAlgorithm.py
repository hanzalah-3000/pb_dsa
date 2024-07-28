def BST(A,start,end,key,mid):
    
    if key<A[mid]:
        mid//=2
        BST(A,start,mid-1,key,mid)
    

    elif key>A[mid]:
        BST(A,mid+1,end,key,mid+1)

    else:
        print(mid)
try:   
    a=["a",'b','c','d']
    BST(a,"a",(len(a)-1),"d",len(a)//2)

except:
    print("Not Found")
