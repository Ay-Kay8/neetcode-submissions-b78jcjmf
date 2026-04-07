class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for str in strs:
            encoded += str + '/'
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        word = ""
        for char in s:
            if(char == "/"):
                decoded.append(word)
                word = ""
            else:
                word += char
        return decoded
