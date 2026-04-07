from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.dict = defaultdict(list)

    # all calls for set will always be sorted   
    def set(self, key: str, value: str, timestamp: int) -> None: # O(1)
        self.dict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str: # (Olog(n))
        if key not in self.dict.keys():
            return ""
        
        list = self.dict[key]

        # If whatever timestamp is smaller than all values
        if timestamp < list[0][1]:
            return ""
        
        l, r = 0, len(list) - 1
        while l <= r:
            mid = l + (r - l)//2
            if timestamp == list[mid][1]:
                return list[mid][0]
            if timestamp < list[mid][1]:
                r = mid - 1
            else:
                l = mid + 1
        # return whatever value is immediately less than timestamp
        return list[r][0]
