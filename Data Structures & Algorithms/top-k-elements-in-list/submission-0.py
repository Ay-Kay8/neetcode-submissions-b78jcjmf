from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        sorted_d = dict(sorted(d.items(), key = lambda i : -i[1]))
        return list(sorted_d)[:k]