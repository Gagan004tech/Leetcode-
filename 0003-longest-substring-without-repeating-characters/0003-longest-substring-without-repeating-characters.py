class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leaf=max_l=0
        char_set=set()

        for right in range(0,len(s)):
            while s[right] in char_set:
                char_set.remove(s[leaf])
                leaf+=1
            char_set.add(s[right])
            max_l=max(max_l,right-leaf+1)
        return max_l


        