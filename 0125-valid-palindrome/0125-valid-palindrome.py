class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        start=0
        last=len(s)-1
        while start<last:
            if not s[start].isalnum():
                start+=1
                continue
            if not s[last].isalnum():
                last-=1
                continue
            if s[start]==s[last]:
                start+=1
                last-=1
            else:
                return False
        return True
        