class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = "".join(char.lower() for char in s if char.isalnum())
        rev = temp[::-1]
        return rev==temp
        