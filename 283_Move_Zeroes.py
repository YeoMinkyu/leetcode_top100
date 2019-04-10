# TODO : 속도 개선
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = nums.count(0)

        for count in range(0, counts):
            nums.remove(0)
            nums.append(0)