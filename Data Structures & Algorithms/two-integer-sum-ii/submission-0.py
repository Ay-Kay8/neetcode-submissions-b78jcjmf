class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while True:
            print(numbers[l] + numbers[r])
            if numbers[l] + numbers[r] > target:
                r -= 1
                print("r", r)
            elif numbers[l] + numbers[r] < target:
                l += 1
                print("l", l)
            else:
                return [l + 1, r + 1]
