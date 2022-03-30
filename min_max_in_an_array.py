#find min and max in an array
#Using Iterative method


def min_max(a,n):
    max = a[0]
    min = a[0]
    for i in a:
        if i>=max:
            max=i
        if i<=min:
            min=i
    return min,max


#tournament method
def min_max_recur(arr,start,end):
    if start == end:
        min=max=arr[start]
        return min,max
    if end == start+1:
        if(arr[start]>arr[start+1]):
            max=arr[start]
            min=arr[start+1]
            return min,max
        else:
            max=arr[start+1]
            min=arr[start]
            return min,max
    mid = (start+end)//2
    min1,max1=min_max_recur(arr,start,mid)
    min2,max2=min_max_recur(arr,mid+1,len(arr)-1)
    if(min1<min2):
        minf=min1
    else:
        minf=min2
    if(max1>max2):
        maxf=max1
    else:
        maxf=max2
    return minf,maxf

def min_max_using_pair(arr,len):
    if len == 1:
        return arr[0],arr[0]
    if len == 2:
        if(arr[0]>arr[1]):
            return arr[1],arr[0]
        else:
            return arr[0],arr[1]
    if len % 2 ==0:
        start = 2
        if arr[0]>arr[1]:
            max=arr[0]
            min=arr[1]

        else:
            min=arr[0]
            max=arr[1]
    else :
        min=arr[0]
        max=arr[0]
        start=1
    for i in range(start,len-1):
        p1=arr[i]
        p2=arr[i+1]
        if(p1>p2):
            if(p1>max):
                max=p1
            if(p2<min):
                min=p2
        if(p2>p1):
            if(p2>max):
                max=p2
            if(p1<min):
                min=p1
        i=i+2
    return min,max





if __name__ == '__main__':
    arr=[int(i) for i in input().split()]
    print(min_max_using_pair(arr,len(arr)))
    print(min_max_recur(arr,0,len(arr)-1))
    print(min_max(arr,len(arr)))