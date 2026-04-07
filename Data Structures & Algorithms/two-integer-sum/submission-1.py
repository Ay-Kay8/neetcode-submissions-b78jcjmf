class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {nums[0]: 0}
        for i in range(1, len(nums)):
            print(dict)
            diff = target - nums[i]
            if diff in dict.keys():
                return [dict[diff], i]
            dict[nums[i]] = i