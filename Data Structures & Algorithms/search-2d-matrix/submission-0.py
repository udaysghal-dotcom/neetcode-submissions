class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        search_array = None
        for i in range(len(matrix)):
            l_idx = len(matrix[i]) - 1
            if matrix[i][l_idx] < target:
                continue
            else:
                # target must be in this array
                search_array = matrix[i]
                break

        if not search_array:
            # exit early, val does not exist
            return False

        return self.binary_search(search_array, target)  
    
    def binary_search(self, nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = ((high - low) // 2) + low

            if target == nums[mid]:
                return True
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return False