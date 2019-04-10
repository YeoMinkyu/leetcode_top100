class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = set(nums)

        for num in candidate:
            count = nums.count(num)
            if count > (len(nums) * 0.5):
                return num