class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        Hashmap={}
        for num in nums:
            Hashmap[num]=Hashmap.get(num,0)+1
        return heapq.nlargest(k,Hashmap.keys(),key=Hashmap.get)
        
        