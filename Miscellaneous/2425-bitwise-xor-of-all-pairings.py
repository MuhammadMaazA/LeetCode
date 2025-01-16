class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # Compute XOR of all elements in nums1
        xor1 = 0
        for num in nums1:
            xor1 ^= num
        
        # Compute XOR of all elements in nums2
        xor2 = 0
        for num in nums2:
            xor2 ^= num
        
        # Initialize the result
        result = 0
        
        # If the length of nums1 is odd, include xor2
        if len(nums1) % 2 == 1:
            result ^= xor2
        
        # If the length of nums2 is odd, include xor1
        if len(nums2) % 2 == 1:
            result ^= xor1
        
        return result
