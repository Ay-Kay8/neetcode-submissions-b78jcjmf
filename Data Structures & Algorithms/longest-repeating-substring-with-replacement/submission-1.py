from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        freq = defaultdict(int) # "A" -> 3
        longest = 0

        while r < len(s):
            win_length = r - l + 1

            # most_common is the most common letter in the current window
            # Since there are 26 letters in the alphabet, this is O(26)
            freq[s[r]] += 1
            most_common = max(freq.values())
            print("most_common: ", most_common)
            print(list(freq.items()))
            
            # Window is invalid, meaning there is a letter than can't be replaced
            if (win_length - most_common) > k:
                freq[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
            # NOT THIS: you must recompute the window length
            # longest = max(longest, win_length)
            if longest < r - l + 1:
                longest = r - l + 1
            # Increment r everytime
            r += 1

        return longest