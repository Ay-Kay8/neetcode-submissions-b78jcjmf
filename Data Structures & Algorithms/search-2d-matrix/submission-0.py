class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        u, d = 0, len(matrix)
        while u < d:
            mid_row = u + (d - u)//2
            if matrix[mid_row][0] > target:
                d = mid_row
            elif matrix[mid_row][cols - 1] < target:
                u = mid_row + 1
            else:
                # break when value is between the bounds of the curr row
                break
        # regular bin search on the curr row
        row = matrix[mid_row]
        l, r = 0, cols
        while l < r:
            mid = l + (r - l)//2
            if row[mid] == target:
                return True

            if row[mid] > target:
                r = mid
            elif row[mid] < target:
                l = mid + 1
        return False