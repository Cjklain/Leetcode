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


# test1 = Solution().twoSum([2, 7, 11, 15], 9)

# test2 = Solution().twoSum([3, 2, 3], 6)

# print(test1, test2)
# test5 = {3: 3, 2: "qwe", 3: 0, 3: 1}

# print(test5[3])


class Solution3:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if len(nums) > 1000:
            return
        # O2
        # for idi, i in enumerate(nums):
        #     for idx, x in enumerate(nums[idi + 1 :]):
        #         if i + x == target:
        #             return [idi, idx + idi + 1]

        # the range is 10,000,000 and number len is 1000 so 1000x1000 is better

        hashmap = {}
        for i, num in enumerate(nums):
            hashmap[num] = i

        for i, num in enumerate(nums):
            if target - num in hashmap and i != hashmap[target - num]:
                return [i, hashmap[target - num]]


asd = Solution3().twoSum([1, 3, 4, 2], 6)
print(asd)
