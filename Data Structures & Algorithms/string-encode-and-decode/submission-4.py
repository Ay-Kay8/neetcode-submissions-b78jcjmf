class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + '/' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '/':
                j += 1
            # s[i:j] is everything from i to j, excluding i
            length = int(s[i:j])
            # j = i + the number
            # + 1 = for '/'
            decoded.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return decoded

