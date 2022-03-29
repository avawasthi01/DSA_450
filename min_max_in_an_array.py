#find min and max in an array

def min_max(a,n):
    max = a[0]
    min = a[0]
    for i in a:
        if i>=max:
            max=i
        if i<=min:
            min=i
    return min,max

if __name__ == '__main__':
    arr=[int(i) for i in input().split()]
    print(min_max(arr,len(arr)))