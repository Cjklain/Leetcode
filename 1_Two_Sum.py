class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(1, len(nums)):
            if nums[i - 1] + nums[i] == target:
                return [i - 1, i]
        for j in range(0, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[j] + nums[k] == target:
                    return [j, k]
                
test1 = Solution().twoSum([2,7,11,15], 9)

test2 = Solution().twoSum([3,2,3], 6)

test5 = {3: 3, 2: 'qwe'}

print(test5[3])