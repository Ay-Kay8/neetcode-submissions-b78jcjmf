class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        l, r = 0, 1
        visited = set(s[l])
        longest = 1
        while r < len(s):
            
            if s[r] not in visited:
                visited.add(s[r])

                # Track the highest size 
                if longest < len(visited):
                    longest = len(visited)
                r += 1
            else:
                visited.remove(s[l])
                l += 1
        
        return longest