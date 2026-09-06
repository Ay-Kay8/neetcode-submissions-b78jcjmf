class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # We want the unsorted part so we can find the pivot
        while l < r:
            mid = l + (r - l) // 2

            # Pivot is definitely on the right side
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]