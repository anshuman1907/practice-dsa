class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # l1 = len(nums)
        t1 = sum(range(len(nums) +1))
        print(t1)
        
        return t1 - sum(nums)
        