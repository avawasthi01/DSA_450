#Find nth fibonacci number


#using memoization
def fibo(n,l):
    if n<=1:
        return n
    if l[n]!=0:
        return l[n]
    a=fibo(n-1,l)
    b=fibo(n-2,l)
    l[n-1]=a
    l[n-2]=b
    return a+b
#using dp
def fibo_dp(n):
    l=[]
    l=[0]*(n+1)
    l[0]=0
    l[1]=1
    for i in range(2,n+1):
        l[i]=l[i-1]+l[i-2]
    print(l[n])



n=int(input())
l=[]
l=[0]*(n+1)
print(fibo(n,l))
fibo_dp(n)
