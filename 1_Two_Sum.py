# TODO : 속도 개선
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []

        nums_map = dict()
        result = []

        for idx, num in enumerate(nums):
            nums_map[num] = idx

        print(nums_map)
        for idx, num in enumerate(nums):
            complement = target - num
            print(complement)
            if complement in nums_map and idx != nums_map.get(complement):
                result.append(idx)
                result.append(nums_map.get(complement))
                break

        return result