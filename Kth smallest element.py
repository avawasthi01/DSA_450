#Find the Kth smallest element

def kth_smallest_ele(arr,k):
    arr.sort()
    return (arr[k-1])

if __name__ == '__main__':
    arr=[int(i) for i in input().split()]
    k=int(input())
    print(kth_smallest_ele(arr,k))