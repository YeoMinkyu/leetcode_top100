class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        result = [0] * (len(nums))

        for num in nums:
            result[num - 1] += 1

        nums.clear()

        for idx, val in enumerate(result):
            if val == 0:
                nums.append(idx + 1)
        return nums