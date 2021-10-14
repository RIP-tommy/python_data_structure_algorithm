class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for w in s:
            if w.isalnum():
                s1 += w.lower()
        rev = s1[::-1]
        print(s1, rev)
        if s1 == rev:
            return True
        else:
            return False
