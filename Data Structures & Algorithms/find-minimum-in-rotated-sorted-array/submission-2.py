class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l)//2
            what = nums[0] + (nums[-1] - nums[0])//2 + 1
            if len(nums) == 1:
                return nums[0]
            # if min is at the start of the array
            if mid == 0:
                if nums[-1] > nums[mid]:
                    return nums[mid]
        
            if nums[mid-1] > nums[mid]:
                return nums[mid]

            if nums[mid] <= what:
                r = mid
            else:
                l = mid+1
