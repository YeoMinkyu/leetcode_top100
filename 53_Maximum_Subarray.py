class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return None

        d = []
        d.append(nums[0])
        ans = d[0]

        for i in range(1, len(nums)):
            sum_sub = d[i - 1] + nums[i]
            if sum_sub > nums[i]:
                d.append(sum_sub)
            else:
                d.append(nums[i])

            if d[i] > ans:
                ans = d[i]

        return ans