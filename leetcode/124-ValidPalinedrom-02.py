import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        p = re.compile('[a-zA-Z0-9]')
        for w in s:
            if p.match(w):
                s1 += w.lower()
        rev = s1[::-1]
        if s1 == rev:
            return True
        else:
            return False
