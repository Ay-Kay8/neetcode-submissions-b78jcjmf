class Solution:

    def encode(self, strs: List[str]) -> str:
        new_strs = []
        for s in strs:
            # Add % to make sure to know when the number ends
            new_strs.append(str(len(s)) + "%" + s)
        return "".join(new_strs)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        int_counter = 0
        while i < len(s): 
            if s[i] == '%':
                num_chars = int(s[int_counter:i])
                decoded.append(s[i+1:i+1+num_chars])
                i += num_chars
                int_counter = i + 1
            i += 1
        return decoded
