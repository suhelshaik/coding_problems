import sys
def construct_tree(arr,seg_tree,low,high,pos):
    if low==high:
        seg_tree[pos]=arr[low]
        return
    mid=(low+high)//2
    construct_tree(arr,seg_tree,low,mid,(2*pos)+1)
    construct_tree(arr,seg_tree,mid+1,high,(2*pos)+2)
    seg_tree[pos]=min(seg_tree[2*pos+1],seg_tree[2*pos+2])

def rmq(seg_tree,qlow,qhigh,low,high,pos):
    if qlow<=low and qhigh>=high:
        return seg_tree[pos]
    if qlow>high or qhigh<low:
        return sys.maxsize
    mid=(low+high)//2
    return min(rmq(seg_tree,qlow,qhigh,low,mid,2*pos+1),rmq(seg_tree,qlow,qhigh,mid+1,high,2*pos+2))

arr=list(map(int,input().split()))
if bin(len(arr))[2:].count('1')==1:
    k=(len(arr)<<1)-1
    seg_tree=[sys.maxsize for i in range(k)]
else:
    k=1<<len(bin(len(arr))[2:])
    k=k*2-1
    seg_tree=[sys.maxsize for i in range(k)]
construct_tree(arr,seg_tree,0,len(arr)-1,0)
print(seg_tree)
print(rmq(seg_tree,4,6,0,len(arr)-1,0))
