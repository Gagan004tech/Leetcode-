class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        Hashmap={}

        for char in s:
            Hashmap[char]=Hashmap.get(char,0)+1

        for char in t:
            if char not in s or Hashmap[char]==0:
                return False
            Hashmap[char]-=1
        return True 

        