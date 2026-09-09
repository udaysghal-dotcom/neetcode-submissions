class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)

        # do binary search though all possible speeds, not banana array
        result = max(piles)
        low = 1
        high = result

        while low <= high:
            mid = ((high - low) // 2) + low
            hours_needed = 0
            
            for num in piles:
                hours_needed += math.ceil(num / mid)

            if hours_needed > h:
                # invalid, increase rate
                low = mid + 1
            else:
                # valid, save into result and look for potential lower
                result = mid
                high = mid - 1
            
        return result
