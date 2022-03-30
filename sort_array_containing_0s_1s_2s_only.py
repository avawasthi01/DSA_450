def sort012(arr,n):
        # code here
        z=0
        o=0
        t=0
        for i in arr:
            if i == 0:
                z=z+1
            elif i == 1:
                o=o+1
            else:
                t=t+1
        for i in range(n):
            if(z!=0):
                arr[i]=0
                z=z-1
            elif(o!=0):
                arr[i]=1
                o=o-1
            else:
                arr[i]=2
                t=t-1
        return arr

if __name__ == '__main__':
    arr=[int(i)for i in input().split()]
    print(sort012(arr,len(arr)))