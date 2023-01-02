#Solution 1
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        counters=Counter(nums)
        for key,values in counters.items():
            if values > 1:
                return key

           
        
#Solution 2        
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

       for i in nums:
            nums[abs(i)-1] *= -1
            if nums[abs(i)-1] > 0: return abs(i)
