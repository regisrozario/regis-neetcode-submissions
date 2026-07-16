class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        scanned_rows = 0
        rows = len(matrix)-1
        col = len(matrix[0])-1
        
        if target < matrix[0][0] or target > matrix[rows][col]:
            return False

        while scanned_rows <= rows:
            if self.binary_search(matrix[scanned_rows], target):
                return True
            scanned_rows +=1
        
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

