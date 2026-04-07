from collections import defaultdict
import string

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alph = defaultdict()
        for k in string.ascii_lowercase:
            alph[k] = 0
        for i in range(len(s)):
            alph[s[i]] += 1
            alph[t[i]] -= 1
        return all(k == 0 for k in alph.values())    
