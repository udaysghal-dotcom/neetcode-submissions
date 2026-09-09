class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = ((high - low) // 2) + low

            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1
        
        return nums[low]
