class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        counters=Counter(nums)
        for key,values in counters.items():
            if values > 1:
                return key
