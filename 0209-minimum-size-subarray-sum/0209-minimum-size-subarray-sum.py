class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        right=0
        count=float('inf')
        curr_sumW=0
        
        for right in range(0,len(nums)):
            curr_sumW+=nums[right]

            while curr_sumW >=target:
                count=min(count,right-left+1)
                curr_sumW-=nums[left]
                left+=1
        return count if count!=float('inf') else 0
        