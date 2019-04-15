class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[0]
            else:
                return nums[1]

        rob = [nums[0], nums[1]]

        for idx in range(2, len(nums)):
            price = nums[idx] + max(rob[:(idx - 1)])
            rob.append(price)

        max_price = max(rob)
        return max_price
