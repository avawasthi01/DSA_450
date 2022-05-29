#apprach -- the part which is giving negative sum will not benefit the max sum,so ignore the sub array giving negative sum.
#so I made max = -infinity,then start calculating sum of elements,until the sum is positive,if the sum if neg then,reseting the sum,after comparing it with
#with the current max.

class Solution:
   
   
    def maxSubArraySum(self,arr,N):
        sum=0
        max1=-999999999
        for i in range(N):
            sum=sum+arr[i]
            if sum<0:
                sum=0
            elif max1<sum:
                    max1=sum
        if max1==-999999999:
            max1=max(arr)
        return max1
            
            
        
        
        ##You code here
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends