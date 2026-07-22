class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        HashSet=set()

        for i in range(0,len(nums)):
            HashSet.add(nums[i])
        
        long_streak=0
        for i in HashSet:
            curr=i
            if curr-1 not in HashSet:
                curr_streak=1
                while curr+1 in HashSet:
                    curr_streak+=1
                    curr+=1
                long_streak=max(curr_streak,long_streak)
        return long_streak
        