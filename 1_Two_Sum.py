class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(1, len(nums)):
            if nums[i - 1] + nums[i] == target:
                return [i - 1, i]
        for j in range(0, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[j] + nums[k] == target:
                    return [j, k]


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numsDict = {}

        for i in range(len(nums)):
            tempKey = nums[i]
            toCheck = target - tempKey
            if toCheck in numsDict:
                return [i, numsDict[toCheck]]

            numsDict[tempKey] = i
        return []


test1 = Solution().twoSum([2, 7, 11, 15], 9)

test2 = Solution().twoSum([3, 2, 3], 6)

print(test1, test2)
# test5 = {3: 3, 2: "qwe", 3: 0, 3: 1}

# print(test5[3])
