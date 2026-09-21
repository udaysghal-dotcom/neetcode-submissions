class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_len = len(nums)
        result = [1] * num_len

        prefix_array = []
        product = 1
        for i in range(num_len):
            # including this curr 
            product *= nums[i]
            prefix_array.append(product)
        
        suffix_array = [0] * num_len
        product = 1
        for i in range(num_len - 1, -1, -1):
            product *= nums[i]
            suffix_array[i] = product
        
        for i in range(num_len):
            if i == 0 or i == num_len - 1:
                continue
            
            val = suffix_array[i+1] * prefix_array[i-1]
            result[i] = val
        
        result[0] = suffix_array[1]
        result[num_len-1] = prefix_array[num_len-2]
        return result
