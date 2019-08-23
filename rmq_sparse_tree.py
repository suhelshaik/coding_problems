import math
def preprocess(arr):
    n=len(arr)
    sparse=[[0 for i in range(math.ceil(math.log(n)+1))] for j in range(n)]
    for i in range(0,n):
        sparse[i][0]=i
    for j in range(1,n):
        if 2**j<=n:
            for i in range(n):
                if i+2**j-1<n:
                    if arr[sparse[i][j-1]]<arr[sparse[i+2**(j-1)][j-1]]:
                        sparse[i][j]=sparse[i][j-1]
                    else:
                        sparse[i][j]=sparse[i+2**(j-1)][j-1]
                else:
                    break
        else:
            break
    return sparse

def rmq(arr,low,high,sparse):
    l=high-low+1
    k=math.log(l)
    k=math.floor(k)
    return min(arr[sparse[low][k]],arr[sparse[low+l-2**k][k]])


arr=list(map(int,input().split()))
sp=preprocess(arr)
print(rmq(arr,0,3,sp))
