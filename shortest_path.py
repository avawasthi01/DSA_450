from sys import stdin
MAX_VALUE = 2147483647
def find_memo(l,m,n,i,j,arr):
    if i==m-1 and j==n-1:
        return l[i][j]
    if i>=m or j>=n:
        return MAX_VALUE
    if arr[i][j]!=-1:
        return arr[i][j]
    
    x=find_memo(l,m,n,i,j+1,arr)
    y=find_memo(l,m,n,i+1,j,arr)
    z=find_memo(l,m,n,i+1,j+1,arr)
    a=min(x,min(y,z))+l[i][j]
    arr[i][j]=a
    return a


def find_dp(l,n,m,arr):
    MAX_VALUE=12345679
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            right=MAX_VALUE
            dia=MAX_VALUE
            down=MAX_VALUE
            if j+1<=n-1:
                right=arr[i][j+1]
                
            if i+1 <=m-1  and j+1<=n-1:
                dia=arr[i+1][j+1]
               
            if i+1<=m-1:
                down=arr[i+1][j]
               
            x=min(right,min(dia,down))
            
            if x== MAX_VALUE:
                arr[i][j]=l[i][j]
               
                
            else:
                arr[i][j]=l[i][j]+x
           
    return arr[0][0]



m,n=input().split()
m=int(m)
n=int(n)
l=[]
arr=[[-1]*(n) for i in range(m)]
for i in range(m):
    x=[int(i) for i in input().split()]
    l.append(x)
print(find_memo(l,m,n,0,0,arr))
print(find_dp(l,m,n,arr))
