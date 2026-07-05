class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # skip the last 2 digits since they'll always stay the same
        if len(nums) != 2:
            for i in range(len(nums) - 3, -1, -1):
                if i == len(nums) - 3:
                    nums[i] += nums[i+2]
                    continue
                
                nums[i] += max(nums[i+2], nums[i+3])

        print(nums)
        return max(nums[0], nums[1])