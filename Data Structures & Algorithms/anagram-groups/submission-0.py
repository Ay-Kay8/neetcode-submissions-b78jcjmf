from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for str in strs:
            sorted_str = "".join(sorted(str))
            dict[sorted_str].append(str)
        return list(dict.values())