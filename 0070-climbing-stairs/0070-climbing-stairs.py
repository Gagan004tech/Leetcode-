class Solution:
    def climbStairs(self, n: int) -> int:
        # if n <=2 :
        #     return n
        # prev1 =1
        # prev2 =2
        # for i in range(3,n+1):
        #     temp =prev1+prev2
        #     prev1,prev2 = prev2,temp
        # return prev2
        one,two = 1,1
        for i in range(n-1):
            temp=one
            one=one+two
            two=temp
        return one
'''
Here Time Complexity:= O(n)
Here Space Complexity:= O(1)
'''
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n
#         dp=[0]*(n+1)
#         dp[1]=1
#         dp[2]=2
#         for i in range(3,n+1):
#             dp[i]=dp[i-1]+dp[i-2]
#         return dp[n]
# '''
#  Here Time Complexity:= O(n)
#  Here Space Complexity:= O(n)
#   '''     