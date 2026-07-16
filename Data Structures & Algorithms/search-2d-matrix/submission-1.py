class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bot = 0, len(matrix) - 1
        
        while top <= bot:
            mid = (top + bot) // 2

            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid -1
            else:
                return self.binary_search(matrix[mid], target)

        return False
        
    


    def binary_search(self, nums:list[int], target: int) -> bool:
        low,high = 0,len(nums)-1
        
        while low <= high:
            mid = (low+high) //2
            if nums[mid] == target:
                return True
            if nums[mid] > target:
                high = mid -1
            else:
                low = mid +1
        return False

