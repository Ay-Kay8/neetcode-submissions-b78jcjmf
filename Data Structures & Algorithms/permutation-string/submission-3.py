class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq = defaultdict(int)
        for s in s1:
                freq[s] += 1

        s2_freq = defaultdict(int)
        l, r = 0, 0
        # Get r into position so that the win size is len(s1)
        while r < len(s1):
            s2_freq[s2[r]] += 1
            r += 1

        while r < len(s2):
            print(list(s2_freq.items()), ":", list(freq.items()))
            
            if s2_freq == freq:
                return True
            # Move and update left pointer
            s2_freq[s2[l]] -= 1
            if s2_freq[s2[l]] == 0:
                del s2_freq[s2[l]]
            l += 1

            # Move and update right pointer
            s2_freq[s2[r]] += 1
            r += 1

        # If the correct substring is at the very end, loop will terminate, leaving one extra comparison to
        # be made
        if s2_freq == freq:
                return True

        return False