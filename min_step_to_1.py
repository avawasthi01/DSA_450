from sys import stdin
from sys import maxsize as MAX_VALUE



def countMinStepsToOne(n,l) :
    if n==1:
        return 0
    if n==2 or n==3:
        return 1
    if l[n-1] !=-1:
        x=1+l[n-1]
    else: 
    	x=1+countMinStepsToOne(n-1,l)
    y=n+1
    z=n+1
    if(n%2==0):
        if l[n//2]!=-1:
            y=1+l[n//2]
        else:
        	y=1+countMinStepsToOne(n//2,l)
    if(n%3==0):
        if l[n//3]!=-1:
            z=1+l[n//3]
        else:
        	z=1+countMinStepsToOne(n//3,l)
    a=min(y,z)
    l[n]=min(a,x)
    return min(a,x)



#main
n = int(stdin.readline().rstrip())
l=[]
l=[-1]*(n+1)
print(countMinStepsToOne(n,l))