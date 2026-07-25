class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.rob1(nums[1:]),self.rob1(nums[:-1]))

    def rob1(self,vals):
        rob1,rob2=0,0
        for n in vals:
            temp=max(n+rob1,rob2)
            rob1=rob2
            rob2=temp
        return rob2
        