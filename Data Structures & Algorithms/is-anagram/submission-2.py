class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        ans = [0] *26
    
        for char in s:
            ans[ord(char)-ord('a')]+=1
        for char in t:
            ans[ord(char)-ord('a')]-=1
        return all(x==0 for x in ans)
    