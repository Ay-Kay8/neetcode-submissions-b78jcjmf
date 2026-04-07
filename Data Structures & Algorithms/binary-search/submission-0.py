class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.searchRecursion(nums, 0, len(nums) - 1, target)

    def searchRecursion(self, nums, left, right, target):

        if left > right:
            return -1
        
        mid = left + (right - left)//2
        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            return self.searchRecursion(nums, mid+1, right, target)
        elif nums[mid] > target:
            return self.searchRecursion(nums, left, mid-1, target)
            