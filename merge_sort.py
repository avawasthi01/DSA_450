def merge(arr,start,mid,end):
    i=start
    end1=mid
    j=mid+1
    end2=end
    l=[]
    while(i<=end1 and j<=end2):
        if arr[i] >= arr[j]:
            l.append(arr[j])
            j=j+1
        else:
            l.append(arr[i])
            i=i+1
    while(i<=end1):
        l.append(arr[i])
        i=i+1
    while j<=end2:
        l.append(arr[j])
        j=j+1
    k=start
    for i in range(0,len(l)):
        arr[k]=l[i]
        k=k+1
    
        
        

def mergeSort(arr, start, end):
    # Please add your code here
    if start<end:
        mid=(start+end)//2
        mergeSort(arr,start,mid)
        mergeSort(arr,mid+1,end)

        merge(arr,start,mid,end)
        


# Main



n=int(input())
arr=[int(i) for i in input().split()]
mergeSort(arr,0,n-1)
for i in arr:
    print(i,end=" ")