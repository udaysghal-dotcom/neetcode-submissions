class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = ((high - low) // 2) + low

            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[mid]:
                # low, mid is sorted
                if target < nums[mid] and nums[low] <= target:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1 
        