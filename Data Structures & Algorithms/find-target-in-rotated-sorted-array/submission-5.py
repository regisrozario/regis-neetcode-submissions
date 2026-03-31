class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) -1
        # 1. identify the pivot point
        pivote = -1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid +1
            else:
                r = mid
        pivote = l

        # 2. identify which portion the target is there
        if nums[pivote] <= target <= nums[-1]: # check if target is in the right side of the array, if so, we will do binary search on the right side, otherwise we will do binary search on the left side.
                #search right
            n_l,n_r = pivote, len(nums) -1
        else:
            n_l,n_r = 0, pivote -1
        
        while n_l <= n_r:
            mid = (n_l + n_r)//2

            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                n_r = mid-1
            else:
                n_l = mid+1
            
        return -1

    
        